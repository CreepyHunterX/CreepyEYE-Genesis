# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================


import os
from settings.translations import settings_details
from settings.helpers import log_warning_yellow
from dotenv import load_dotenv

# ======= LOAD .env =======
dotenv_path = os.path.join(os.path.dirname(__file__), "api_keys.env")
load_dotenv(dotenv_path=dotenv_path)


SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")
IPINFO_TOKEN = os.getenv("IPINFO_TOKEN")
ABUSEIPDB_KEY = os.getenv("ABUSEIPDB_KEY")
HUNTER_API_KEY = os.getenv("HUNTER_API_KEY")
VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
NUMVERIFY_API_KEY = os.getenv("NUMVERIFY_API_KEY")
GREYNOISE_API_KEY = os.getenv("GREYNOISE_API_KEY")
EMAILREP_API_KEY = os.getenv("EMAILREP_API_KEY")
WHOIS_API_KEY = os.getenv("WHOIS_API_KEY")

def validate_api_key(api_key, api_name="API", language="en"):
    from settings.helpers import check_api_key  
    if not api_key or api_key.lower().startswith("your_"):
        log_warning_yellow(settings_details[language]["api_key_not_found"].format(api_name=api_name))
        return False


    if not check_api_key(api_key, api_name=api_name, language=language):
        log_warning_yellow(settings_details[language]["invalid_api_key"].format(api_name=api_name))
        return False
    return True