# <img src="PNG/CreepyEYE_mini_baner.png" style="height: 100px !important;width: 300px !important;" ></a>

![License: MIT](https://img.shields.io/badge/License-MIT-purple) 
![Status: Stable](https://img.shields.io/badge/Status-Stable-green) 
![Version: 1.1](https://img.shields.io/badge/Version-1.1-darkred.svg)
![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue) 
![OS: Windows/Linux/Mac](https://img.shields.io/badge/OS-Windows%20|%20Linux%20|%20Mac-lightgrey)
![Last Commit](https://img.shields.io/github/last-commit/CreepyHunterX/CreepyEYE-Genesis.svg)
![Open Issues](https://img.shields.io/github/issues/CreepyHunterX/CreepyEYE-Genesis.svg)
&nbsp;

## ⚠️ ВАЖЛИВО!
**CreepyEYE Genesis** — це інструмент для OSINT (Open Source Intelligence), який допомагає шукати інформацію за username, email, IP, телефоном, та іншими параметрами через різні сервіси.  
**Використовуйте тільки в етичних цілях! Розробники не несуть відповідальності за ваші дії.**

---

| Windows | Linux |
|---------|-------|
| ![CE Win](./PNG/CE_Windows_ua.png) | ![CE Linux](./PNG/CE_Linux_ua.png) |




## 🛠️ Можливості

🔎 Перевірка існування псевдоніму у соцмережах:  
&nbsp;&nbsp;&nbsp;&nbsp;`GitHub`, `Twitter`, `Instagram`, `TikTok`, `Facebook`, `GitLab`, `Bitbucket`, `Reddit`, `Twitch`, `StackOverflow`, `Kaggle`, `Medium`, `SoundCloud`, `Spotify`

📧 Перевірка email:  
&nbsp;&nbsp;&nbsp;&nbsp;через `Hunter.io`, `EmailRep.io`, `SpiderFoot`  
🌐 IP/домен перевірка:  
&nbsp;&nbsp;&nbsp;&nbsp;через `IPinfo`, `Shodan`, `AbuseIPDB`, `VirusTotal`, `GreyNoise`, `Whois`, `SpiderFoot`  
📱 Телефонні номери: `Numverify`  
🧅 Підтримка Tor для анонімності  
🈯 Меню з вибором мови (`Українська` / `Англійська` / `Російська`)  
⚙️ Автоматичне встановлення залежностей

---

## Приклад скріншотів — багатомовний

| Мова | Windows | Linux |
|----------|---------|-------|
| Українська | ![CE Win UA](./PNG/CE_Windows_ua.png) | ![CE Linux UA](./PNG/CE_Linux_ua.png) |
| Російська | ![CE Win RU](./PNG/CE_Windows_ru.png) | ![CE Linux RU](./PNG/CE_Linux_ru.png) |
| Англіська  | ![CE Win](./PNG/CE_Windows.png) | ![CE Linux](./PNG/CE_Linux.png) |

---

## Встановлення

1. **Встановіть Python 3.8+**  
   [Завантажити Python](https://www.python.org/downloads/)

2. **Встановіть Git**  
   - Windows: [Завантажити Git](https://git-scm.com/downloads/win)
   - Linux: `sudo apt update && sudo apt install git`
   - MacOS: [Завантажити Git](https://git-scm.com/downloads/mac)

3. **Склонуйте репозиторій**  
   ```sh
   git clone https://github.com/CreepyHunterX/CreepyEYE-Genesis.git
   cd "CreepyEYE-Genesis"
   ```

4. **Встановіть залежності**  
   ```sh
   pip install -r requirements.txt
   ```

5. **(Опційно) Встановіть [SpiderFoot](https://github.com/smicallef/spiderfoot)**  
   Якщо ви хочете використовувати функції SpiderFoot, його потрібно встановити окремо:
   ```sh
   git clone https://github.com/smicallef/spiderfoot.git
   cd spiderfoot
   pip install -r requirements.txt
   ```
   Після встановлення поверніться у директорію CreepyEYE Genesis для запуску основної програми.

6. **Запустіть програму**  
   ```sh
   python ce_genesis.py
   ```

---

## Налаштування API ключів

Під час запуску в програмі буде опція створити або відкрити файл з API ключами (`settings/api/api_keys.env`).  
Ви можете додати або змінити ключі у цьому файлі у будь-який час.
Відкрийте цей файл та вставте свої ключі:

- SHODAN_API_KEY
- IPINFO_TOKEN
- ABUSEIPDB_KEY
- HUNTER_API_KEY
- VIRUSTOTAL_API_KEY
- NUMVERIFY_API_KEY
- GREYNOISE_API_KEY
- EMAILREP_API_KEY
- WHOIS_API_KEY

### Де отримати API ключі та для чого вони потрібні

| Сервіс        | URL для ключа                             | Призначення                                     |
|---------------|-------------------------------------------|------------------------------------------------|
| Shodan        | https://www.shodan.io/                    | Сканування IP, пристроїв, відкритих портів     |
| IPinfo        | https://ipinfo.io/                        | Геолокація IP та інформація про ASN            |
| AbuseIPDB     | https://www.abuseipdb.com/                | Перевірка, чи повідомляли про зловмисну активність IP |
| Hunter.io     | https://hunter.io/                        | Перевірка email та пошук по домену            |
| Numverify     | https://numverify.com/                     | Валідація телефонних номерів                   |
| GreyNoise     | https://greynoise.io/                 | Інформація про сканери та ботів в мережі      |
| EmailRep.io   | https://emailrep.io/                       | Перевірка репутації email адрес                |
| WhoisXML API  | https://whoisxmlapi.com/                  | Дані WHOIS та інформація про домени            |
| VirusTotal    | https://www.virustotal.com/               | Перевірка IP, доменів та файлів на шкідливе ПЗ |


---

## Використання Tor

Для підвищення анонімності рекомендується запускати Tor (наприклад, через Tor Browser або tor.exe).  
Програма автоматично визначає, чи працює Tor, і використовує його для запитів.

---

## Важливе попередження

Цей інструмент призначений лише для етичного OSINT.  
Використовуйте його відповідально та тільки в межах закону.

---

## Ліцензія

[MIT License](LICENSE)

---

## 🧠 CreepyEYE PRO — вже вийшов 🎉

**CreepyEYE PRO** — преміум-редакція CreepyEYE: десктопний OSINT-застосунок для **Windows і Linux**
з **довічною ліцензією**. 37 інтеграцій (з власними API-ключами), скани за email, username, доменом,
телефоном, IP, імʼям та EXIF фото, експорт звітів, підтримка проксі й Tor, до 3 пристроїв на ключ.

📖 **Повна інформація** — встановлення, активація, повний список сервісів і довідник CLI —
дивіться на **[github.com/CreepyHunterX/CreepyEYE-PRO](https://github.com/CreepyHunterX/CreepyEYE-PRO)**

🛒 **Придбати — [creepycore.com](https://creepycore.com/store)**

> ℹ️ CreepyEYE PRO має закритий код і є комерційним продуктом. Цей репозиторій лишається
> безкоштовною відкритою редакцією **CreepyEYE Genesis**.
---

## 💸 Підтримати CreepyEYE

Якщо вам подобається CreepyEYE і ви хочете підтримати розвиток інструменту, ви можете зробити це через:

### ☕ Ko-fi
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/F1F71KKMAH)

### 💛 Buy Me a Coffee
[<a href="https://www.buymeacoffee.com/CreepyHunterX" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>](https://buymeacoffee.com/CreepyHunterX)

Ваша підтримка допомагає нам додавати нові API, покращувати графіку та швидкодію, а також забезпечувати стабільні оновлення. 🙌


### Доступні переклади / Available translations / Доступные переводы

- 🇺🇦 Українська Версія (Цей переклад)
- 🇷🇺 [Русская Версия](./README_ru.md)
- 🇬🇧 [English Version](./README.md)

---
