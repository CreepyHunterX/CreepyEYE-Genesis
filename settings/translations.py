# ================================
# 👁️‍🗨️ CreepyEYE Genesis MODULE  👁️‍🗨️
# Author: CreepyHunterX aka ₵RɆɆ₽Ɏ X ₣RΔ₥Ɇ
# Year: 2025
# License: MIT
# ================================


check_messages = {
    "uk": {
        "abuseipdb_check": "\n[🚨] AbuseIPDB для IP: {query}",
        "emailrep_check" : "\n[🔍] EmailRep перевірка: {query}",
        "greynoise_check": "\n[🚨] GreyNoice перевірка: {query}",
        "ipinfo_check": "\n[🌐] Перевірка IP: {query}",
        "numverify_check": "\n[📞] Перевірка номера телефону: {query}",
        "hunter_check": "\n[📧] Перевірка email через Hunter.io: {query}",
        "username_search": "\n[🔍] Пошук по ніку: {query}",
        "shodan_check": "\n[🔍] Shodan перевірка: {query}",
        "virustotal_check" : "\n[🔍] VirusTotal перевірка: {query}",
        "spiderfoot_check": "\n[🕷️] SpiderFoot перевірка: {query}",
        "whois_check": "\n[🔍] Whois перевірка: {query}",
    },
    "en": {
        "abuseipdb_check": "\n[🚨] AbuseIPDB for IP: {query}",
        "emailrep_check" : "\n[🔍] EmailRep check: {query}",
        "greynoise_check": "\n[🚨] GreyNoice check: {query}",
        "ipinfo_check": "\n[🌐] Checking IP: {query}",
        "numverify_check": "\n[📞] Checking phone number: {query}",
        "hunter_check": "\n[📧] Checking email via Hunter.io: {query}",
        "username_search": "\n[🔍] Searching by username: {query}",
        "shodan_check": "\n[🔍] Shodan check: {query}",
        "virustotal_check": "[🔍] VirusTotal check: {query}",
        "spiderfoot_check": "\n[🕷️] SpiderFoot check: {query}",
        "whois_check": "\n[🔍] Whois check: {query}",
    },
    "ru": {
        "abuseipdb_check": "\n[🚨] Проверка AbuseIPDB для IP: {query}",
        "emailrep_check" : "\n[🔍] Проверка EmailRep: {query}",
        "greynoise_check": "\n[🚨] Проверка GreyNoise: {query}",
        "ipinfo_check": "\n[🌐] Проверка IP: {query}",
        "numverify_check": "\n[📞] Проверка номера телефона: {query}",
        "hunter_check": "\n[📧] Проверка email через Hunter.io: {query}",
        "username_search": "\n[🔍] Поиск по нику: {query}",
        "shodan_check": "\n[🔍] Проверка Shodan: {query}",
        "virustotal_check" : "\n[🔍] Проверка VirusTotal: {query}",
        "spiderfoot_check": "\n[🕷️] Проверка SpiderFoot: {query}",
        "whois_check": "\n[🔍] Проверка Whois: {query}",
    }
}


status_messages = {
    "uk": {
        "processing": "[~] Обробка запиту: {query}",
        "results_found": "[+] Знайдено:",
        "no_results": "[-] Нічого не знайдено.",
        "tor_status_active": "[+] Tor увімкнено — з'єднання зашифровано",
        "": ""
    },
    "en": {
        "processing": "[~] Processing query: {query}",
        "results_found": "[+] Found:",
        "no_results": "[-] No results found.",
        "tor_status_active": "[+] Tor routing enabled – connection anonymized"
    },
    "ru": {
        "processing": "[~] Обработка запроса: {query}",
        "results_found": "[+] Найдено:",
        "no_results": "[-] Ничего не найдено.",
        "tor_status_active": "[+] Tor включен — соединение зашифровано"
    }
}

error_details = {
    "uk": {
        "key_error" : "[!] Ключ {e} не знайдено у словнику",
        "api_error": "[!] Помилка API: {e}",
        "error": "[!] Сталася помилка {e}",
        "json_error": "[!] Помилка декодування JSON відповіді: {e}",
        "empty_response": "[!] Сервер повернув порожню відповідь.",
        "request_timeout": "[!] Тайм-аут при запиті до {url}",
        "request_error": "[!] Помилка при запиті до {url}: {e}",
        "found_and_status": "[!] Ресурс {name} знайдено за URL {url} — статус: {res}",
        "unsupported_request_method": "[!] Непідтримуваний метод запиту",
        "dependency_check_failed": "[!] Перевірка залежностей провалена! Будь ласка, встановіть відсутні модулі або додайте файл sf.py.",
        "env_errors": "[!] Не вдалося відкрити файл .env: {e}",
        "invalid_email": "[!] Неправильний формат email.",
        "invalid_ip": "[!] Невірна IP-адреса.",
        "invalid_domain": "[!] Невірне доменне ім’я.",
        "invalid_phone": "[!] Невірний номер телефону.",
        "invalid_username": "[!] Некоректне ім’я користувача"
        
    },
    "en": {
        "key_error" : "[!] Key {e} not found in dictionary",
        "api_error": "[!] API error: {e}",
        "error": "[!] An error occurred: {e}",
        "json_error": "[!] JSON response decoding error: {e}",
        "empty_response": "[!] Server returned empty response.",
        "request_timeout": "[!] Request to {url} timed out",
        "request_error": "[!] Error while requesting {url}: {e}",
        "found_and_status": "[!] Resource {name} found at {url} — status: {res}",
        "unsupported_request_method": "[!] Unsupported request method",
        "dependency_check_failed": "[!] Dependency check failed! Please install the missing modules or add sf.py.",
        "env_errors": "[!] Failed to open .env file: {e}",
        "invalid_email": "[!] Invalid email format.",
        "invalid_ip": "[!] Invalid IP address.",
        "invalid_domain": "[!] Invalid domain name.",
        "invalid_phone": "[!] Invalid phone number.",
        "invalid_username": "[!] Invalid username"
    },
    "ru": {
        "key_error": "[!] Ключ {e} не найден в словаре",
        "api_error": "[!] Ошибка API: {e}",
        "error": "[!] Произошла ошибка {e}",
        "json_error": "[!] Ошибка декодирования JSON ответа: {e}",
        "empty_response": "[!] Сервер вернул пустой ответ.",
        "request_timeout": "[!] Тайм-аут при запросе к {url}",
        "request_error": "[!] Ошибка при запросе к {url}: {e}",
        "found_and_status": "[!] Ресурс {name} найден по адресу {url} — статус: {res}",
        "unsupported_request_method": "[!] Неподдерживаемый метод запроса",
        "dependency_check_failed": "[!] Проверка зависимостей провалена! Установите недостающие модули или добавьте файл sf.py.",
        "env_errors": "[!] Не удалось открыть файл .env: {e}",
        "invalid_email": "[!] Неверный формат email.",
        "invalid_ip": "[!] Неверный IP-адрес.",
        "invalid_domain": "[!] Неверное имя домена.",
        "invalid_phone": "[!] Неверный номер телефона.",
        "invalid_username": "[!] Некорректное имя пользователя"
    }
}

warnings = {
    "uk": {
        "ethical_use_warning" : (
            "[!] УВАГА - цей інструмент був створений тільки для етичних цілей. \n",
            "-> Розробники не несуть відповідальності за ваші дії."
        ),
        "missing_module" : "[!] Увага - Без '{module_name}' деякі функції не працюватимуть.",
        "missing_dependency": "[!] Модуль {module} відсутній!",
        "ascii_warning": "[!] Неможливо відобразити результати з не-ASCII символами. Використовується ASCII-only режим.",
        "tor_inactive_warning": "[!] Помилка підключення Tor — використовується стандартна мережа",
        "check_failed_fallback": "[!] Неможливо перевірити доступ, fallback увімкнено",
        "limited_whoi_active": "[!] Використовуємо обмежений режим WhoisService",
        "community_api_fallback": "[!] Перехід на Community API (безкоштовна версія)"
    },
    "en": {
        "ethical_use_warning" : (
            "[!] WARNING - this tool was created for ethical purposes only. \n",
            "-> Developers are not responsible for your actions."
        ),
        "missing_module" : "[!] Warning - Without '{module_name}' some functions will not work.",
        "missing_dependency": "[!] Module {module} is missing!",
        "ascii_warning": "[!] Unable to display results with non-ASCII characters. ASCII-only mode is being used.",
        "tor_inactive_warning": "[!] Tor connection error — standard network is being used",
        "check_failed_fallback": "[!] Unable to verify access, fallback enabled",
        "limited_whoi_active": "[!] Using limited WhoisService mode",
        "community_api_fallback": "[!] Falling back to Community API (free endpoint)"
    
    },
    "ru": {
    "ethical_use_warning": (
        "[!] ВНИМАНИЕ — этот инструмент создан только для этических целей.\n",
        "-> Разработчики не несут ответственности за ваши действия."
    ),
    "missing_module": "[!] Внимание — без '{module_name}' некоторые функции работать не будут.",
    "missing_dependency": "[!] Модуль {module} отсутствует!",
    "ascii_warning": "[!] Невозможно отобразить результаты с не-ASCII символами. Используется режим только ASCII.",
    "tor_inactive_warning": "[!] Ошибка подключения Tor — используется стандартная сеть",
    "check_failed_fallback": "[!] Невозможно проверить доступ, fallback включен",
    "limited_whoi_active": "[!] Используется ограниченный режим WhoisService",
    "community_api_fallback": "[!] Переход на Community API (бесплатная версия)"
    }
}

menu_details = {
    "uk": {
        "press_any_key": "Натисніть любу клавішу для продовження...",
        "exit_message" : "Вихід із CreepyEYE. Бувай!",
        "incorrect_option": "[!] Невірна опція. Спробуйте ще раз.",
        "menu": "--- ГОЛОВНЕ МЕНЮ ---",
        "choose_option": ">>> Оберіть опцію: ",
        "input_username": "Введіть псевдонім: ",
        "input_email": "Введіть email: ",
        "input_ip": "Введіть IP: ",
        "input_domain": "Введіть домен: ",
        "input_phone": "Введіть номер телефону  (в міжнародному форматі, наприклад, +380XXXXXXXXX або +1XXXXXXXXXX): ",
        "input_telegram_username": "Введіть Telegram псевдонім (без @): ",
        "tor_enabled": "[+] Tor увімкнено!",
        "tor_ip": "[+] IP через Tor: {ip}",
        "tor_not_running": "[-] Tor не запущений. Запусти Tor (наприклад, через Tor Browser або tor.exe)"

    },
    "en": {
        "press_any_key": "Press any key to continue...",
        "exit_message": "Exiting CreepyEYE. Goodbye!",
        "incorrect_option": "[!] Incorrect option. Please try again.",
        "menu": "--- MAIN MENU ---",
        "choose_option": ">>> Choose an option: ",
        "input_username": "Enter username: ",
        "input_email": "Enter email: ",
        "input_ip": "Enter IP: ",
        "input_domain": "Enter domain: ",
        "input_phone": "Enter phone number (in international format, e.g., +380XXXXXXXXX or +1XXXXXXXXXX): ",
        "input_telegram_username": "Enter Telegram username (without @): ",
        "tor_enabled": "[+] Tor is enabled!",
        "tor_ip": "[+] IP via Tor: {ip}",  
        "tor_not_running": "[-] Tor is not running. Start Tor (e.g., via Tor Browser or tor.exe)"
    },

    "ru": {
        "press_any_key": "Нажмите любую клавишу для продолжения...",
        "exit_message": "Выход из CreepyEYE. Пока!",
        "incorrect_option": "[!] Неверная опция. Попробуйте ещё раз.",
        "menu": "--- ГЛАВНОЕ МЕНЮ ---",
        "choose_option": ">>> Выберите опцию: ",
        "input_username": "Введите псевдоним: ",
        "input_email": "Введите email: ",
        "input_ip": "Введите IP: ",
        "input_domain": "Введите домен: ",
        "input_phone": "Введите номер телефона (в международном формате, например, +380XXXXXXXXX или +1XXXXXXXXXX): ",
        "input_telegram_username": "Введите Telegram псевдоним (без @): ",
        "tor_enabled": "[+] Tor включен!",
        "tor_ip": "[+] IP через Tor: {ip}",
        "tor_not_running": "[-] Tor не запущен. Запустите Tor (например, через Tor Browser или tor.exe)"
    }
}

info_details = {
    "uk": {
        "abuse_score": "[+] Рівень зловживань:",
        "last_report": "[+] Останнє повідомлення:",
        "reputation": "[+] Репутація:",
        "suspicious": "[+] Підозрілий:",
        "blacklist": "[+] На чорному списку:",
        "leaked_passwords": "[+] Злиті паролі:",
        "activity": "[+] Активність:",
        "domain_checked": "[+] Домен перевірено:",
        "classification": "[+] Класифікація:",
        "name": "[+] Назва:",
        "emails_found": "[+] Знайдені емейли на домені {domain}:",
        "ip_info": "[+] Інформація про IP:",
        "country": "[+] Країна:",
        "location": "[+] Локація:",
        "carrier": "[+] Оператор:",
        "provider": "[+] Провайдер:",
        "organization": "[+] Організація:",
        "os": "[+] ОС:",
        "detections": "[+] Виявлення:",
    },
    "en": {
        "abuse_score": "[+] Abuse Score:",
        "last_report": "[+] Last Report:",
        "reputation": "[+] Reputation:",
        "suspicious": "[+] Suspicious:",
        "blacklist": "[+] Blacklisted:",
        "leaked_passwords": "[+] Leaked Passwords:",
        "activity": "[+] Activity:",
        "domain_checked": "[+] Domain Checked:",
        "classification": "[+] Classification:",
        "name": "[+] Name:",
        "emails_found": "[+] Emails found on domain {domain}:",
        "ip_info": "[+] IP Information:",
        "country": "[+] Country:",
        "location": "[+] Location:",
        "carrier": "[+] Carrier:",
        "provider": "[+] Provider:",
        "organization": "[+] Organization:",
        "os": "[+] OS:",
        "detections": "[+] Detections:",
    },
    "ru": {
        "abuse_score": "[+] Уровень злоупотреблений:",
        "last_report": "[+] Последнее сообщение:",
        "reputation": "[+] Репутация:",
        "suspicious": "[+] Подозрительный:",
        "blacklist": "[+] В черном списке:",
        "leaked_passwords": "[+] Слитые пароли:",
        "activity": "[+] Активность:",
        "domain_checked": "[+] Домен проверен:",
        "classification": "[+] Классификация:",
        "name": "[+] Название:",
        "emails_found": "[+] Найденные email на домене {domain}:",
        "ip_info": "[+] Информация об IP:",
        "country": "[+] Страна:",
        "location": "[+] Локация:",
        "carrier": "[+] Оператор:",
        "provider": "[+] Провайдер:",
        "organization": "[+] Организация:",
        "os": "[+] ОС:",
        "detections": "[+] Обнаружения:",
    }
}


menu = {
    "uk": [
        "Виберіть опцію:",
        "1. Пошук по псевдоніму/ім'ям 🔍",
        "2. Пошук по email 📧",
        "3. Перевірка IP 🌐",
        "4. Перевірка домену 🕵️",
        "5. Перевірка номера телефону 📱",
        "6. Налаштування API 🔧",
        "7. Запустити TOR 🔧",
        "8. Поміняти мову 🔄",
        "0. Вихід ❌"
    ],
    "en": [
        "Select an option:",
        "1. Search by username/name 🔍",
        "2. Search by email 📧",
        "3. Check IP 🌐",
        "4. Check domain 🕵️",
        "5. Check phone number 📱",
        "6. API settings 🔧",
        "7. Start TOR 🔧",
        "8. Change language 🔄",
        "0. Exit ❌"
    ],
    "ru": [
        "Выберите опцию:",
        "1. Поиск по псевдониму/имени 🔍",
        "2. Поиск по email 📧",
        "3. Проверка IP 🌐",
        "4. Проверка домена 🕵️",
        "5. Проверка номера телефона 📱",
        "6. Настройки API 🔧",
        "7. Запустить TOR 🔧",
        "8. Сменить язык 🔄",
        "0. Выход ❌"
    ]
}

settings_details = {
    "uk": {
        "module_not_found": "[!] Модуль '{module_name}' не знайдено. Встановити? (y/n): ",
        "some_modules_missing": "[!] Деякі модулі не знайдені. Бажаєте їх встановити автоматично? (y/n): ",
        "install_requirements": "Будь ласка, встановіть модулі за допомогою 'pip install -r requirements.txt', а потім повторно запустіть скрипт.",
        "invalid_option": "[!] Невірний ввід. Будь ласка, введіть 'y' або 'n'.",
        "missing_api_key": "[!] Змінна середовища '{name}' не знайдена в .env файлі!",
        "found_and_status": "[-] {name}: {url} - статус: {res}",
        "connection_error": "[-] {name}: Не вдалося підключитися до {url}",
        "env_file_created": "[+] Файл {env_path} створено!",
        "env_file_exists": "[!] Файл {env_path} вже існує.",
        "api_key_not_found": "[!] {api_name} не знайдено в api_keys.env файлі!",
        "invalid_api_key": "[!] Невірний API ключ для {api_name} !",
        "too_many_attempts": "[!] Забагато невірних спроб. Вихід.",
        "restart_required": "API ключі змінено. Натисніть Enter, щоб закрити CreepyEYE. Потім запустіть його вручну знову..."
    },
    "en": {
        "module_not_found": "[!] Module '{module_name}' not found. Install? (y/n): ",
        "some_modules_missing": "[!] Some modules are missing. Do you want to install them automatically? (y/n): ",
        "install_requirements": "Please install the modules using 'pip install -r requirements.txt' and then rerun the script.",
        "invalid_option": "[!] Invalid input. Please enter 'y' or 'n'.",
        "missing_api_key": "[!] Environment variable '{name}' not found in .env file!",
        "found_and_status": "[-] {name}: {url} - status: {res}",
        "connection_error": "[-] {name}: Failed to connect to {url}",
        "env_file_created": "[+] File {env_path} created!",
        "env_file_exists": "[!] File {env_path} already exists.",
        "api_key_not_found": "[!] {api_name} not found in api_keys.env file!",
        "invalid_api_key": "[!] Invalid API key for {api_name} !",
        "too_many_attempts": "[!] Too many invalid attempts. Exiting.",
        "restart_required": "API keys have been changed. Press Enter to close CreepyEYE. Then restart it manually..."
    },
    "ru": {
        "module_not_found": "[!] Модуль '{module_name}' не найден. Установить? (y/n): ",
        "some_modules_missing": "[!] Некоторые модули отсутствуют. Хотите установить их автоматически? (y/n): ",
        "install_requirements": "Пожалуйста, установите модули через 'pip install -r requirements.txt', затем перезапустите скрипт.",
        "invalid_option": "[!] Некорректный ввод. Введите 'y' или 'n'.",
        "missing_api_key": "[!] Переменная окружения '{name}' не найдена в .env файле!",
        "found_and_status": "[-] {name}: {url} - статус: {res}",
        "connection_error": "[-] {name}: Не удалось подключиться к {url}",
        "env_file_created": "[+] Файл {env_path} создан!",
        "env_file_exists": "[!] Файл {env_path} уже существует.",
        "api_key_not_found": "[!] {api_name} не найден в файле api_keys.env!",
        "invalid_api_key": "[!] Неверный API ключ для {api_name}!",
        "too_many_attempts": "[!] Слишком много неверных попыток. Выход.",
        "restart_required": "API ключи изменены. Нажмите Enter, чтобы закрыть CreepyEYE. Затем запустите его вручную..."
    }
}

spiderfoot_details = {
    "uk": {
        "start": "[🕷️] Запуск SpiderFoot...",
        "start_error": "[!] Помилка при запуску SpiderFoot: {e}",
        "stop": "[!] SpiderFoot зупинено",
        "stop_error": "[!] Помилка при зупинці SpiderFoot: {e}",
        "not_running": "[!] SpiderFoot неактивний",
        "already_running": "[!] SpiderFoot вже запущений",
        "timeout_error": "[!] Час вийшов при запиті до SpiderFoot",
        "status": "[~] Статус SpiderFoot: {status}",
        "request_error": "[!] Помилка при запиті до SpiderFoot: {e}",
        "error": "[!] Помилка SpiderFoot: {error}",
        "process_not_found": "[!] Процес SpiderFoot не знайдено або вже зупинено",
        "missing_sf_script": "[!] Файл sf.py не знайдено! Перевір, чи Spiderfoot встановлено правильно.",
        "sf_script_found": "[+] Знайдено sf.py",
        "spiderfoot_check": "[~] Виконується запит до Spiderfoot: {query}"
    },
    "en": {
        "start": "[🕷️] Starting SpiderFoot...",
        "start_error": "[!] Error starting SpiderFoot: {e}",
        "stop": "[!] SpiderFoot stopped",
        "stop_error": "[!] Error stopping SpiderFoot: {e}",
        "not_running": "[!] SpiderFoot is not running",
        "already_running": "[!] SpiderFoot is already running",
        "timeout_error": "[!] Timeout while making request to SpiderFoot",
        "status": "[~] SpiderFoot Status: {status}",
        "request_error": "[!] Error making request to SpiderFoot: {e}",
        "error": "[!] SpiderFoot Error: {error}",
        "process_not_found": "[!] SpiderFoot process not found or already stopped",
        "missing_sf_script": "[!] sf.py file not found! Check if Spiderfoot is installed correctly.",
        "sf_script_found": "[+] sf.py found",
        "spiderfoot_check": "[~] Making request to Spiderfoot: {query}"
    },
    "ru": {
        "start": "[🕷️] Запуск SpiderFoot для: {target}",
        "start_error": "[!] Ошибка при запуске SpiderFoot: {e}",
        "stop": "[!] SpiderFoot остановлен",
        "stop_error": "[!] Ошибка при остановке SpiderFoot: {e}",
        "not_running": "[!] SpiderFoot неактивен",
        "already_running": "[!] SpiderFoot уже запущен",
        "timeout_error": "[!] Время ожидания истекло при запросе к SpiderFoot",
        "status": "[~] Статус SpiderFoot: {status}",
        "request_error": "[!] Ошибка запроса к SpiderFoot: {e}",
        "error": "[!] Ошибка SpiderFoot: {error}",
        "process_not_found": "[!] Процесс SpiderFoot не найден или уже остановлен",
        "missing_sf_script": "[!] Файл sf.py не найден! Проверьте, правильно ли установлен SpiderFoot.",
        "sf_script_found": "[+] Файл sf.py найден",
        "spiderfoot_check": "[~] Выполняется запрос к SpiderFoot: {query}"
    }
}