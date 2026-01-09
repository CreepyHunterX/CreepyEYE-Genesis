# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================


import subprocess, socket, json, time, logging, sys, os
from settings.translations import spiderfoot_details, status_messages, warnings, error_details, check_messages
from settings.config import SHOW_JSON, spiderfoot_process, SPIDERFOOT_PORT
from settings.helpers import log_error_red, log_warning_yellow
from settings.make_request import make_request
from termcolor import colored

logger = logging.getLogger("EYE_tools.spiderfoot")
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def is_spiderfoot_running(host='127.0.0.1', port=SPIDERFOOT_PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        return sock.connect_ex((host, port)) == 0

def start_spiderfoot(language):
    global spiderfoot_process

    if not is_spiderfoot_running():
        print(colored(spiderfoot_details[language]["not_running"], "red") + "\n" + colored(spiderfoot_details[language]["start"], "green"))
        try:
            spiderfoot_path = os.path.join(os.getcwd(), "spiderfoot", "sf.py")
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
    else:
        log_warning_yellow(spiderfoot_details[language]["already_running"])

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

    url = f"http://localhost:{SPIDERFOOT_PORT}/api/query?query={query}"
    try:
        data = make_request("GET", url, language=language)
        if data and SHOW_JSON:
            try:
                print(json.dumps(data, indent=2, ensure_ascii=False))
            except UnicodeEncodeError:
                print(colored(warnings[language]["ascii_warning"], "yellow"))
                print(json.dumps(data, indent=2, ensure_ascii=True))
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
