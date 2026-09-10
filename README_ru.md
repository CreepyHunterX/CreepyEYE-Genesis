# <img src="PNG/CreepyEYE_mini_baner.png" style="height: 100px !important;width: 300px !important;" ></a>

![License: MIT](https://img.shields.io/badge/License-MIT-purple) 
![Status: Stable](https://img.shields.io/badge/Status-Stable-green) 
![Version: 1.1](https://img.shields.io/badge/Version-1.1-darkred.svg)
![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue) 
![OS: Windows/Linux/Mac](https://img.shields.io/badge/OS-Windows%20|%20Linux%20|%20Mac-lightgrey)
![Last Commit](https://img.shields.io/github/last-commit/CreepyHunterX/CreepyEYE-Genesis.svg)
![Open Issues](https://img.shields.io/github/issues/CreepyHunterX/CreepyEYE-Genesis.svg)
&nbsp;


## ⚠️ ВАЖНО!
**CreepyEYE Genesis** — это инструмент OSINT (Open Source Intelligence), который помогает искать информацию по имени пользователя, email, IP, телефону, и другим параметрам на различных сервисах.  
**Используйте только в этических целях! Разработчики не несут ответственности за ваши действия.**

⚠️ Внимание! Эта русская версия является **community-переводом**.  
Официальные языки: английский и украинский.  
Авторы CreepyEYE не несут ответственности за этот перевод.  
Используйте на свой страх и риск. CreepyEYE предназначен только для **этичного OSINT**.

---

| Windows | Linux |
|---------|-------|
| ![CE Win](./PNG/CE_Windows_ru.png) | ![CE Linux](./PNG/CE_Linux_ru.png) |




## 🛠️ Возможности

🔎 Проверка существования имени пользователя на платформах соцсетей:  
&nbsp;&nbsp;&nbsp;&nbsp;`GitHub`, `X`, `Instagram`, `TikTok`, `Facebook`, `GitLab`, `Bitbucket`, `Reddit`, `Twitch`, `Kaggle`, `Medium`, `SoundCloud`, `Spotify`

📧 Проверка email:  
&nbsp;&nbsp;&nbsp;&nbsp;через `Hunter.io`, `EmailRep.io`  
🌐 Проверка IP/доменов:  
&nbsp;&nbsp;&nbsp;&nbsp;через `IPinfo`, `Shodan`, `AbuseIPDB`, `VirusTotal`, `GreyNoise`, `Whois`  
📱 Телефоны: `Numverify`  
🧅 Поддержка Tor для анонимности  
🈯 Меню выбора языка (`Украинский` / `Английский` / `Русский`)  
⚙️ Автоматическая установка зависимостей

---

## Примеры скриншотов — многоязычный

| Язык | Windows | Linux |
|----------|---------|-------|
| Русский  | ![CE Win RU](./PNG/CE_Windows_ru.png) | ![CE Linux RU](./PNG/CE_Linux_ru.png) |
| Украинский | ![CE Win UA](./PNG/CE_Windows_ua.png) | ![CE Linux UA](./PNG/CE_Linux_ua.png) |
| Английской | ![CE Win](./PNG/CE_Windows.png) | ![CE Linux](./PNG/CE_Linux.png) |

---

## Установка

1. **Установите Python 3.8+**  
   [Скачать Python](https://www.python.org/downloads/)

2. **Установите Git**  
   - Windows: [Скачать Git](https://git-scm.com/downloads/win)  
   - Linux: `sudo apt update && sudo apt install git`  
   - MacOS: [Скачать Git](https://git-scm.com/downloads/mac)

3. **Клонируйте репозиторий**  
   ```sh
   git clone https://github.com/CreepyHunterX/CreepyEYE-Genesis.git
   cd "CreepyEYE-Genesis"
   ```

4. **Установите зависимости**

   ```sh
   pip install -r requirements.txt
   ```

5. **Запуск программы**

   ```sh
   python ce_genesis.py
   ```

---

## Настройка API ключей

При запуске программы вы сможете создать или открыть файл с API ключами (`settings/api/api_keys.env`).
Вы можете добавлять или изменять ключи в любое время.
Откройте файл и вставьте ваши ключи:

* SHODAN\_API\_KEY
* IPINFO\_TOKEN
* ABUSEIPDB\_KEY
* HUNTER\_API\_KEY
* VIRUSTOTAL\_API\_KEY
* NUMVERIFY\_API\_KEY
* GREYNOISE\_API\_KEY
* EMAILREP\_API\_KEY
* WHOIS\_API\_KEY

### Где взять API ключи и их использование

| Сервис       | Ссылка на API                                              | Назначение                                               |
| ------------ | ---------------------------------------------------------- | -------------------------------------------------------- |
| Shodan       | [https://www.shodan.io/](https://www.shodan.io/)           | Сканирование IP, устройств, открытых портов              |
| IPinfo       | [https://ipinfo.io/](https://ipinfo.io/)                   | Геолокация IP и ASN                                      |
| AbuseIPDB    | [https://www.abuseipdb.com/](https://www.abuseipdb.com/)   | Проверка, не сообщалось ли о вредоносной активности с IP |
| Hunter.io    | [https://hunter.io/](https://hunter.io/)                   | Проверка email и поиск по домену                         |
| Numverify    | [https://numverify.com/](https://numverify.com/)           | Проверка номеров телефонов                               |
| GreyNoise    | [https://greynoise.io/](https://api.greynoise.io/)     | Контекст сканеров/ботов                                  |
| EmailRep.io  | [https://emailrep.io/](https://emailrep.io/)               | Репутация email адресов                                  |
| WhoisXML API | [https://whoisxmlapi.com/](https://whoisxmlapi.com/)       | WHOIS данные и информация о доменах                      |
| VirusTotal   | [https://www.virustotal.com/](https://www.virustotal.com/) | Сканирование IP, доменов и файлов на вирусы              |

---

## Использование Tor

Для увеличения анонимности рекомендуется запускать Tor (например, через Tor Browser или tor.exe).
Программа автоматически определяет, работает ли Tor, и использует его для запросов.

---

## Важное уведомление

Инструмент предназначен только для этического OSINT.
Используйте ответственно и в рамках закона.

---

## 🧠 CreepyEYE PRO — уже вышел 🎉

**CreepyEYE PRO** — премиум-редакция CreepyEYE: десктопное OSINT-приложение для **Windows и Linux**
с **пожизненной лицензией**. 37 интеграций (со своими API-ключами), сканы по email, username, домену,
телефону, IP, имени и EXIF фото, экспорт отчётов, поддержка прокси и Tor, до 3 устройств на ключ.

📖 **Полная информация** — установка, активация, полный список сервисов и справочник CLI —
смотрите на **[github.com/CreepyHunterX/CreepyEYE-PRO](https://github.com/CreepyHunterX/CreepyEYE-PRO)**

🛒 **Купить — [creepycore.com](https://creepycore.com/store)**

> ℹ️ CreepyEYE PRO имеет закрытый код и является коммерческим продуктом. Этот репозиторий остаётся
> бесплатной открытой редакцией **CreepyEYE Genesis**.
---

## 💸 Поддержать CreepyEYE

Если вам нравится CreepyEYE и вы хотите поддержать его развитие, вы можете сделать это через:

### ☕ Ko-fi
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/F1F71KKMAH)

### 💛 Buy Me a Coffee
[<a href="https://www.buymeacoffee.com/CreepyHunterX" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>](https://buymeacoffee.com/CreepyHunterX)

Ваша поддержка помогает нам добавлять новые API, улучшать графику и производительность, а также обеспечивать стабильные обновления. 🙌


---

### Доступные переводы / Available translations / Доступні переклади 

- 🇺🇦 [Українська версія](./README_ua.md)
- 🇷🇺 Русская версия (Этот перевод)
- 🇬🇧 [Englis](./README.md)

---
