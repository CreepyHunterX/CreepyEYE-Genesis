# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================

import json, logging
from settings.translations import status_messages, info_details, error_details, check_messages, warnings
from settings.api.api import WHOIS_API_KEY, validate_api_key
from settings import config
from settings.helpers import log_error_red, log_warning_yellow, print_json, module_result
from settings.make_request import make_request
from termcolor import colored

logger = logging.getLogger("EYE_tools.whois")

# Пробний запит до example.com витрачає квоту на кожен скан. Тип доступу
# (повний/lite) не змінюється в межах запуску, тож кешуємо його.
_full_access_cache = None


def check_whois_access(api_key, language="en"):
    global _full_access_cache
    if _full_access_cache is not None:
        return _full_access_cache

    url = "https://www.whoisxmlapi.com/whoisserver/WhoisService"
    params = {"apiKey": api_key, "domainName": "example.com", "outputFormat": "JSON"}

    try:
        data = make_request("GET", url, params=params, language=language)
        if data and isinstance(data, dict):
            error_code = data.get("ErrorMessage", {}).get("errorCode")
            if error_code == "API_KEY_05":
                _full_access_cache = False
                return False
            if data.get("WhoisRecord"):
                _full_access_cache = True
                return True
        logger.warning(warnings[language]["check_failed_fallback"])
        _full_access_cache = False
        return False
    except Exception as e:
        # Транзієнтну помилку не кешуємо — дамо шанс перепробувати наступного разу.
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
        return module_result("whois", "error", error="missing or invalid API key")

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
            if config.SHOW_JSON:
                print_json(data)
            parse_whois_record(data, language=language)
            status = "ok" if data.get("WhoisRecord") else "empty"
            return module_result("whois", status, data=data)
        else:
            log_warning_yellow(error_details[language]["empty_response"])
            return module_result("whois", "empty")

    except json.JSONDecodeError as e:
        log_error_red(error_details[language]["json_decode_error"].format(e=e))
        return module_result("whois", "error", error=str(e))
    except Exception as e:
        log_error_red(error_details[language]["error"].format(e=e))
        return module_result("whois", "error", error=str(e))
