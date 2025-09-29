# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================


import json, logging, requests
from settings.translations import check_messages, info_details, error_details
from settings.api.api import ABUSEIPDB_KEY, validate_api_key
from settings.config import SHOW_JSON
from settings.helpers import log_error_red, log_warning_yellow
from settings.make_request import make_request
from termcolor import colored

logger = logging.getLogger("EYE_tools.abuseipdb")

def abuseipdb(query, language="en"):
    logger.info("\n" + check_messages[language]["abuseipdb_check"].format(query=query))
    if not validate_api_key(ABUSEIPDB_KEY, "AbuseIPDB", language=language):
        return
    
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
            if SHOW_JSON:
                print(json.dumps(data, indent=2, ensure_ascii=False))
            print(colored(info_details[language]["abuse_score"], "green"), f"{data.get('abuseConfidenceScore', 'N/A')}%")
            print(colored(info_details[language]["last_report"], "green"), f"{data.get('lastReportedAt', 'N/A')}")
        else:
            log_warning_yellow(error_details[language]["empty_response"])
            return
    except json.JSONDecodeError as e:
        log_error_red(error_details[language]["json_error"].format(e=e))
        return
    except requests.exceptions.RequestException as e:
        log_error_red(f"[HTTP ERROR] {str(e)}")
        return
    except Exception as e:
        log_error_red(error_details[language]["error"].format(e=e))
        return