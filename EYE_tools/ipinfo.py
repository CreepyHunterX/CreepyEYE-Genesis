# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================


import json, logging
from settings.translations import check_messages, info_details, error_details
from settings.api.api import IPINFO_TOKEN, validate_api_key
from settings.helpers import log_error_red, log_warning_yellow, print_json, module_result
from settings.make_request import make_request
from settings import config
from termcolor import colored

logger = logging.getLogger("EYE_tools.ipinfo")

def ipinfo(ip, language="en"):
    logger.info("\n" + check_messages[language]["ipinfo_check"].format(query=ip))

    if not validate_api_key(IPINFO_TOKEN, "Ipinfo", language=language):
        return module_result("ipinfo", "error", error="missing or invalid API key")

    try:
        url = f"https://ipinfo.io/{ip}"
        data = make_request("GET", url, api_key=IPINFO_TOKEN, language=language)

        if data and isinstance(data, dict):
            if config.SHOW_JSON:
                print_json(data)
            print(colored(info_details[language]["ip_info"], "green"))
            for k, v in data.items():
                print(f"{k.capitalize()}: {v}")
            return module_result("ipinfo", "ok", data=data)
        else:
            log_warning_yellow(error_details[language]["empty_response"])
            return module_result("ipinfo", "empty")
    except json.JSONDecodeError as e:
        log_error_red(error_details[language]["json_error"].format(e=e))
        return module_result("ipinfo", "error", error=str(e))
    except Exception as e:
        log_error_red(error_details[language]["error"].format(e=e))
        return module_result("ipinfo", "error", error=str(e))