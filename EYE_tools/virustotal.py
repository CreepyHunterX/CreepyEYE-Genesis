# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================


import json, logging, ipaddress
from settings.translations import status_messages, info_details, error_details, check_messages
from settings.api.api import VIRUSTOTAL_API_KEY, validate_api_key
from settings import config
from settings.helpers import log_error_red, log_warning_yellow, print_json, module_result
from settings.make_request import make_request
from termcolor import colored

logger = logging.getLogger("EYE_tools.virustotal")


def is_ip(target):
    try:
        ipaddress.ip_address(target)
        return True
    except ValueError:
        return False

def virustotal(target, language="en"):
    """Check VirusTotal for IP or domain."""
    logger.info("\n" + check_messages[language]["virustotal_check"].format(query=target))
    
    if not validate_api_key(VIRUSTOTAL_API_KEY, "VirusTotal", language=language):
        return module_result("virustotal", "error", error="missing or invalid API key")

    try:
        endpoint = f"ip_addresses/{target}" if is_ip(target) else f"domains/{target}"
        url = f"https://www.virustotal.com/api/v3/{endpoint}"
        data = make_request(
            "GET",
            url,
            api_key=VIRUSTOTAL_API_KEY,
            key_type="x-apikey",
            language=language
        )

        if not data or not isinstance(data, dict):
            log_warning_yellow(error_details[language]["empty_response"])
            return module_result("virustotal", "empty")

        if config.SHOW_JSON:
            print_json(data)

        stats = data.get("data", {}).get("attributes", {}).get("last_analysis_stats")
        if not stats:
            log_warning_yellow(status_messages[language]["no_results"])
            return module_result("virustotal", "empty", data=data)

        print(colored(info_details[language]["detections"], "green"))
        for key, value in stats.items():
            print(f"  {key}: {value}")

        return module_result("virustotal", "ok", data=data)

    except json.JSONDecodeError as e:
        log_error_red(error_details[language]["json_decode_error"].format(e=e))
        return module_result("virustotal", "error", error=str(e))
    except Exception as e:
        log_error_red(error_details[language]["error"].format(e=e))
        return module_result("virustotal", "error", error=str(e))

