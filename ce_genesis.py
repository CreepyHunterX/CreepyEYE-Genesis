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



# ======= MAIN =======
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

        choice = input("\n" + colored(menu_details[language]["choose_option"], "magenta").strip())

        if choice == '0':
            print(menu_details[language]["exit_message"])
            stop_spiderfoot(language)
            time.sleep(1)
            clear_text()
            break

        elif choice == '1':
            username = input(menu_details[language]["input_username"]).strip()
            if username:
                clear_text()
                print(status_messages[language]["processing"].format(query=username))
                search_by_sites_username(username, language)
            input(menu_details[language]["press_any_key"])

        elif choice == '2':
            email = input(menu_details[language]["input_email"]).strip()
            if is_valid_email(email):
                clear_text()
                print(status_messages[language]["processing"].format(query=email))
                hunter_io(email, language)
                emailrep_io(email, language)
                spiderfoot(email, language)
            else:
                log_warning_yellow(error_details[language]["invalid_email"])
            input(menu_details[language]["press_any_key"])

        elif choice == '3':
            ip = input(menu_details[language]["input_ip"]).strip()
            if is_valid_ip(ip):
                clear_text()
                print(status_messages[language]["processing"].format(query=ip))
                ipinfo(ip, language)
                shodan_scan(ip, language)
                abuseipdb(ip, language)
                greynoise(ip, language)
                virustotal(ip, language)
                spiderfoot(ip, language)
            else:
                log_warning_yellow(error_details[language]["invalid_ip"])
            input(menu_details[language]["press_any_key"])

        elif choice == '4':
            domain = input(menu_details[language]["input_domain"]).strip()
            if is_valid_domain(domain):
                clear_text()
                print(status_messages[language]["processing"].format(query=domain))
                whois(domain, language)
                virustotal(domain, language)
                spiderfoot(domain, language)
                input(menu_details[language]["press_any_key"])
            else:
                log_warning_yellow(error_details[language]["invalid_domain"])
            input(menu_details[language]["press_any_key"])

        elif choice == '5':
            phone = input(menu_details[language]["input_phone"]).strip()
            if is_valid_phone(phone):
                clear_text()
                print(status_messages[language]["processing"].format(query=phone))
                numverify(phone, language)
            else: 
                log_warning_yellow(error_details[language]["invalid_phone"])
            input(menu_details[language]["press_any_key"])

        elif choice == '6':
            open_api_env(language) 
            input(settings_details[language]["restart_required"])
            stop_spiderfoot(language)
            time.sleep(1)
            break

        elif choice == '7':
            session = get_smart_session(language)
            if is_tor_running():
                try:
                    ip_res = session.get("http://httpbin.org/ip", timeout=5)
                    if ip_res.status_code == 200:
                        ip = ip_res.json().get("origin")
                        print(menu_details[language]["tor_ip"].format(ip=ip))
                    headers_res = session.get("http://httpbin.org/headers")
                    print(headers_res.text)
                except Exception as e:
                    print(error_details[language]["error"].format(e=e))
            else:
                print(warnings[language]["tor_inactive_warning"])
            input(menu_details[language]["press_any_key"])     

        elif choice == '8':
            language = ask_language_choice()

        else:
            print(colored(menu_details[language]["incorrect_option"], "red"))
            time.sleep(1)

if __name__ == "__main__":
    
    print(colored("".join(warnings[language]["ethical_use_warning"]), "yellow"))
    print("=" * 60)
    input(menu_details[language]["press_any_key"])
    clear_text()

    setup_logging()
    main(language)
