# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================


import logging
from settings.proxy.tor import get_smart_session
from urllib.parse import quote
from settings.translations import check_messages, error_details, status_messages
from settings.helpers import log_error_red  
from termcolor import colored

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

SOCIALS = {
    "GitHub": lambda u: f"https://github.com/{u}",
    "Twitter": lambda u: f"https://twitter.com/{u}",
    "Instagram": lambda u: f"https://www.instagram.com/{u}",
    "TikTok": lambda u: f"https://www.tiktok.com/@{u}",
    "Facebook": lambda u: f"https://www.facebook.com/{u}",
    "GitLab": lambda u: f"https://gitlab.com/{u}",
    "Bitbucket": lambda u: f"https://bitbucket.org/{u}",
    "Reddit": lambda u: f"https://www.reddit.com/user/{u}",
    "Twitch": lambda u: f"https://www.twitch.tv/{u}",
    "StackOverflow": lambda u: f"https://stackoverflow.com/users/{u}",
    "Kaggle": lambda u: f"https://www.kaggle.com/{u}",
    "Medium": lambda u: f"https://medium.com/@{u}",
    "SoundCloud": lambda u: f"https://soundcloud.com/{u}",
    "Spotify": lambda u: f"https://open.spotify.com/user/{u}",
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; CreepyEYE Genesis)"
}

def check_connection(url, name, language="en"):
    session = get_smart_session(language)
    try:
        response = session.get(url, headers=HEADERS, timeout=10)

        if response.status_code == 404 or "not found" in response.text.lower():
            print(colored(status_messages[language]["no_results"], "yellow"), f"- {url}")
            return False

        elif "this account is private" in response.text.lower():
            print(colored(f"[!] {name}: {url} (private)", "cyan"))
            return True
        
        else:
            print(colored(f"[+] {name}: {url}", "green"))
            return True

    except Exception as e:
        log_error_red(error_details[language]["request_error"].format(e=str(e), url=url))
        return False
    
def search_by_sites_username(username, language="en"):
    print(check_messages[language]["username_search"].format(query=username))
    results = []
    for name, url_fn in SOCIALS.items():
        safe_username = quote(username.replace(" ", ""))
        raw_url = url_fn(safe_username)
        url = raw_url
        is_found = check_connection(url, name, language)
        status = "✅" if is_found else "❌"
        results.append((name, url, status))
    return results