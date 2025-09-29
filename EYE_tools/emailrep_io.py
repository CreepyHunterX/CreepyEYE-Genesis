# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================


import json, logging
from settings.translations import check_messages, info_details, error_details, status_messages
from settings.api.api import EMAILREP_API_KEY, validate_api_key
from settings.config import SHOW_JSON
from settings.helpers import log_error_red, log_warning_yellow
from settings.make_request import make_request
from termcolor import colored

logger = logging.getLogger("EYE_tools.emailrep_io")


def process_emailrep_result(result, language="en"):
    if result:
        print(colored(info_details[language]["reputation"], "green"), result.get('reputation', 'N/A'))
        print(colored(info_details[language]["suspicious"], "green"), result.get('suspicious', 'N/A'))
        print(colored(info_details[language]["blacklist"], "green"), result.get('blacklisted', 'N/A'))
        print(colored(info_details[language]["leaked_passwords"], "green"), result.get('credentials_leaked', 'N/A'))
        print(colored(info_details[language]["activity"], "green"), result.get('malicious_activity', 'N/A'))
        print(colored(info_details[language]["domain_checked"], "green"), result.get('details', {}).get('domain_exists', 'N/A'))
    else:
        log_warning_yellow(status_messages[language]["no_results"])

def emailrep_io(email, language):
    logger.info("\n" + check_messages[language]["emailrep_check"].format(query=email))

    url = f"https://emailrep.io/{email}"

    if not validate_api_key(EMAILREP_API_KEY, "EmailRep", language=language):
        return
    
    try:
        result = make_request("GET", url, api_key=EMAILREP_API_KEY, key_type="Bearer", language=language)

        if result and isinstance(result, dict):
            if SHOW_JSON:
                print(json.dumps(result, indent=2, ensure_ascii=False))
            process_emailrep_result(result, language=language)
        else:
            log_warning_yellow(error_details[language]["empty_response"])
    except json.JSONDecodeError as e:
        log_error_red(error_details[language]["json_error"].format(e=e))
    except Exception as e:
        log_error_red(error_details[language]["api_error"].format(e=e))
