# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================

import requests, logging, json, re
from settings.proxy.tor import get_smart_session
from settings.translations import error_details
from settings.helpers import log_error_red
logger = logging.getLogger("settings.make_request")

# Деякі API (Hunter, Whois, NumVerify) очікують ключ у query-рядку. Текст
# HTTPError містить повний URL, тож без редагування ключ друкується в
# терміналі й потрапляє у скріншоти. Ховаємо значення чутливих параметрів.
_SECRET_QS = re.compile(r"(?i)([?&](?:api_?key|access_key|apikey|key|token)=)[^&\s#]+")


def _redact(text):
    return _SECRET_QS.sub(r"\1***REDACTED***", str(text)) if text is not None else text


def redact_obj(obj):
    """Рекурсивно чистить чутливі query-параметри у строкових значеннях.
    Використовується перед збереженням звіту: сирі відповіді API інколи
    містять URL із ключем, і такий файл не повинен потрапити в issues."""
    if isinstance(obj, dict):
        return {k: redact_obj(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [redact_obj(v) for v in obj]
    if isinstance(obj, str):
        return _redact(obj)
    return obj

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

        # Розрізняємо типові помилки авторизації/лімітів в одному місці, щоб
        # модулі не показували їх як "порожню відповідь".
        if res.status_code in (401, 403, 429):
            key_map = {401: "http_401", 403: "http_403", 429: "http_429"}
            log_error_red(error_details[language][key_map[res.status_code]])
            return None

        res.raise_for_status()

        try:
            return res.json()
        except json.JSONDecodeError:
            return res.text

        
    except requests.exceptions.Timeout:
        log_error_red(error_details[language]["request_timeout"].format(url=_redact(url)))
    except requests.exceptions.RequestException as e:
        log_error_red(error_details[language]["request_error"].format(url=_redact(url), e=_redact(e)))
    return None

