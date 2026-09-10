# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================

import json, logging
from settings.translations import status_messages, info_details, error_details, check_messages, warnings
from settings.api.api import GREYNOISE_API_KEY, validate_api_key
from settings import config
from settings.helpers import log_error_red, log_warning_yellow, print_json, module_result
from settings.make_request import make_request
from termcolor import colored

logger = logging.getLogger("EYE_tools.greynoise")

def greynoise(ip, language="en"):
    logger.info("\n" + check_messages[language]["greynoise_check"].format(query=ip))

    if not validate_api_key(GREYNOISE_API_KEY, "GreyNoise", language=language):
        return module_result("greynoise", "error", error="missing or invalid API key")

    paid_url = f"https://api.greynoise.io/v3/noise/{ip}"
    free_url = f"https://api.greynoise.io/v3/community/{ip}"

    try:
        response = make_request(
            "GET",
            paid_url,
            api_key=GREYNOISE_API_KEY,
            key_type="Key",
            language=language
        )

        if not response or (isinstance(response, dict) and response.get("message") == "Forbidden"):
            logger.warning(warnings[language]["community_api_fallback"])
            response = make_request(
                "GET",
                free_url,
                api_key=GREYNOISE_API_KEY,
                key_type="Bearer",
                language=language
            )

        if response and isinstance(response, dict):
            if config.SHOW_JSON:
                print_json(response)

            if "classification" in response:
                print(colored(info_details[language]["classification"], "green"), f"{response.get('classification', 'N/A')}")
                print(colored(info_details[language]["name"], "green"), f"{response.get('name', 'N/A')}")
                return module_result("greynoise", "ok", data=response)
            else:
                log_warning_yellow(status_messages[language]["no_results"])
                return module_result("greynoise", "empty")
        else:
            log_warning_yellow(error_details[language]["empty_response"])
            return module_result("greynoise", "empty")

    except json.JSONDecodeError as e:
        log_error_red(error_details[language]["json_error"].format(e=e))
        return module_result("greynoise", "error", error=str(e))
    except Exception as e:
        log_error_red(error_details[language]["error"].format(e=e))
        return module_result("greynoise", "error", error=str(e))
