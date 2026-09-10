# ================================
# 👁️‍🗨️ CreepyEYE Genesis TESTS  👁️‍🗨️
# Pre-commit round 2: JSON-перемикач і збереження звітів.
# Запуск:  python -m unittest discover -s tests
# ================================

import io
import json
import os
import sys
import shutil
import tempfile
import unittest
from contextlib import redirect_stdout
from datetime import datetime, timezone

# Корінь репозиторію у sys.path, щоб імпортувати settings/ і EYE_tools/.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from settings import config              # noqa: E402
from settings import report as report_mod  # noqa: E402
from EYE_tools import shodan as shodan_mod  # noqa: E402

WHEN = datetime(2026, 9, 10, 21, 40, 0, tzinfo=timezone.utc)


class RuntimeJsonToggleTest(unittest.TestCase):
    """Перемикач JSON має міняти поведінку модуля ПІД ЧАС роботи, а не лише
    після перезапуску — це ловить пастку `from settings.config import SHOW_JSON`."""

    def setUp(self):
        self._orig = {
            "validate": shodan_mod.validate_api_key,
            "make": shodan_mod.make_request,
            "print_json": shodan_mod.print_json,
            "show": config.SHOW_JSON,
        }
        self.printed = []
        shodan_mod.validate_api_key = lambda *a, **k: True
        shodan_mod.make_request = lambda *a, **k: {"org": "ACME", "ports": [80]}
        shodan_mod.print_json = lambda data: self.printed.append(data)

    def tearDown(self):
        shodan_mod.validate_api_key = self._orig["validate"]
        shodan_mod.make_request = self._orig["make"]
        shodan_mod.print_json = self._orig["print_json"]
        config.SHOW_JSON = self._orig["show"]

    def _run(self):
        with redirect_stdout(io.StringIO()):
            return shodan_mod.shodan_scan("8.8.8.8", "en")

    def test_toggle_affects_behavior_at_runtime(self):
        config.SHOW_JSON = False
        result = self._run()
        self.assertEqual(self.printed, [], "JSON не мав друкуватися при OFF")
        self.assertEqual(result["status"], "ok")

        # Змінюємо стан у тому ж процесі — без перезапуску.
        config.SHOW_JSON = True
        self._run()
        self.assertEqual(len(self.printed), 1, "JSON мав надрукуватися після ON")


class ReportFilenameTest(unittest.TestCase):
    """IPv6-ціль має давати валідне ім'я файлу для Windows (без ':')."""

    def test_ipv6_target_safe_filename(self):
        path = report_mod.build_report_path("2001:db8::1", "ip", WHEN)
        base = os.path.basename(path)
        for ch in ':<>"|?*':
            self.assertNotIn(ch, base, f"символ {ch!r} заборонений у Windows-іменах")
        self.assertTrue(base.endswith(".json"))
        self.assertIn("20260910-214000", base)


class ReportContentTest(unittest.TestCase):
    """Звіт: без витоку ключа та з цілою кирилицею."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self._orig_dir = report_mod.REPORTS_DIR
        report_mod.REPORTS_DIR = self.tmp

    def tearDown(self):
        report_mod.REPORTS_DIR = self._orig_dir
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_api_key_not_written(self):
        # Сира відповідь інколи повертає URL із ключем — він не має потрапити у файл.
        results = [{
            "module": "shodan",
            "status": "ok",
            "data": {"echoed_url": "https://api.shodan.io/host?key=SUPERSECRET123&x=1"},
            "error": None,
        }]
        path = report_mod.save_report(results, "8.8.8.8", "ip", False, WHEN, WHEN)
        with open(path, encoding="utf-8") as f:
            content = f.read()
        self.assertNotIn("SUPERSECRET123", content)
        self.assertIn("REDACTED", content)

    def test_cyrillic_roundtrip(self):
        org = "Приклад Організації «Тест»"
        results = [{
            "module": "whois",
            "status": "ok",
            "data": {"org": org},
            "error": None,
        }]
        path = report_mod.save_report(results, "example.com", "domain", False, WHEN, WHEN)
        with open(path, encoding="utf-8") as f:
            loaded = json.load(f)
        self.assertEqual(loaded["results"][0]["data"]["org"], org)


if __name__ == "__main__":
    unittest.main()
