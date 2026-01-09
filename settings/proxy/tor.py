# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================


import socket, requests
from settings.translations import status_messages

def is_tor_running(host="127.0.0.1", port=9050):
    try:
        with socket.create_connection((host, port), timeout=3):
            return True
    except Exception:
        return False


def get_tor_proxies():
    return {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }


def test_tor_identity():
    try:
        response = requests.get('https://httpbin.org/ip', proxies=get_tor_proxies(), timeout=5)
        if response.status_code == 200:
            return response.json().get("origin")
        else:
            return None
    except Exception:
        return None

def get_smart_session(language="en"):
    session = requests.Session()
    if is_tor_running():
        session.proxies.update(get_tor_proxies())
        print(status_messages[language]["tor_status_active"])
    return session
