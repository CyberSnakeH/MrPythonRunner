import base64
import copy
import io
import json
import sys
import tempfile
import threading
import time
import unittest
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

from runner.app import Application, create_server
from runner.engine import MAX_OUTPUT, grade
from runner.formats import assign_pack, export_pack, export_work, fingerprint, import_pack, import_work, validate_pack, validate_tests
from runner.jobs import Jobs
from runner.storage import Store

ROOT = Path(__file__).resolve().parent.parent
SOLUTION = 'def carre(n: int) -> int:\n    """Retourne le carré de n."""\n    return n * n\n'


def sample():
    return json.loads((ROOT / 'examples/premiers-pas.json').read_text(encoding='utf-8'))


class EngineTests(unittest.TestCase):
    def test_passes_all_tests_and_awards_points(self):
        result = grade(SOLUTION, sample()['exercises'][0]['tests'], 4)
        self.assertEqual((result['status'], result['passed'], result['score']), ('passed', 3, 4))

    def test_failure_does_not_stop_other_tests(self):
        ex = sample()['exercises'][0]
        result = grade(ex['starter'], ex['tests'], 4)
        self.assertEqual([t['passed'] for t in result['tests']], [False, True, False])
        self.assertEqual(result['status'], 'failed')
        self.assertEqual(result['score'], 1.33)

    def test_mrpython_type_error_prevents_grading(self):
        result = grade(SOLUTION.replace('n * n', '"texte"'), sample()['exercises'][0]['tests'])
        self.assertEqual(result['status'], 'type_error')
        self.assertTrue(result['diagnostics'])
        self.assertEqual(result['tests'], [])

    def test_syntax_error_has_original_line(self):
        result = grade('def f(:\n', [])
        self.assertEqual(result['status'], 'syntax_error')
        self.assertEqual(result['diagnostics'][0]['line'], 1)

    def test_runtime_line_matches_student_source(self):
        result = grade(SOLUTION.replace('n * n', 'n // 0'), sample()['exercises'][0]['tests'])
        self.assertEqual(result['tests'][0]['error']['line'], 3)
        self.assertEqual(result['tests'][0]['error']['file'], 'eleve.py')

    def test_student_assertion_failure_is_not_counted_as_success(self):
        result = grade(SOLUTION + '\nassert carre(2) == 9\n', sample()['exercises'][0]['tests'])
        self.assertEqual(result['passed'], 0)
        self.assertEqual(result['status'], 'failed')

    def test_preconditions_are_enforced(self):
        source = 'def positif(n: int) -> int:\n    """Retourne n.\n    Précondition : n > 0\n    """\n    return n\n'
        tests = [{'id': 'p', 'label': 'Positif', 'code': 'assert positif(2) == 2'},
                 {'id': 'n', 'label': 'Négatif', 'code': 'assert positif(-1) == -1'}]
        result = grade(source, tests)
        self.assertEqual([t['passed'] for t in result['tests']], [True, False])
        self.assertIn('Précondition', result['tests'][1]['error']['details'])

    def test_fresh_student_globals_for_each_test(self):
        tests = [{'id': 'a', 'label': 'A', 'code': 'carre = lambda n: -1\nassert carre(1) == -1'},
                 {'id': 'b', 'label': 'B', 'code': 'assert carre(3) == 9'}]
        self.assertEqual(grade(SOLUTION, tests)['passed'], 2)

    def test_no_gui_is_imported(self):
        grade(SOLUTION, sample()['exercises'][0]['tests'])
        self.assertFalse(any(name == 'tkinter' or name.startswith('tkinter.') for name in sys.modules))

    def test_output_is_bounded(self):
        result = grade(SOLUTION, [{'id': 'o', 'label': 'Sortie', 'code': "print('a' * 100000)\nassert True"}])
        self.assertLess(len(result['output']), MAX_OUTPUT + 100)
        self.assertIn('limitée', result['output'])

    def test_empty_tests_never_award_success(self):
        self.assertEqual(grade(SOLUTION, [])['status'], 'no_tests')


class FormatTests(unittest.TestCase):
    def archive(self, items):
        stream = io.BytesIO()
        with zipfile.ZipFile(stream, 'w', zipfile.ZIP_DEFLATED) as archive:
            for name, content in items:
                archive.writestr(name, content)
        return stream.getvalue()

    def test_round_trip_preserves_latex_code_and_images(self):
        pack = sample()
        pack['assets']['assets/figure.png'] = base64.b64encode(b'png-fixture').decode()
        self.assertEqual(import_pack(export_pack(pack)), pack)

    def test_rejects_path_traversal_and_unknown_files(self):
        for name in ('../outside.py', '/absolute.png', 'assets/../../outside', 'C:\\evil.py', 'run.py'):
            with self.subTest(name=name), self.assertRaises(ValueError):
                import_pack(self.archive([('manifest.json', json.dumps(sample())), (name, 'x')]))

    def test_rejects_oversized_decompression(self):
        with self.assertRaises(ValueError):
            import_pack(self.archive([('manifest.json', 'x' * (25 * 1024 * 1024))]))

    def test_rejects_version_duplicate_ids_and_invalid_points(self):
        for change in ('version', 'duplicate', 'points'):
            p = sample()
            if change == 'version': p['version'] = 99
            if change == 'duplicate': p['exercises'].append(copy.deepcopy(p['exercises'][0]))
            if change == 'points': p['exercises'][0]['points'] = float('nan')
            with self.subTest(change=change), self.assertRaises(ValueError):
                validate_pack(p)

    def test_export_rejects_no_tests_and_silent_test_scripts(self):
        p = sample()
        p['exercises'][0]['tests'] = []
        with self.assertRaises(ValueError): export_pack(p)
        p['exercises'][0]['tests'] = [{'id': 't', 'label': 'T', 'code': 'print(42)'}]
        with self.assertRaises(ValueError): validate_tests(p['exercises'][0])

    def test_work_round_trip(self):
        work = {'format': 'mrpython-work', 'version': 1, 'student': 'Élève 27', 'pack_id': 'premiers-pas',
                'pack_fingerprint': fingerprint(sample()), 'answers': [{'exercise_id': 'carre', 'code': SOLUTION}]}
        self.assertEqual(import_work(export_work(work)), work)


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.store = Store(self.directory.name)
        self.pack = assign_pack(sample(), 'alice')
        self.store.save_pack(self.pack)

    def tearDown(self):
        self.directory.cleanup()

    def test_students_are_separate_and_persist_across_restarts(self):
        self.store.save_draft('alice', self.pack['id'], 'carre', SOLUTION)
        bob = assign_pack(sample(), 'bob')
        self.store.save_pack(bob)
        other = Store(self.directory.name)
        self.assertEqual(other.drafts('alice', self.pack['id'])['carre']['code'], SOLUTION)
        self.assertEqual(other.drafts('bob', bob['id']), {})

    def test_editing_code_invalidates_grade(self):
        ex = self.pack['exercises'][0]
        self.store.save_draft('alice', self.pack['id'], ex['id'], SOLUTION)
        self.store.record_attempt('alice', self.pack['id'], ex, SOLUTION, grade(SOLUTION, ex['tests']))
        self.assertIsNotNone(self.store.drafts('alice', self.pack['id'])[ex['id']]['report'])
        self.store.save_draft('alice', self.pack['id'], ex['id'], SOLUTION + '\n')
        self.assertIsNone(self.store.drafts('alice', self.pack['id'])[ex['id']]['report'])

    def test_edited_tests_invalidate_grade_without_losing_code(self):
        ex = self.pack['exercises'][0]
        self.store.save_draft('alice', self.pack['id'], ex['id'], SOLUTION)
        self.store.record_attempt('alice', self.pack['id'], ex, SOLUTION, grade(SOLUTION, ex['tests']))
        ex['tests'][0]['code'] = 'assert carre(5) == 25'
        self.store.save_pack(self.pack)
        draft = self.store.drafts('alice', self.pack['id'])[ex['id']]
        self.assertEqual(draft['code'], SOLUTION)
        self.assertIsNone(draft['report'])

    def test_late_report_does_not_overwrite_newer_code(self):
        ex = self.pack['exercises'][0]
        self.store.save_draft('alice', self.pack['id'], ex['id'], SOLUTION + '\n')
        self.store.record_attempt('alice', self.pack['id'], ex, SOLUTION, grade(SOLUTION, ex['tests']))
        self.assertIsNone(self.store.drafts('alice', self.pack['id'])[ex['id']]['report'])


class JobTests(StoreTests):
    def setUp(self):
        super().setUp()
        self.jobs = Jobs(self.store)

    def tearDown(self):
        self.jobs.close()
        super().tearDown()

    def wait(self, job):
        deadline = time.monotonic() + 10
        while time.monotonic() < deadline:
            state = self.jobs.get(job['id'])
            if state['state'] == 'done': return state['report']
            time.sleep(.05)
        self.fail('Worker did not stop within 10 seconds')

    def slow_exercise(self):
        ex = self.pack['exercises'][0]
        ex['timeout'] = 1
        ex['tests'] = [{'id': 'loop', 'label': 'Boucle', 'code': 'while True:\n    pass\nassert True'}]
        self.store.save_pack(self.pack)

    def test_subprocess_grades_and_persists(self):
        report = self.wait(self.jobs.start(self.pack['id'], 'carre', SOLUTION, 'alice'))
        self.assertEqual(report['status'], 'passed', report)
        self.assertEqual(self.store.drafts('alice', self.pack['id'])['carre']['report']['status'], 'passed')

    def test_deadline_stops_infinite_loop(self):
        self.slow_exercise()
        self.assertEqual(self.wait(self.jobs.start(self.pack['id'], 'carre', SOLUTION, 'alice'))['status'], 'timeout')

    def test_cancel_and_single_job_limit(self):
        self.slow_exercise()
        job = self.jobs.start(self.pack['id'], 'carre', SOLUTION, 'alice')
        with self.assertRaises(ValueError): self.jobs.start(self.pack['id'], 'carre', SOLUTION, 'alice')
        self.jobs.cancel(job['id'])
        self.assertEqual(self.wait(job)['status'], 'cancelled')


class ApiTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.app = Application(self.directory.name)
        self.server = create_server(self.app)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.url = f'http://127.0.0.1:{self.server.server_port}'

    def tearDown(self):
        self.app.jobs.close()
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()
        self.directory.cleanup()

    def request(self, path, data=None, token=True, origin=None):
        headers = {'Content-Type': 'application/json'}
        if token: headers['X-Runner-Token'] = self.app.token
        if origin: headers['Origin'] = origin
        request = urllib.request.Request(self.url + '/api/' + path, data=json.dumps(data or {}).encode(), headers=headers)
        with urllib.request.urlopen(request, timeout=5) as response:
            return json.load(response)

    def test_api_requires_token_and_same_origin(self):
        for args in ({'token': False}, {'origin': 'https://example.invalid'}):
            with self.assertRaises(urllib.error.HTTPError) as error:
                self.request('state', **args)
            self.assertEqual(error.exception.code, 403)
            error.exception.close()

    def test_tikz_worker_is_local_and_only_worker_can_compile_wasm(self):
        if not (ROOT / 'frontend/dist/vendor/tikzjax/run-tex.js').exists():
            self.skipTest('Build the frontend to check bundled TikZ resources.')
        for path in ('/', '/vendor/tikzjax/run-tex.js', '/vendor/tikzjax/core.dump.gz',
                     '/vendor/tikzjax/tex.wasm.gz', '/vendor/tikzjax/fonts.css'):
            with urllib.request.urlopen(self.url + path, timeout=5) as response:
                policy = response.headers['Content-Security-Policy']
                self.assertEqual("'wasm-unsafe-eval'" in policy, path.endswith('/run-tex.js'))
                self.assertNotIn("'unsafe-eval'", policy)
                self.assertIn("connect-src 'self'", policy)
                self.assertGreater(len(response.read()), 0)

    def test_distribution_submission_review_round_trip(self):
        state = self.request('state')
        self.assertEqual(len(state['packs']), 1)
        exported = self.request('pack/export', {'pack_id': 'premiers-pas', 'student': 'eleve-42'})
        imported = self.request('pack/import', {'data': exported['data']})
        self.assertEqual(imported['pack']['title'], sample()['title'])
        self.request('draft/save', {'student': 'eleve-42', 'pack_id': imported['pack']['id'], 'exercise_id': 'carre', 'code': SOLUTION})
        work = self.request('work/export', {'student': 'eleve-42', 'pack_id': imported['pack']['id']})
        reviewed = self.request('work/import', {'data': work['data']})
        self.assertTrue(reviewed['matching'])
        self.assertEqual(reviewed['work']['answers'][0]['code'], SOLUTION)

    def test_import_conflict_does_not_overwrite(self):
        pack = sample()
        pack['title'] = 'Autre version'
        data = base64.b64encode(export_pack(pack)).decode()
        response = self.request('pack/import', {'data': data})
        self.assertTrue(response['conflict'])
        self.assertEqual(self.app.store.pack(pack['id'])['title'], sample()['title'])


if __name__ == '__main__':
    unittest.main()
