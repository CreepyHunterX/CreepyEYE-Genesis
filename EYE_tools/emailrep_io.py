# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================


import json, logging
from settings.translations import check_messages, info_details, error_details, status_messages
from settings.api.api import EMAILREP_API_KEY, validate_api_key
from settings import config
from settings.helpers import log_error_red, log_warning_yellow, print_json, module_result
from settings.make_request import make_request
from termcolor import colored

logger = logging.getLogger("EYE_tools.emailrep_io")


def process_emailrep_result(result, language="en"):
    if result:
        # reputation/suspicious лежать на верхньому рівні, решта — у details.
        details = result.get('details', {}) or {}
        print(colored(info_details[language]["reputation"], "green"), result.get('reputation', 'N/A'))
        print(colored(info_details[language]["suspicious"], "green"), result.get('suspicious', 'N/A'))
        print(colored(info_details[language]["blacklist"], "green"), details.get('blacklisted', 'N/A'))
        print(colored(info_details[language]["leaked_passwords"], "green"), details.get('credentials_leaked', 'N/A'))
        print(colored(info_details[language]["activity"], "green"), details.get('malicious_activity', 'N/A'))
        print(colored(info_details[language]["domain_checked"], "green"), details.get('domain_exists', 'N/A'))
    else:
        log_warning_yellow(status_messages[language]["no_results"])

def emailrep_io(email, language):
    logger.info("\n" + check_messages[language]["emailrep_check"].format(query=email))

    url = f"https://emailrep.io/{email}"

    if not validate_api_key(EMAILREP_API_KEY, "EmailRep", language=language):
        return module_result("emailrep", "error", error="missing or invalid API key")

    try:
        result = make_request("GET", url, api_key=EMAILREP_API_KEY, key_type="Key", language=language)

        if result and isinstance(result, dict):
            if config.SHOW_JSON:
                print_json(result)
            process_emailrep_result(result, language=language)
            return module_result("emailrep", "ok", data=result)
        else:
            log_warning_yellow(error_details[language]["empty_response"])
            return module_result("emailrep", "empty")
    except json.JSONDecodeError as e:
        log_error_red(error_details[language]["json_error"].format(e=e))
        return module_result("emailrep", "error", error=str(e))
    except Exception as e:
        log_error_red(error_details[language]["api_error"].format(e=e))
        return module_result("emailrep", "error", error=str(e))
