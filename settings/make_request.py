# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================

import requests, logging, json
from settings.proxy.tor import get_smart_session
from settings.translations import error_details
from settings.helpers import log_error_red
logger = logging.getLogger("settings.make_request")

def make_request(method, url, params=None, api_key=None, data=None, files=None, timeout=10, language="en",  key_type="Bearer"):
    session = get_smart_session(language)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    }

    if api_key:
        if key_type == "Bearer":
            headers["Authorization"] = f"Bearer {api_key}"
        elif key_type == "Key":
            headers["Key"] = api_key
        elif key_type == "x-apikey": 
            headers["x-apikey"] = api_key

    try:
        if method == "GET":
            res = session.get(url, params=params, headers=headers, timeout=timeout)
        elif method == "POST":
            res = session.post(url, data=data, files=files, headers=headers, timeout=timeout)
        else:
            raise ValueError(error_details[language]["unsupported_request_method"])

        res.raise_for_status()

        try:
            return res.json()
        except json.JSONDecodeError:
            return res.text

        
    except requests.exceptions.Timeout:
        log_error_red(error_details[language]["request_timeout"].format(url=url))
    except requests.exceptions.RequestException as e:
        log_error_red(error_details[language]["request_error"].format(url=url, e=e))
    return None

