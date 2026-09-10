# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================


from settings import config
from settings.make_request import make_request
from settings.translations import check_messages, status_messages, info_details, error_details
from settings.helpers import log_error_red, log_warning_yellow, print_json, module_result
from settings.api.api import SHODAN_API_KEY, validate_api_key
from termcolor import colored

def shodan_scan(query, language="en"):
    if not validate_api_key(SHODAN_API_KEY, "Shodan", language=language):
        return module_result("shodan", "error", error="missing or invalid API key")

    print(check_messages[language]["shodan_check"].format(query=query))

    # /shodan/host/{ip} повертає один хост і чекає ключ у query (?key=),
    # а не Bearer-заголовок. Ключ matches існує лише у /host/search.
    base_url_host = "https://api.shodan.io/shodan/host/"

    try:
        host = make_request(
            "GET",
            base_url_host + query,
            params={"key": SHODAN_API_KEY},
            language=language,
        )

        if not host or not isinstance(host, dict):
            log_warning_yellow(status_messages[language]["no_results"])
            return module_result("shodan", "empty")

        if config.SHOW_JSON:
            print_json(host)

        if host.get("error"):
            log_warning_yellow(host["error"])
            return module_result("shodan", "empty", error=host["error"])

        print(colored(f"{info_details[language]['organization']}: {host.get('org', 'N/A')}", "green"))
        print(colored(f"{info_details[language]['os']}: {host.get('os', 'N/A')}", "green"))
        print(colored(f"{info_details[language]['country']}: {host.get('country_name', 'N/A')}", "green"))
        print(colored(f"{info_details[language]['provider']}: {host.get('isp', 'N/A')}", "green"))

        ports = host.get("ports", [])
        if ports:
            print(colored(f"Ports: {', '.join(str(p) for p in ports)}", "green"))

        for item in host.get("data", []):
            port = item.get("port", "N/A")
            banner = (item.get("data") or "").strip()
            print(f"\n    --- Port {port} ---")
            if banner:
                print(banner)

        return module_result("shodan", "ok", data=host)

    except Exception as e:
        log_error_red(error_details[language]["error"].format(e=e))
        return module_result("shodan", "error", error=str(e))
