# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================


import logging, shutil, platform, os, locale, subprocess, sys, time 
from pathlib import Path
from settings.translations import settings_details, error_details, menu_details
from settings.install_if_missing import check_and_install
from settings.config import SUPPORTED_LANGS

def set_language(lang_code):
    os.environ["LANGUAGE"] = lang_code if lang_code in SUPPORTED_LANGS else "en"

def get_system_language():
    try:
        lang, _ = locale.getdefaultlocale()
        if lang:
            lang_code = lang[:2].lower()
            return lang_code if lang_code in SUPPORTED_LANGS else "en"
    except (ValueError, TypeError):
        pass
    return "en"



    


def init_language():
    lang = os.environ.get("LANGUAGE") or get_system_language()
    if lang not in SUPPORTED_LANGS:
        lang = "en"
    set_language(lang)
    return lang

try:
    from termcolor import colored
except ImportError:
    def ask_to_install(language="en"):
        for _ in range(3): 
            ask = input(settings_details[language]["some_modules_missing"]).strip().lower()
            if ask in ("y", "yes"):
                check_and_install("termcolor", language)
                check_and_install("requests", language)
                check_and_install("python-dotenv", language)
                check_and_install("rich", language)
                import importlib
                importlib.import_module("termcolor")
                return
            elif ask in ("n", "no"):
                print(settings_details[language]["install_requirements"])
                print(menu_details[language]["exit_message"])
                time.sleep(2)
                sys.exit()
            else:
                print(settings_details[language]["invalid_option"])
        print(settings_details[language]["too_many_attempts"])
        time.sleep()
        sys.exit()
    language = init_language()

    ask_to_install(language)
    from termcolor import colored


def get_terminal_size():
    size = shutil.get_terminal_size((80, 20))  
    return size.columns, size.lines

def ask_language_choice():
    print("🌐 Select language / Оберіть мову:")
    print("1. 🇺🇸 English")
    print("2. 🇺🇦 Українська")
    print("3. 🇷🇺 Русский")
    choice = input("→ ")
    return "uk" if choice == "2" else "ru" if choice == "3" else "en"

def log_warning_yellow(message: str):
    colored_msg = colored(message, "yellow")
    logging.warning(colored_msg)

def log_error_red(message: str, exc: Exception = None):
    colored_msg = colored(message, "red")
    if exc:
        logging.error(colored_msg, exc_info=True)
    else:
        logging.error(colored_msg)

def open_api_env(language="en"):
    path = Path("settings/api/api_keys.env")
    create_env_file_if_not_exists(path, language)

    system = platform.system()
    try:
        if system == "Windows":
            os.startfile(path)
        elif system == "Darwin":
            subprocess.run(["open", str(path)])
        else:
            subprocess.run(["xdg-open", str(path)])
    except Exception as e:
        log_error_red(error_details[language]["env_errors"])

def create_env_file_if_not_exists(env_path: Path, language="en"):
    default_env_content = """SHODAN_API_KEY=your_shodan_api_key
IPINFO_TOKEN=your_ipinfo_token
ABUSEIPDB_KEY=your_abuseipdb_key
HUNTER_API_KEY=your_hunter_api_key
VIRUSTOTAL_API_KEY=your_virustotal_api_key
NUMVERIFY_API_KEY=your_numverify_api_key
GREYNOISE_API_KEY=your_greynoise_api_key
EMAILREP_API_KEY=your_emailrep_api_key
WHOIS_API_KEY=your_whois_api_key
"""
    if not env_path.exists():
        env_path.parent.mkdir(parents=True, exist_ok=True)
        with env_path.open("w") as f:
            f.write(default_env_content)
        print(settings_details[language]["env_file_created"].format(env_path=env_path))


def clear_text():
    os.system("cls" if platform.system() == "Windows" else "clear")

def center_text(text: str) -> str:
    columns, _ = get_terminal_size()
    return "\n".join(line.center(columns) for line in text.splitlines())


def check_api_key(key, api_name, language="en"):
    if not key:
        log_error_red(settings_details[language]["missing_api_key"].format(name=api_name))
        return False
    return True
