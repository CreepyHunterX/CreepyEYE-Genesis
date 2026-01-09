# ================================ 
# 👁️‍🗨️ CreepyEYE Genesis MAIN 👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================

import time, logging, re, ipaddress   
from settings.translations import status_messages, menu, menu_details, warnings, error_details, settings_details
from settings.helpers import center_text, clear_text, open_api_env, init_language, ask_language_choice, log_warning_yellow
from settings.config import setup_logging
from settings.proxy.tor import get_smart_session, is_tor_running
from EYE_tools.spiderfoot import stop_spiderfoot, spiderfoot
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

def show_menu_diagonal(language):
    menu_items = menu[language]
    print("\n" + colored(" " + menu_details[language]['menu'].upper(), "magenta", attrs=["bold"]) + "\n")
    for i, item in enumerate(menu_items):
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

def process(funcs, value, language):
    if value is None:  # <-- guard: не чіпати API при invalid input
        return
    clear_text()
    print(status_messages[language]["processing"].format(query=value))
    for f in funcs:
        f(value, language)
    input(menu_details[language]["press_any_key"])


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
            language
        ),

        "2": lambda: process(
            [hunter_io, emailrep_io, spiderfoot],
            validated_input(
                menu_details[language]["input_email"],
                is_valid_email,
                error_details[language]["invalid_email"]
            ),
            language
        ),

        "3": lambda: process(
            [ipinfo, shodan_scan, abuseipdb, greynoise, virustotal, spiderfoot],
            validated_input(
                menu_details[language]["input_ip"],
                is_valid_ip,
                error_details[language]["invalid_ip"]
            ),
            language
        ),

        "4": lambda: process(
            [whois, virustotal, spiderfoot],
            validated_input(
                menu_details[language]["input_domain"],
                is_valid_domain,
                error_details[language]["invalid_domain"]
            ),
            language
        ),

        "5": lambda: process(
            [numverify],
            validated_input(
                menu_details[language]["input_phone"],
                is_valid_phone,
                error_details[language]["invalid_phone"]
            ),
            language
        ),

        "6": lambda: "restart",

        "7": lambda: tor_info(language),

        "8": lambda: ask_language_choice()
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
        if result == "break":
            break
        elif isinstance(result, str):
            language = result  


# ==================== Entry point ====================
if __name__ == "__main__":
    print(colored("".join(warnings[language]["ethical_use_warning"]), "yellow"))
    print("=" * 60)
    input(menu_details[language]["press_any_key"])
    clear_text()
    setup_logging()
    main(language)
