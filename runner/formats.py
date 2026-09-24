"""Versioned, bounded ZIP/JSON formats. Never extract imported paths to disk."""
import ast
import base64
import hashlib
import io
import json
import re
import zipfile
import copy
import uuid
from pathlib import PurePosixPath

MAX_ARCHIVE = 16 * 1024 * 1024
MAX_UNPACKED = 24 * 1024 * 1024
ID = re.compile(r"^[a-zA-Z0-9_-]{1,80}$")
ASSET = re.compile(r"^assets/[a-zA-Z0-9_-]+\.(png|jpg|jpeg|webp|gif)$")
KINDS = {"function", "complete", "debug"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def text(value, name, maximum=100_000, empty=True):
    require(isinstance(value, str) and len(value) <= maximum, f"{name} : texte invalide ou trop long.")
    require(empty or bool(value.strip()), f"{name} est obligatoire.")
    return value


def identifier(value):
    require(isinstance(value, str) and bool(ID.fullmatch(value)), "Identifiant de fichier invalide.")
    return value


def student_id(value):
    text(value, "Identifiant élève", 80, empty=False)
    require(not any(ord(c) < 32 for c in value), "Identifiant élève invalide.")
    return value.strip()


def assigned_pack_id(source_id, student):
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"mrpython:{source_id}:{student}"))


def check_student(pack, student):
    require(bool(pack.get("assignment")),
            "Ce fichier est un modèle professeur sans identifiant attribué. Le professeur doit utiliser « Distribuer à un élève » pour créer votre fichier personnel.")
    student = student_id(student)
    if pack.get("assignment"):
        require(student == pack["assignment"]["student_id"],
                "Cet identifiant ne correspond pas à l’élève auquel ce fichier est attribué.")
    return student


def assign_pack(pack, student):
    validate_pack(pack)
    require(not pack.get("assignment"), "Utilisez le modèle professeur pour attribuer une série.")
    student = student_id(student)
    result = copy.deepcopy(pack)
    result.update(version=2, id=assigned_pack_id(pack["id"], student),
                  assignment={"source_pack_id": pack["id"], "student_id": student})
    return validate_pack(result)


def validate_pack(pack):
    require(isinstance(pack, dict) and pack.get("format") == "mrpython-pack"
            and type(pack.get("version")) is int and pack["version"] in (1, 2),
            "Format de série inconnu. Versions 1 et 2 acceptées.")
    identifier(pack.get("id"))
    if pack["version"] == 2:
        assignment = pack.get("assignment")
        require(isinstance(assignment, dict), "Attribution élève manquante.")
        source = identifier(assignment.get("source_pack_id"))
        student = student_id(assignment.get("student_id"))
        require(student == assignment["student_id"], "Identifiant élève non normalisé.")
        require(pack["id"] == assigned_pack_id(source, student), "Attribution de série incohérente.")
    else:
        require("assignment" not in pack, "Une série attribuée nécessite le format version 2.")
    text(pack.get("title"), "Titre", 200, empty=False)
    text(pack.get("description", ""), "Description", 20_000)
    text(pack.get("author", ""), "Auteur", 200)
    exercises = pack.get("exercises")
    require(isinstance(exercises, list) and len(exercises) <= 100, "Maximum : 100 exercices par série.")
    ids = set()
    for ex in exercises:
        require(isinstance(ex, dict), "Exercice invalide.")
        identifier(ex.get("id"))
        require(ex["id"] not in ids, "Identifiants d'exercices dupliqués.")
        ids.add(ex["id"])
        require(ex.get("kind") in KINDS, "Type d'exercice inconnu.")
        text(ex.get("title"), "Titre de l'exercice", 200, empty=False)
        text(ex.get("statement"), "Énoncé")
        text(ex.get("starter"), "Code initial")
        require(type(ex.get("points")) in (float, int) and 0 < ex["points"] <= 1000, "Barème : de 0 à 1000 points, strictement positif.")
        require(type(ex.get("timeout")) in (float, int) and 1 <= ex["timeout"] <= 30, "Délai : de 1 à 30 secondes.")
        tests = ex.get("tests")
        require(isinstance(tests, list) and len(tests) <= 50, "Maximum : 50 tests par exercice.")
        test_ids = set()
        for test in tests:
            require(isinstance(test, dict), "Test invalide.")
            identifier(test.get("id"))
            require(test["id"] not in test_ids, "Identifiants de tests dupliqués.")
            test_ids.add(test["id"])
            text(test.get("label"), "Nom du test", 200, empty=False)
            text(test.get("code"), "Code du test", 20_000)
            require(type(test.get("hidden", False)) is bool, "Visibilité du test invalide.")
    assets = pack.get("assets", {})
    require(isinstance(assets, dict) and len(assets) <= 100, "Maximum : 100 images.")
    size = 0
    for name, data in assets.items():
        require(bool(ASSET.fullmatch(name)), "Nom d'image invalide. PNG, JPEG, GIF et WebP acceptés.")
        text(data, "Image", 8_000_000)
        try:
            raw = base64.b64decode(data, validate=True)
        except Exception as exc:
            raise ValueError("Image encodée incorrectement.") from exc
        size += len(raw)
    require(size <= 12 * 1024 * 1024, "Les images dépassent 12 Mo.")
    return pack


def validate_tests(exercise):
    require(bool(exercise["tests"]), "Ajoutez au moins un test avant de corriger ou d'exporter.")
    for test in exercise["tests"]:
        try:
            tree = ast.parse(test["code"], "test.py")
        except SyntaxError as exc:
            raise ValueError(f"Test « {test['label']} » : {exc.msg}, ligne {exc.lineno}.") from exc
        require(any(isinstance(node, ast.Assert) for node in tree.body),
                f"Le test « {test['label']} » doit contenir au moins un assert au niveau principal.")


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                     allow_nan=False).encode()).hexdigest()


def _read_zip(raw):
    require(len(raw) <= MAX_ARCHIVE, "Fichier trop volumineux (16 Mo maximum).")
    try:
        archive = zipfile.ZipFile(io.BytesIO(raw))
        infos = archive.infolist()
        require(len(infos) <= 110, "Archive contenant trop de fichiers.")
        require(sum(i.file_size for i in infos) <= MAX_UNPACKED, "Archive décompressée trop volumineuse.")
        names = [i.filename for i in infos]
        require(len(names) == len(set(names)), "Archive contenant des noms dupliqués.")
        for name in names:
            p = PurePosixPath(name)
            require(not p.is_absolute() and ".." not in p.parts and "\\" not in name
                    and ":" not in name, "Chemin interdit dans l'archive.")
        return archive
    except (zipfile.BadZipFile, OSError) as exc:
        raise ValueError("Ce fichier n'est pas une archive MrPython valide.") from exc


def export_pack(pack):
    validate_pack(pack)
    require(bool(pack["exercises"]), "Ajoutez un exercice avant d'exporter.")
    for ex in pack["exercises"]:
        validate_tests(ex)
    manifest = {k: v for k, v in pack.items() if k != "assets"}
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("manifest.json", json.dumps(manifest, ensure_ascii=False, allow_nan=False))
        for name, data in pack.get("assets", {}).items():
            archive.writestr(name, base64.b64decode(data))
    raw = stream.getvalue()
    require(len(raw) <= MAX_ARCHIVE, "La série dépasse 16 Mo.")
    return raw


def import_pack(raw):
    with _read_zip(raw) as archive:
        require("manifest.json" in archive.namelist(), "manifest.json manquant.")
        pack = json.loads(archive.read("manifest.json"))
        require(isinstance(pack, dict), "Manifeste invalide.")
        pack["assets"] = {}
        for name in archive.namelist():
            if name != "manifest.json":
                require(bool(ASSET.fullmatch(name)), "Fichier inattendu dans la série.")
                pack["assets"][name] = base64.b64encode(archive.read(name)).decode()
    return validate_pack(pack)


def export_work(work):
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("submission.json", json.dumps(work, ensure_ascii=False, allow_nan=False))
    return stream.getvalue()


def import_work(raw):
    with _read_zip(raw) as archive:
        require(archive.namelist() == ["submission.json"], "Fichier de réponses invalide.")
        work = json.loads(archive.read("submission.json"))
    require(isinstance(work, dict) and work.get("format") == "mrpython-work" and type(work.get("version")) is int and work["version"] in (1, 2),
            "Format de réponses inconnu.")
    work["student"] = student_id(work.get("student"))
    identifier(work.get("pack_id"))
    if work["version"] == 2:
        source = identifier(work.get("source_pack_id"))
        require(work["pack_id"] == assigned_pack_id(source, work["student"]), "L’identifiant de cette copie ne correspond pas à son attribution.")
    text(work.get("pack_fingerprint"), "Version de série", 64, empty=False)
    answers = work.get("answers")
    require(isinstance(answers, list) and len(answers) <= 100, "Réponses invalides.")
    ids = set()
    for answer in answers:
        require(isinstance(answer, dict), "Réponse invalide.")
        identifier(answer.get("exercise_id"))
        require(answer["exercise_id"] not in ids, "Réponse dupliquée.")
        ids.add(answer["exercise_id"])
        text(answer.get("code"), "Réponse")
    # Local grades are explicitly untrusted; teachers must re-run the code.
    return work
