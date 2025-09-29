# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================

import json, logging
from settings.translations import status_messages, info_details, error_details, check_messages, warnings
from settings.api.api import WHOIS_API_KEY, validate_api_key
from settings.config import SHOW_JSON
from settings.helpers import log_error_red, log_warning_yellow
from settings.make_request import make_request
from termcolor import colored

logger = logging.getLogger("EYE_tools.whois")


def check_whois_access(api_key, language="en"):
    url = "https://www.whoisxmlapi.com/whoisserver/WhoisService"
    params = {"apiKey": api_key, "domainName": "example.com", "outputFormat": "JSON"}
    
    try:
        data = make_request("GET", url, params=params, language=language)
        if data and isinstance(data, dict):
            error_code = data.get("ErrorMessage", {}).get("errorCode")
            if error_code == "API_KEY_05":
                return False
            if data.get("WhoisRecord"):
                return True
        logger.warning(warnings[language]["check_failed_fallback"])
        return False
    except Exception as e:
        log_error_red(error_details[language]["error"].format(e=e))
        return False


def parse_whois_record(data, language="en"):
    whois_record = data.get("WhoisRecord")
    if not whois_record:
        log_warning_yellow(status_messages[language]["no_results"])
        return

    domain_name = whois_record.get('domainName', 'N/A')
    organization = whois_record.get('registrant', {}).get('organization', 'N/A')
    country = whois_record.get('registrant', {}).get('country', 'N/A')

    print(colored(info_details[language]["domain_checked"], "green"), domain_name)
    print(colored(info_details[language]["organization"], "green"), organization)
    print(colored(info_details[language]["country"], "green"), country)


def whois(domain, language="en"):
    logger.info("\n" + check_messages[language]["whois_check"].format(query=domain))

    if not validate_api_key(WHOIS_API_KEY, "WhoIs", language=language):
        return

    full_access = check_whois_access(WHOIS_API_KEY, language=language)

    urls = {
        "full": "https://www.whoisxmlapi.com/whoisserver/WhoIsService",
        "fallback": "https://www.whoisxmlapi.com/whoisserver/WhoIsService"  
    }

    params_full = {"apiKey": WHOIS_API_KEY, "domainName": domain, "outputFormat": "JSON"}
    params_fallback = {"apiKey": WHOIS_API_KEY, "domainName": domain, "outputFormat": "JSON", "mode": "lite"}

    try:
        if full_access:
            data = make_request("GET", urls["full"], params=params_full, language=language)
        else:
            logger.warning(warnings[language]["limited_whoi_active"])
            data = make_request("GET", urls["fallback"], params=params_fallback, language=language)

        if data and isinstance(data, dict):
            if SHOW_JSON:
                print(json.dumps(data, indent=2, ensure_ascii=False))
            parse_whois_record(data, language=language)
        else:
            log_warning_yellow(error_details[language]["empty_response"])

    except json.JSONDecodeError as e:
        log_error_red(error_details[language]["json_decode_error"].format(e=e))
    except Exception as e:
        log_error_red(error_details[language]["error"].format(e=e))
