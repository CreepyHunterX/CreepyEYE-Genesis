# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================


import json, logging
from settings.translations import status_messages, info_details, error_details, check_messages
from settings.api.api import GREYNOISE_API_KEY, validate_api_key
from settings.config import SHOW_JSON
from settings.helpers import log_error_red, log_warning_yellow
from settings.make_request import make_request
from termcolor import colored

logger = logging.getLogger("EYE_tools.greynoise")

def greynoise(ip, language="en"):
    logger.info("\n" + check_messages[language]["greynoise_check"].format(query=ip))
    if not validate_api_key(GREYNOISE_API_KEY, "GreyNoise", language=language):
        return
    try:
        url = f"https://api.greynoise.io/v3/community/{ip}"
        data = make_request("GET", url, api_key=GREYNOISE_API_KEY, language=language)

        if data and isinstance(data, dict):
            if SHOW_JSON:
                print(json.dumps(data, indent=2, ensure_ascii=False))
            if "classification" in data:
                print(colored(info_details[language]["classification"], "green"), f"{data.get('classification', 'N/A')}")
                print(colored(info_details[language]["name"], "green"), f"{data.get('name', 'N/A')}")
            else:
                log_warning_yellow(status_messages[language]["no_results"])
        else:
            log_warning_yellow(error_details[language]["empty_response"])
    except json.JSONDecodeError as e:
        log_error_red(error_details[language]["json_error"].format(e=e))
        return
    except Exception as e:
        log_error_red(error_details[language]["error"].format(e=e))
        return