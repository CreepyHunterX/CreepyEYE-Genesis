# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================

import os, logging

VERSION = "1.1"
SPIDERFOOT_PORT = 5001
# Стан JSON-виводу тримаємо тут і читаємо як config.SHOW_JSON у момент виклику,
# а НЕ через `from settings.config import SHOW_JSON` (інакше значення копіюється
# один раз при старті й перемикач у меню не працюватиме під час сесії).
SHOW_JSON = False
spiderfoot_process = None
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
USE_TOR_PROXY = True  
TOR_PROXY = "socks5h://127.0.0.1:9050"
SUPPORTED_LANGS = {"uk", "en", "ru"}

def setup_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )