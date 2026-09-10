# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================


import subprocess, socket, json, time, logging, sys, os
from settings.translations import spiderfoot_details, status_messages, warnings, error_details, check_messages
from settings import config
from settings.config import spiderfoot_process, SPIDERFOOT_PORT
from settings.helpers import log_error_red, log_warning_yellow, print_json
from settings.make_request import make_request
from termcolor import colored

logger = logging.getLogger("EYE_tools.spiderfoot")
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def is_spiderfoot_running(host='127.0.0.1', port=SPIDERFOOT_PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        return sock.connect_ex((host, port)) == 0

def sf_script_path():
    return os.path.join(os.getcwd(), "spiderfoot", "sf.py")


def start_spiderfoot(language):
    global spiderfoot_process

    if is_spiderfoot_running():
        log_warning_yellow(spiderfoot_details[language]["already_running"])
        return

    spiderfoot_path = sf_script_path()
    # Без встановленого sf.py Popen все одно "стартував" би python, який миттєво
    # падає, а цикл нижче марно чекав би 10 секунд на порт. Виходимо одразу.
    if not os.path.exists(spiderfoot_path):
        log_warning_yellow(spiderfoot_details[language]["missing_sf_script"])
        return

    print(colored(spiderfoot_details[language]["not_running"], "red") + "\n" + colored(spiderfoot_details[language]["start"], "green"))
    try:
        spiderfoot_process = subprocess.Popen(
            [sys.executable, spiderfoot_path, "-l", f"127.0.0.1:{SPIDERFOOT_PORT}"]
        )
        for _ in range(10):
            if is_spiderfoot_running():
                break
            time.sleep(1)
        else:
            log_error_red(spiderfoot_details[language]["start_error"].format(e="Spiderfoot did not start in time."))
    except Exception as e:
        log_error_red(spiderfoot_details[language]["start_error"].format(e=e))

def stop_spiderfoot(language):
    global spiderfoot_process
    if spiderfoot_process and spiderfoot_process.poll() is None:
        try:
            spiderfoot_process.terminate()
            spiderfoot_process.wait()
            print(colored(spiderfoot_details[language]["stop"], "green"))
        except Exception as e:
            log_error_red(spiderfoot_details[language]["stop_error"].format(e=e))

def spiderfoot(query, language="en"):
    import requests
    logger.info("\n" + check_messages[language]["spiderfoot_check"].format(query=query))

    start_spiderfoot(language)

    # Якщо SpiderFoot не вдалося підняти (не встановлено / не стартував) —
    # не тиснемо в неіснуючий сервіс, просто пропускаємо модуль.
    if not is_spiderfoot_running():
        return

    # TODO(feature): /api/query не існує в SpiderFoot — потрібен повноцінний
    # запуск скану через його API з подальшим опитуванням статусу.
    url = f"http://localhost:{SPIDERFOOT_PORT}/api/query?query={query}"
    try:
        data = make_request("GET", url, language=language)
        if data and config.SHOW_JSON:
            print_json(data)
        if data:
            print(colored(status_messages[language]["results_found"], "green"))
            print(data)
        else:
            log_warning_yellow(status_messages[language]["no_results"])
    except requests.exceptions.Timeout:
        log_error_red(spiderfoot_details[language]["timeout_error"])
        return
    except requests.exceptions.RequestException as e:
        log_error_red(spiderfoot_details[language]["request_error"].format(e=e))
        return
    except Exception as e:
        log_error_red(error_details[language]["error"].format(e=e))
        return
