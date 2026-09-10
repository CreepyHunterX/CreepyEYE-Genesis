# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================


import json, logging
from settings.translations import check_messages, error_details, info_details, status_messages
from settings.api.api import NUMVERIFY_API_KEY, validate_api_key
from settings import config
from settings.helpers import log_error_red, log_warning_yellow, print_json, module_result
from settings.make_request import make_request
from termcolor import colored

logger = logging.getLogger("EYE_tools.numverify")

def numverify(phone, language="en"):
    logger.info("\n" + check_messages[language]["numverify_check"].format(query=phone))

    if not validate_api_key(NUMVERIFY_API_KEY, "NumVerify", language=language):
        return module_result("numverify", "error", error="missing or invalid API key")

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

            if config.SHOW_JSON:
                print_json(data)

            # При проблемі з ключем/квотою NumVerify віддає 200 з success:false.
            if data.get("success") is False:
                err = data.get("error", {}) or {}
                log_error_red(error_details[language]["api_error"].format(
                    e=err.get("info") or err.get("type") or err))
                return module_result("numverify", "error", error=str(err.get("info") or err.get("type") or err))

            if data.get("valid"):
                print(colored(info_details[language]["country"], "green"), f"{data.get('country_name', 'N/A')}")
                print(colored(info_details[language]["carrier"], "green"), f"{data.get('carrier', 'N/A')}")
                print(colored(info_details[language]["location"], "green"), f"{data.get('location', 'N/A')}")
                return module_result("numverify", "ok", data=data)
            else:
                log_warning_yellow(status_messages[language]["no_results"])
                return module_result("numverify", "empty", data=data)
        else:
            log_warning_yellow(error_details[language]["empty_response"])
            return module_result("numverify", "empty")

    except json.JSONDecodeError as e:
        log_error_red(error_details[language]["json_error"].format(e=e))
        return module_result("numverify", "error", error=str(e))
    except Exception as e:
        log_error_red(error_details[language]["error"].format(e=e))
        return module_result("numverify", "error", error=str(e))