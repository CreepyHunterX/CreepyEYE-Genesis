# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================


import json, logging
from settings.translations import check_messages, error_details, info_details, status_messages
from settings.api.api import NUMVERIFY_API_KEY, validate_api_key
from settings.config import SHOW_JSON
from settings.helpers import log_error_red, log_warning_yellow
from settings.make_request import make_request
from termcolor import colored

logger = logging.getLogger("EYE_tools.numverify")

def numverify(phone, language="en"):
    logger.info("\n" + check_messages[language]["numverify_check"].format(query=phone))

    if not validate_api_key(NUMVERIFY_API_KEY, "NumVerify", language=language):
        return
    
    try:
        url = "https://apilayer.net/api/validate"
        params = {
            "access_key": NUMVERIFY_API_KEY,
            "number": phone,
            "country_code": "",
            "format": 1
        }
        data = make_request("GET", url, params=params, language=language)

        if data and isinstance(data, dict):
        
            if SHOW_JSON:
                print(json.dumps(data, indent=2, ensure_ascii=False))

            if data.get("valid"):
                print(colored(info_details[language]["country"], "green"), f"{data.get('country_name', 'N/A')}")
                print(colored(info_details[language]["carrier"], "green"), f"{data.get('carrier', 'N/A')}")
                print(colored(info_details[language]["location"], "green"), f"{data.get('location', 'N/A')}")
            else:
                log_warning_yellow(status_messages[language]["no_results"])
                return
        else:
            log_warning_yellow(error_details[language]["empty_response"])
            return
    
    except json.JSONDecodeError as e:
        log_error_red(error_details[language]["json_error"].format(e=e))
        return
    except Exception as e:
        log_error_red(error_details[language]["error"].format(e=e))
        return