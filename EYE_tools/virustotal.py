# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================


import json, logging
from settings.translations import status_messages, info_details, error_details, check_messages
from settings.api.api import VIRUSTOTAL_API_KEY, validate_api_key
from settings.config import SHOW_JSON
from settings.helpers import log_error_red, log_warning_yellow
from settings.make_request import make_request
from termcolor import colored

logger = logging.getLogger("EYE_tools.virustotal")

def virustotal(ip, language="en"):
    logger.info("\n" + check_messages[language]["virustotal_check"].format(query=ip))
    if not validate_api_key(VIRUSTOTAL_API_KEY, "VirusTotal", language=language):
        return
    try:
        url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
        data = make_request("GET", url, api_key=VIRUSTOTAL_API_KEY, language=language)

        if data and isinstance(data, dict):
            if SHOW_JSON:
                print(json.dumps(data, indent=2, ensure_ascii=False))

            stats = data.get("data", {}).get("attributes", {}).get("last_analysis_stats")
            if stats:
                print(colored(info_details[language]["detections"], "green"))
                for key, value in stats.items():
                    print(f"  {key}: {value}")
            else:
                log_warning_yellow(status_messages[language]["no_results"])
        else:
            log_warning_yellow(error_details[language]["empty_response"])
    except json.JSONDecodeError as e:
        log_error_red(error_details[language]["json_decode_error"].format(e=e))
    except Exception as e:
        log_error_red(error_details[language]["error"].format(e=e))