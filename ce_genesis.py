# ================================ 
# 👁️‍🗨️ CreepyEYE Genesis MAIN 👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================

import time, logging, re, ipaddress
from datetime import datetime, timezone
from settings.translations import status_messages, menu, menu_details, warnings, error_details, settings_details
from settings.helpers import center_text, clear_text, open_api_env, init_language, ask_language_choice, log_warning_yellow, log_error_red
from settings.config import setup_logging, SUPPORTED_LANGS
from settings import config
from settings.report import save_report
from settings.proxy.tor import get_smart_session, is_tor_running, announce_tor_status
from EYE_tools.spiderfoot import stop_spiderfoot
from EYE_tools.hunter_io import hunter_io
from EYE_tools.shodan import shodan_scan
from EYE_tools.virustotal import virustotal
from EYE_tools.search_by_sites import search_by_sites_username
from EYE_tools.ipinfo import ipinfo
from EYE_tools.abuseipdb import abuseipdb
from EYE_tools.greynoise import greynoise
from EYE_tools.emailrep_io import emailrep_io
from EYE_tools.whois import whois
from EYE_tools.numverify import numverify
from termcolor import colored
from rich.console import Console

language = init_language()

setup_logging()
logger = logging.getLogger("EYE_tools.helpers")


# ==================== Validators ====================
def is_valid_phone(phone):
    cleaned = re.sub(r"[ \-\(\)]", "", phone)
    pattern = r"^\+?\d{9,15}$"
    return bool(re.match(pattern, cleaned))

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def is_valid_ip(query):
    try:
        ipaddress.ip_address(query)
        return True
    except ValueError:
        return False

def is_valid_domain(query):
    return re.match(r"^(?!:\/\/)([a-zA-Z0-9-_]+\.)+[a-zA-Z]{2,11}$", query) is not None


# ==================== Terminal utils ====================
def get_terminal_height():
    try:
        import shutil
        return shutil.get_terminal_size().lines
    except Exception:
        return 24  

def count_newlines_for_center(text):
    term_height = get_terminal_height()
    text_height = text.count('\n') + 1
    return max((term_height - text_height) // 2, 0)

def json_toggle_label(language):
    state = (menu_details[language]["json_state_on"] if config.SHOW_JSON
             else menu_details[language]["json_state_off"])
    return menu_details[language]["json_toggle"].format(state=state)


def show_menu_diagonal(language):
    menu_items = menu[language]
    print("\n" + colored(" " + menu_details[language]['menu'].upper(), "magenta", attrs=["bold"]) + "\n")
    for item in menu_items:
        # Пункт 9 (перемикач JSON) друкуємо динамічно перед "0. Вихід",
        # бо його підпис залежить від поточного стану config.SHOW_JSON.
        if item.strip().startswith("0."):
            print(json_toggle_label(language))
            time.sleep(0.1)
        print(item)
        time.sleep(0.1)


# ==================== Input / process ====================
def validated_input(prompt, validator, error_msg):
    value = input(prompt).strip()
    if not validator(value):
        log_warning_yellow(error_msg)
        time.sleep(1.2)
        return None
    return value

def process(funcs, value, language, target_type):
    if value is None:  # <-- guard: не чіпати API при invalid input
        return
    clear_text()
    print(status_messages[language]["processing"].format(query=value))
    started_at = datetime.now(timezone.utc)
    results = []
    for f in funcs:
        r = f(value, language)
        # Модулі повертають єдину схему module_result; решту (None) ігноруємо.
        if isinstance(r, dict) and "module" in r:
            results.append(r)
    finished_at = datetime.now(timezone.utc)
    maybe_save_report(results, value, target_type, language, started_at, finished_at)
    input(menu_details[language]["press_any_key"])


def maybe_save_report(results, target, target_type, language, started_at, finished_at):
    if not results:
        return
    answer = input("\n" + menu_details[language]["save_report_prompt"]).strip().lower()
    if answer not in ("y", "yes"):
        return
    # У звіт пишемо реальний стан анонімізації, а не лише прапорець конфігу.
    tor_active = config.USE_TOR_PROXY and is_tor_running()
    try:
        path = save_report(results, target, target_type, tor_active, started_at, finished_at)
        print(menu_details[language]["report_saved"].format(path=path))
    except Exception as e:
        log_error_red(error_details[language]["error"].format(e=e))


def toggle_json(language):
    # Мутуємо саме config.SHOW_JSON (атрибут модуля), щоб перемикач діяв у межах
    # сесії: модулі читають config.SHOW_JSON у момент виклику.
    config.SHOW_JSON = not config.SHOW_JSON
    print(json_toggle_label(language))
    time.sleep(1)


# ==================== Tor info ====================
def tor_info(language):
    session = get_smart_session(language)
    if not is_tor_running():
        print(warnings[language]["tor_inactive_warning"])
        input(menu_details[language]["press_any_key"])
        return
    try:
        ip_res = session.get("https://httpbin.org/ip", timeout=5)
        if ip_res.status_code == 200:
            ip = ip_res.json().get("origin")
            print(menu_details[language]["tor_ip"].format(ip=ip))
        headers_res = session.get("https://httpbin.org/headers")
        print(headers_res.text)
    except Exception as e:
        print(error_details[language]["error"].format(e=e))
    input(menu_details[language]["press_any_key"])


# ==================== Menu router ====================
def handle_menu_choice(choice, language):
    menu_router = {
        "0": lambda: "exit",

        "1": lambda: process(
            [search_by_sites_username],
            validated_input(
                menu_details[language]["input_username"],
                lambda x: len(x) > 2,
                error_details[language]["invalid_username"]
            ),
            language,
            "username"
        ),

        "2": lambda: process(
            [hunter_io, emailrep_io],
            validated_input(
                menu_details[language]["input_email"],
                is_valid_email,
                error_details[language]["invalid_email"]
            ),
            language,
            "email"
        ),

        "3": lambda: process(
            [ipinfo, shodan_scan, abuseipdb, greynoise, virustotal],
            validated_input(
                menu_details[language]["input_ip"],
                is_valid_ip,
                error_details[language]["invalid_ip"]
            ),
            language,
            "ip"
        ),

        "4": lambda: process(
            [whois, virustotal],
            validated_input(
                menu_details[language]["input_domain"],
                is_valid_domain,
                error_details[language]["invalid_domain"]
            ),
            language,
            "domain"
        ),

        "5": lambda: process(
            [numverify],
            validated_input(
                menu_details[language]["input_phone"],
                is_valid_phone,
                error_details[language]["invalid_phone"]
            ),
            language,
            "phone"
        ),

        "6": lambda: "restart",

        "7": lambda: tor_info(language),

        "8": lambda: ask_language_choice(),

        "9": lambda: toggle_json(language)
    }

    action = menu_router.get(choice)

    if not action:
        print(colored(menu_details[language]["incorrect_option"], "red"))
        time.sleep(1.2)
        return language

    result = action()

    if result == "exit":
        stop_spiderfoot(language)
        return "exit"

    if result == "restart":
        open_api_env(language)
        input(settings_details[language]["restart_required"])
        stop_spiderfoot(language)
        exit()

    if isinstance(result, str):
        return result

    return language


# ==================== Main loop ====================
def main(language):
    title = """  
    ______                           ________  ________      _____                     _     
   / ____/_______  ___  ____  __  __/ ____/\\ \\/ / ____/    / ____/__  ____  ___  _____(_)____
  / /   / ___/ _ \\/ _ \\/ __ \\/ / / / __/    \\  / __/      / / __/ _ \\/ __ \\/ _ \\/ ___/ / ___/
 / /___/ /  /  __/  __/ /_/ / /_/ / /___    / / /___     / /_/ /  __/ / / /  __(__  ) (__  ) 
 \\____/_/   \\___/\\___/ .___/\\__, /_____/   /_/_____/     \\____/\\___/_/ /_/\\___/____/_/____/  
                      /_/    /____/                                                              
"""
    while True:
        clear_text()
        Console().print(center_text(title), style="magenta")
        print("\n" * count_newlines_for_center(title))
        show_menu_diagonal(language)

        choice = input("\n" + colored(menu_details[language]["choose_option"], "magenta")).strip()
        result = handle_menu_choice(choice, language)
        if result == "exit":
            print(colored(menu_details[language]["exit_message"], "magenta"))
            break
        elif result in SUPPORTED_LANGS:
            language = result


# ==================== Entry point ====================
if __name__ == "__main__":
    print(colored("".join(warnings[language]["ethical_use_warning"]), "yellow"))
    print("=" * 60)
    # Один раз, чітко: чи справді запити анонімізуються через Tor.
    announce_tor_status(language)
    input(menu_details[language]["press_any_key"])
    clear_text()
    setup_logging()
    main(language)
