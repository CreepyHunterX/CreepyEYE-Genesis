# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================


import json, logging, requests
from settings.translations import check_messages, info_details, error_details
from settings.api.api import ABUSEIPDB_KEY, validate_api_key
from settings import config
from settings.helpers import log_error_red, log_warning_yellow, print_json, module_result
from settings.make_request import make_request
from termcolor import colored

logger = logging.getLogger("EYE_tools.abuseipdb")

def abuseipdb(query, language="en"):
    logger.info("\n" + check_messages[language]["abuseipdb_check"].format(query=query))
    if not validate_api_key(ABUSEIPDB_KEY, "AbuseIPDB", language=language):
        return module_result("abuseipdb", "error", error="missing or invalid API key")

    try:
        url = "https://api.abuseipdb.com/api/v2/check"
        querystring = {"ipAddress": query, "maxAgeInDays": "90"}
        data = make_request(
            "GET",
            url,
            params=querystring,
            api_key=ABUSEIPDB_KEY,
            key_type="Key", 
            language=language
        )
        if data and isinstance(data, dict):
            if config.SHOW_JSON:
                print_json(data)
            # Помилки AbuseIPDB не схожі на "нічого не знайдено" — це список errors.
            if data.get("errors"):
                first = data["errors"][0] if data["errors"] else {}
                log_error_red(error_details[language]["api_error"].format(e=first.get("detail", first)))
                return module_result("abuseipdb", "error", error=first.get("detail", str(first)))
            # Корисні поля загорнуті в data.
            record = data.get("data", {})
            print(colored(info_details[language]["abuse_score"], "green"), f"{record.get('abuseConfidenceScore', 'N/A')}%")
            print(colored(info_details[language]["last_report"], "green"), f"{record.get('lastReportedAt', 'N/A')}")
            return module_result("abuseipdb", "ok", data=data)
        else:
            log_warning_yellow(error_details[language]["empty_response"])
            return module_result("abuseipdb", "empty")
    except json.JSONDecodeError as e:
        log_error_red(error_details[language]["json_error"].format(e=e))
        return module_result("abuseipdb", "error", error=str(e))
    except requests.exceptions.RequestException as e:
        log_error_red(f"[HTTP ERROR] {str(e)}")
        return module_result("abuseipdb", "error", error=str(e))
    except Exception as e:
        log_error_red(error_details[language]["error"].format(e=e))
        return module_result("abuseipdb", "error", error=str(e))