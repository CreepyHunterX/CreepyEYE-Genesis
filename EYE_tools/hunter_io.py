# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================


import json, logging
from settings.translations import check_messages, info_details, error_details, status_messages
from settings.config import SHOW_JSON
from settings.api.api import HUNTER_API_KEY, validate_api_key
from settings.helpers import log_error_red, log_warning_yellow
from settings.make_request import make_request
from termcolor import colored

logger = logging.getLogger("EYE_tools.hunter_io")


def hunter_io(email, language="en"):
    logger.info("\n" + check_messages[language]["hunter_check"].format(query=email))

    if not validate_api_key(HUNTER_API_KEY, "Hunter.io", language=language):
        return

    try:
        domain = email.split('@')[1]
        url = f"https://api.hunter.io/v2/domain-search"
        params = {"domain": domain, "api_key": HUNTER_API_KEY}
        data = make_request("GET", url, params=params, language=language)


        if data and isinstance(data, dict):
            if SHOW_JSON:
                print(json.dumps(data, indent=2, ensure_ascii=False))
            emails = data.get("data", {}).get("emails", [])
            if emails:
                print(colored(info_details[language]["emails_found"].format(domain=domain), "green"))
                for email_info in emails:
                    print(f"    - {email_info['value']}")
            else:
                log_warning_yellow(status_messages[language]["no_results"])
        else:
            log_warning_yellow(error_details[language]["empty_response"])
    except json.JSONDecodeError as e:
        log_error_red(error_details[language]["json_error"].format(e=e))
        return
    except KeyError as e:
        log_error_red(error_details[language]["key_error"].format(e=e))
        return
    except Exception as e:
        log_error_red(error_details[language]["error"].format(e=e))
        return