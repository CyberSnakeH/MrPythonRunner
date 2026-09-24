"""Validate and publish the rewritten teacher bank, preserving the previous edition."""
import ast
from collections import Counter
from datetime import datetime
import json
from pathlib import Path
import sys
import tempfile
import textwrap
import time
import zipfile

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from runner.engine import grade
from runner.formats import assign_pack, check_student, export_pack, import_pack
from runner.jobs import Jobs
from runner.storage import Store
from course2022_v2_core import ITEMS, SERIES
import course2022_v2_ch2
import course2022_v2_ch3
import course2022_v2_ch4
import course2022_v2_ch5

OUT = ROOT / 'exercices/cours2022-chapitres-2-5'
ZIP = OUT.parent / 'cours2022-chapitres-2-5-professeur.zip'


def pack_for(identifier, title, items, description):
    return {'format': 'mrpython-pack', 'version': 1, 'id': identifier, 'title': title,
            'description': description, 'author': 'Banque pédagogique — nouvelle rédaction, édition 2',
            'assets': {}, 'exercises': [item['exercise'] for item in items]}


def refuses_student(pack, identity):
    try:
        check_student(pack, identity)
    except ValueError:
        return True
    return False


def validate_references():
    assert len(ITEMS) == 60
    assert Counter(i['series'] for i in ITEMS) == {n: 5 for n in range(1, 13)}
    assert len({i['name'] for i in ITEMS}) == 60
    assert len({i['exercise']['id'] for i in ITEMS}) == 60
    checks = []
    for item in ITEMS:
        exercise = item['exercise']
        ast.parse(exercise['starter'])
        report = grade(item['solution'], exercise['tests'], exercise['points'])
        starter = grade(exercise['starter'], exercise['tests'], exercise['points'])
        constant_code = item['head'] + '    return ' + repr(item['cases'][0][1]) + '\n'
        constant = grade(constant_code, exercise['tests'], exercise['points'])
        assert report['status'] == 'passed', (item['name'], report)
        assert starter['status'] == 'failed', (item['name'], starter)
        assert constant['status'] != 'passed', (item['name'], constant)
        assert not report['diagnostics'], (item['name'], report['diagnostics'])
        checks.append({'exercise': exercise['id'], 'function': item['name'],
                       'tests': len(exercise['tests']), 'passed': report['passed'],
                       'solution': report['status'], 'starter': starter['status'],
                       'constant_answer': constant['status'], 'diagnostics': report['diagnostics']})
    return checks


def validate_workers(master):
    with tempfile.TemporaryDirectory(prefix='course-v2-validation-') as directory:
        store = Store(directory)
        assigned = assign_pack(master, 'validation-01234')
        store.save_pack(assigned)
        jobs = Jobs(store)
        results = []
        for name in ('commande_partageable', 'assemblages_boites', 'eau_debordee',
                     'premiere_baisse', 'normaliser_espaces', 'contenu_balise'):
            item = next(i for i in ITEMS if i['name'] == name)
            job = jobs.start(assigned['id'], item['exercise']['id'], item['solution'], 'validation-01234')
            deadline = time.monotonic() + 20
            result = jobs.get(job['id'])
            while result['state'] != 'done' and time.monotonic() < deadline:
                time.sleep(0.05)
                result = jobs.get(job['id'])
            assert result['state'] == 'done', (name, result)
            assert result['report']['status'] == 'passed', (name, result)
            results.append({'function': name, 'status': result['report']['status'],
                            'passed': result['report']['passed'], 'total': result['report']['total']})
        try:
            jobs.start(assigned['id'], ITEMS[0]['exercise']['id'], ITEMS[0]['solution'], '111')
        except ValueError:
            pass
        else:
            raise AssertionError('Wrong student identity accepted by Jobs')
        return results


def build(destination):
    checks = validate_references()
    overview = '# Nouvelle banque — chapitres 2 à 5\n\n60 nouveaux problèmes en 12 séries de 5 exercices, fondés sur les notions du cours fourni. Chaque sujet précise la situation, les règles, les données et deux exemples expliqués.\n\n'
    overview += 'Ce parcours travaille les notions principales, sans fonction passée en paramètre ni récursion. Conservez les signatures, annotez les variables et retournez les résultats. Les justifications et méthodes imposées sont relues par le professeur.\n\n'
    overview += '| Série | Chapitre | Thème |\n|---|---|---|\n'
    progression = '| Série | Chapitre / pages imprimées | Thème | Exercices | Points |\n|---|---|---|---|---|\n'
    for index, (chapter, title, _, pages, _) in enumerate(SERIES, 1):
        overview += f'| S{index:02} | {chapter} | {title} |\n'
        points = sum(i['exercise']['points'] for i in ITEMS if i['series'] == index)
        progression += f'| S{index:02} | {chapter} / {pages} | {title} | {(index-1)*5+1:02}–{index*5:02} | {points} |\n'
    master = pack_for('cours2022-r2-ch2-5-professeur', 'Nouvelle banque — Chapitres 2 à 5 · 60 exercices', ITEMS, overview)
    worker_checks = validate_workers(master)
    destination.mkdir(parents=True)
    (destination / 'series').mkdir()
    (destination / 'corriges-professeur').mkdir()
    for item in ITEMS:
        exercise = item['exercise']
        correction = '# CORRIGÉ PROFESSEUR — ne pas distribuer aux élèves.\n# ' + exercise['title'] + '\n'
        if item['notes']:
            correction += textwrap.fill(item['notes'], width=96, initial_indent='# ', subsequent_indent='# ') + '\n'
        correction += '\n' + item['solution'] + '\n# Vérifications\n' + '\n'.join(t['code'] for t in exercise['tests']) + '\n'
        (destination / 'corriges-professeur' / (exercise['id'] + '.py')).write_text(correction, encoding='utf-8')
    exports = []
    for index, (chapter, title, section, pages, objective) in enumerate(SERIES, 1):
        selected = [i for i in ITEMS if i['series'] == index]
        description = f'# Série {index:02} — {title}\n\n{objective}\n\nChapitre {chapter}, sections {section}, pages imprimées {pages}.\n\nCinq problèmes rédigés pour cette banque, avec exemples expliqués. Les tests évaluent les résultats ; les méthodes imposées et raisonnements sont relus par le professeur.'
        pack = pack_for(f'cours2022-r2-s{index:02}-professeur', f'Nouvelle banque · C{chapter} · S{index:02} — {title}', selected, description)
        exports.append((destination / 'series' / f'serie-{index:02}-chapitre-{chapter}.mrpack', pack))
    exports.append((destination / 'professeur-chapitres-2-a-5.mrpack', master))
    for path, pack in exports:
        path.write_bytes(export_pack(pack))
        assert import_pack(path.read_bytes()) == pack
        assigned = import_pack(export_pack(assign_pack(pack, 'validation-01234')))
        assert check_student(assigned, 'validation-01234') == 'validation-01234'
        assert refuses_student(assigned, '111')
        assert refuses_student(pack, 'validation-01234')
        assert all('solution' not in e for e in pack['exercises'])
    total_tests = sum(len(i['exercise']['tests']) for i in ITEMS)
    total_points = sum(i['exercise']['points'] for i in ITEMS)
    (destination / 'professeur-chapitres-2-a-5.json').write_text(json.dumps(master, ensure_ascii=False, indent=2), encoding='utf-8')
    guide = (ROOT / 'scripts/course2022_v2_guide.md').read_text(encoding='utf-8')
    guide = guide.replace('{{PROGRESSION}}', progression).replace('{{TESTS}}', str(total_tests)).replace('{{POINTS}}', str(total_points))
    (destination / 'LIRE-MOI-PROFESSEUR.md').write_text(guide, encoding='utf-8')
    justifications = (ROOT / 'scripts/course2022_v2_justifications.md').read_text(encoding='utf-8')
    (destination / 'JUSTIFICATIONS-CHAPITRE-4.md').write_text(justifications, encoding='utf-8')
    statements = '# Les 60 nouveaux énoncés — chapitres 2 à 5\n\nÉdition 2. Les corrigés sont fournis séparément au professeur.\n\n'
    for item in ITEMS:
        exercise = item['exercise']
        statements += '\n---\n\n# ' + exercise['title'] + '\n\n' + exercise['statement'] + '\n\n### Code de départ\n\n```python\n' + exercise['starter'] + '```\n'
    (destination / 'ENONCES.md').write_text(statements, encoding='utf-8')
    validation = {'edition': 2, 'exercises': len(ITEMS), 'series': len(SERIES), 'tests': total_tests,
                  'points': total_points, 'kinds': dict(Counter(i['exercise']['kind'] for i in ITEMS)),
                  'roundtrip_packs': len(exports), 'assigned_roundtrips': len(exports),
                  'wrong_identity_rejected': True, 'teacher_templates_blocked_for_students': True,
                  'worker_checks': worker_checks, 'checks': checks}
    (destination / 'validation.json').write_text(json.dumps(validation, ensure_ascii=False, indent=2), encoding='utf-8')
    return validation


def main():
    stamp = datetime.now().strftime('%Y%m%d-%H%M%S-%f')
    stage_root = ROOT / 'test-results' / ('course-v2-' + stamp)
    staged = stage_root / OUT.name
    validation = build(staged)
    staged_zip = stage_root / ZIP.name
    with zipfile.ZipFile(staged_zip, 'w', zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(staged.rglob('*')):
            if path.is_file():
                archive.write(path, Path(OUT.name) / path.relative_to(staged))
    with zipfile.ZipFile(staged_zip) as archive:
        assert archive.testzip() is None
        assert len(archive.namelist()) == 78
    # Resolve and check every directory move before preserving/replacing an edition.
    archive_dir = OUT.parent / 'archives' / ('cours2022-chapitres-2-5-avant-remplacement-' + stamp)
    for path in (OUT, ZIP, staged, staged_zip, archive_dir):
        assert path.resolve().is_relative_to(ROOT.resolve()), path
    archive_dir.mkdir(parents=True)
    if OUT.exists():
        OUT.rename(archive_dir / OUT.name)
    if ZIP.exists():
        ZIP.rename(archive_dir / ZIP.name)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    staged.rename(OUT)
    staged_zip.rename(ZIP)
    print(json.dumps({'pack': str(OUT / 'professeur-chapitres-2-a-5.mrpack'),
                      'zip': str(ZIP), 'archive': str(archive_dir),
                      'exercises': validation['exercises'], 'tests': validation['tests'],
                      'points': validation['points']}, ensure_ascii=True))


if __name__ == '__main__':
    main()
