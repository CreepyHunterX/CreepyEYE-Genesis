# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================


import json
from settings.make_request import make_request
from settings.config import SHOW_JSON
from settings.translations import check_messages, status_messages, info_details, error_details
from settings.helpers import log_error_red, log_warning_yellow
from settings.api.api import SHODAN_API_KEY, validate_api_key
from termcolor import colored

def shodan_scan(query, language="en"):
    if not validate_api_key(SHODAN_API_KEY, "Shodan", language=language):
        return

    print(check_messages[language]["shodan_check"].format(query=query))
    
    base_url_search = "https://api.shodan.io/shodan/host/search"
    base_url_host = "https://api.shodan.io/shodan/host/"
    
    params_search = {
        "key": SHODAN_API_KEY,
        "query": query
    }
    
    try:
        response = make_request(
        "GET",
        base_url_host + query,  
        api_key=SHODAN_API_KEY,
        key_type="Bearer", 
        language=language
        )

        if response is None:
            return
        
        results = response.json()
        
        if not results or 'matches' not in results:
            log_warning_yellow(status_messages[language]["no_results"])
            return
        
        if SHOW_JSON:
            print(json.dumps(results, indent=2, ensure_ascii=False))
            return
        
        print(colored(f"\n{status_messages[language]['results_found']} {results['total']}\n", "green"))
        
        for count, result in enumerate(results.get('matches', []), 1):
            ip = result.get('ip_str', 'N/A')
            print(f"[{count}] IP: {ip}")
            
            response_host = make_request("GET", base_url_host + ip, params={"key": SHODAN_API_KEY}, language=language)
            if response_host is None:
                log_warning_yellow(error_details[language]["empty_response"])
                continue
            
            host = response_host.json()
            
            print(colored(f"{info_details[language]['organization']}: {host.get('org', 'N/A')}", "green"))
            print(colored(f"{info_details[language]['os']}: {host.get('os', 'N/A')}", "green"))
            print(colored(f"{info_details[language]['country']}: {host.get('country_name', 'N/A')}", "green"))
            print(colored(f"{info_details[language]['provider']}: {host.get('isp', 'N/A')}", "green"))

            
            for item in host.get('data', []):
                port = item.get('port', 'N/A')
                data = item.get('data', '').strip() if item.get('data') else ''
                print(f"\n    --- Port {port} ---")
                print(data)
    
    except json.JSONDecodeError as e:
        log_error_red(error_details[language]["json_decode_error"].format(e=e))
    except Exception as e:
        log_error_red(error_details[language]["error"].format(e=e))
