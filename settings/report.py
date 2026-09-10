# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================

import os, re, json
from datetime import datetime, timezone

from settings.config import VERSION
from settings.make_request import redact_obj

REPORTS_DIR = "reports"


def _safe_name(value: str) -> str:
    # Двокрапки IPv6 та часу ламають шляхи у Windows — лишаємо лише безпечні символи.
    return re.sub(r"[^A-Za-z0-9._-]", "_", str(value))


def build_report_path(target, target_type, when=None) -> str:
    when = when or datetime.now(timezone.utc)
    ts = when.strftime("%Y%m%d-%H%M%S")
    name = f"{_safe_name(target)}_{_safe_name(target_type)}_{ts}.json"
    return os.path.join(REPORTS_DIR, name)


def _iso(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def save_report(results, target, target_type, tor_active,
                started_at, finished_at):
    """Зберігає звіт у reports/ у форматі JSON (UTF-8, без ASCII-екранування).
    Усі значення проходять redact_obj, щоб ключі з сирих відповідей не потрапили
    у файл. Повертає шлях до збереженого файлу."""
    os.makedirs(REPORTS_DIR, exist_ok=True)

    report = {
        "tool": "CreepyEYE Genesis",
        "version": VERSION,
        "target": target,
        "type": target_type,
        "started_at": _iso(started_at),
        "finished_at": _iso(finished_at),
        "tor": bool(tor_active),
        "results": redact_obj(results),
    }

    path = build_report_path(target, target_type, finished_at)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    return path
