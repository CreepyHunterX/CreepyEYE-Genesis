# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================

import importlib, subprocess, sys
from settings.translations import settings_details, warnings, menu_details

def check_and_install(import_name, pip_name=None, language="en"):
    # Ім'я для import != ім'я пакета в pip (dotenv/python-dotenv, socks/PySocks).
    # Плутанина призводила до import_module("python-dotenv"), який завжди падав,
    # тож інсталятор пропонував ставити вже встановлений пакет.
    pip_name = pip_name or import_name
    try:
        importlib.import_module(import_name)
    except ImportError:
        ans = input(settings_details[language]["module_not_found"].format(module_name=pip_name)).strip().lower()
        if ans == 'y':
            subprocess.call([sys.executable, "-m", "pip", "install", pip_name])
        else:
            print(warnings[language]["missing_module"].format(module_name=pip_name))
            print(menu_details[language]["exit_message"])
            sys.exit()