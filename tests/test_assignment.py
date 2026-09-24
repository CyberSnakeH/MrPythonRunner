import base64
import copy
import tempfile
import time
import unittest

from runner.app import Application
from runner.formats import assign_pack, export_pack, import_pack, import_work, validate_pack

SOLUTION = 'def carre(n: int) -> int:\n    """Retourne le carré."""\n    return n * n\n'


class AssignmentTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.teacher = Application(self.directory.name + '/teacher')
        self.pupil = Application(self.directory.name + '/pupil', seed=False)
        self.export = self.teacher.call('/api/pack/export', {'pack_id': 'premiers-pas', 'student': ' 01234 '})
        self.pack = self.pupil.call('/api/pack/import', {'data': self.export['data']})['pack']

    def tearDown(self):
        self.teacher.jobs.close()
        self.pupil.jobs.close()
        self.directory.cleanup()

    def call(self, action, **kwargs):
        return self.pupil.call('/api/' + action, {'pack_id': self.pack['id'], **kwargs})

    def test_distribution_preserves_template_and_student_leading_zero(self):
        self.assertEqual(self.pack['assignment'], {'source_pack_id': 'premiers-pas', 'student_id': '01234'})
        self.assertEqual(self.pack['version'], 2)
        self.assertIn('01234', self.export['filename'])
        self.assertEqual(len(self.teacher.store.packs()), 1)
        self.assertNotIn('assignment', self.teacher.store.pack('premiers-pas'))
        self.assertEqual(self.call('student/open', student=' 01234 ')['student'], '01234')

    def test_wrong_or_missing_id_rejected_for_every_student_operation(self):
        for action in ('student/open', 'drafts', 'draft/save', 'work/export', 'jobs/start'):
            for student in ('111', '1234', 'other', '', None):
                with self.subTest(action=action, student=student), self.assertRaises(ValueError):
                    self.call(action, student=student, exercise_id='carre', code=SOLUTION)
        with self.assertRaises(ValueError):
            self.call('jobs/start', exercise_id='carre', code=SOLUTION)

    def test_identifiers_are_case_sensitive(self):
        assigned = assign_pack(self.teacher.store.pack('premiers-pas'), 'Alice')
        self.pupil.store.save_pack(assigned)
        with self.assertRaises(ValueError):
            self.pupil.call('/api/student/open', {'pack_id': assigned['id'], 'student': 'alice'})

    def test_unassigned_template_rejects_all_student_operations(self):
        for action in ('student/open', 'drafts', 'draft/save', 'work/export', 'jobs/start'):
            with self.subTest(action=action), self.assertRaisesRegex(ValueError, 'modèle professeur'):
                self.teacher.call('/api/' + action, {'pack_id': 'premiers-pas', 'student': '111',
                                                    'exercise_id': 'carre', 'code': SOLUTION})

    def test_teacher_can_still_try_unassigned_template(self):
        job = self.teacher.call('/api/jobs/start', {'pack_id': 'premiers-pas', 'exercise_id': 'carre', 'code': SOLUTION})
        deadline = time.monotonic() + 10
        while time.monotonic() < deadline:
            state = self.teacher.jobs.get(job['id'])
            if state['state'] == 'done': break
            time.sleep(.05)
        self.assertEqual(state['state'], 'done')
        self.assertEqual(state['report']['status'], 'passed')

    def test_distributions_coexist_and_reexport_preserves_identity(self):
        other = self.teacher.call('/api/pack/export', {'pack_id': 'premiers-pas', 'student': '56789'})
        other_pack = self.pupil.call('/api/pack/import', {'data': other['data']})['pack']
        self.assertNotEqual(other_pack['id'], self.pack['id'])
        self.assertEqual(len(self.pupil.store.packs()), 2)
        again = self.teacher.call('/api/pack/export', {'pack_id': 'premiers-pas', 'student': '01234'})
        self.assertEqual(import_pack(base64.b64decode(again['data'])), self.pack)

    def test_assigned_copy_cannot_be_edited_or_downgraded(self):
        for remove_assignment in (False, True):
            changed = copy.deepcopy(self.pack)
            changed['title'] = 'Changed'
            if remove_assignment:
                del changed['assignment']
                changed['version'] = 1
            with self.assertRaises(ValueError):
                self.call('pack/save', pack=changed)
            if remove_assignment:
                with self.assertRaises(ValueError):
                    self.call('pack/import', data=base64.b64encode(export_pack(changed)).decode(), replace=True)
        with self.assertRaises(ValueError):
            self.call('pack/export', student='other')

    def test_assignment_metadata_is_validated(self):
        for field, value in (('version', 1), ('version', True), ('assignment', None), ('id', 'wrong')):
            changed = copy.deepcopy(self.pack)
            changed[field] = value
            with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                validate_pack(changed)

    def test_student_grades_and_teacher_reviews_using_original_template(self):
        job = self.call('jobs/start', student='01234', exercise_id='carre', code=SOLUTION)
        deadline = time.monotonic() + 10
        while time.monotonic() < deadline:
            state = self.call('jobs/get', id=job['id'])
            if state['state'] == 'done': break
            time.sleep(.05)
        self.assertEqual(state['state'], 'done')
        self.assertEqual(state['report']['status'], 'passed', state)
        work = self.call('work/export', student='01234')
        parsed = import_work(base64.b64decode(work['data']))
        self.assertEqual(parsed['version'], 2)
        self.assertEqual(parsed['source_pack_id'], 'premiers-pas')
        reviewed = self.teacher.call('/api/work/import', {'data': work['data']})
        self.assertTrue(reviewed['matching'])
        self.assertEqual(reviewed['pack_id'], 'premiers-pas')
        self.assertEqual(reviewed['work']['answers'][0]['code'], SOLUTION)
        template = self.teacher.store.pack('premiers-pas')
        template['exercises'][0]['tests'][0]['code'] = 'assert carre(5) == 25'
        self.teacher.call('/api/pack/save', {'pack': template})
        self.assertFalse(self.teacher.call('/api/work/import', {'data': work['data']})['matching'])

    def test_response_restore_requires_same_student_on_another_device(self):
        self.call('draft/save', student='01234', exercise_id='carre', code=SOLUTION)
        work = self.call('work/export', student='01234')
        other = Application(self.directory.name + '/other', seed=False)
        try:
            other.call('/api/pack/import', {'data': self.export['data']})
            for path in ('work/import', 'work/restore'):
                for identity in (None, 'wrong'):
                    with self.subTest(path=path, identity=identity), self.assertRaises(ValueError):
                        other.call('/api/' + path, {'data': work['data'], 'purpose': 'restore', 'student': identity})
            other.call('/api/work/restore', {'data': work['data'], 'student': '01234'})
            self.assertEqual(other.store.drafts('01234', self.pack['id'])['carre']['code'], SOLUTION)
        finally:
            other.jobs.close()

    def test_export_requires_teacher_to_enter_an_identifier(self):
        for student in ('', None, '   '):
            with self.subTest(student=student), self.assertRaises(ValueError):
                self.teacher.call('/api/pack/export', {'pack_id': 'premiers-pas', 'student': student})


if __name__ == '__main__':
    unittest.main()
