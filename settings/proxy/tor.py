# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================


import socket, requests
from settings.translations import status_messages
from settings.config import USE_TOR_PROXY, TOR_PROXY

# Друкуємо статус Tor лише один раз за запуск, а не на кожен запит.
_tor_notice_shown = False


def is_tor_running(host="127.0.0.1", port=9050):
    try:
        with socket.create_connection((host, port), timeout=3):
            return True
    except Exception:
        return False


def get_tor_proxies():
    return {
        'http': TOR_PROXY,
        'https': TOR_PROXY,
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

def announce_tor_status(language="en"):
    """Один раз при старті чітко показуємо стан Tor. Мовчазний фолбек напряму
    для OSINT-тулзи, що обіцяє анонімність, — неприйнятний."""
    global _tor_notice_shown
    if not USE_TOR_PROXY:
        print(status_messages[language]["tor_disabled"])
    elif is_tor_running():
        print(status_messages[language]["tor_status_active"])
    else:
        print(status_messages[language]["tor_fallback_direct"])
    _tor_notice_shown = True


def get_smart_session(language="en"):
    global _tor_notice_shown
    session = requests.Session()
    if USE_TOR_PROXY and is_tor_running():
        session.proxies.update(get_tor_proxies())
    # Статус оголошується один раз при старті (announce_tor_status). Якщо його
    # чомусь не викликали — підстрахуємось і покажемо тут теж лише раз.
    if not _tor_notice_shown:
        announce_tor_status(language)
    return session
