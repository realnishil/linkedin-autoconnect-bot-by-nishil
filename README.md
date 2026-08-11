# 👾 LinkedIn AutoConnect Bot

<div align="center">

```text
██╗     ██╗███╗   ██╗██╗  ██╗███████╗██████╗ ██╗███╗   ██╗
██║     ██║████╗  ██║██║ ██╔╝██╔════╝██╔══██╗██║████╗  ██║
██║     ██║██╔██╗ ██║█████╔╝ █████╗  ██║  ██║██║██╔██╗ ██║
██║     ██║██║╚██╗██║██╔═██╗ ██╔══╝  ██║  ██║██║██║╚██╗██║
███████╗██║██║ ╚████║██║  ██╗███████╗██████╔╝██║██║ ╚████║
╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝╚═╝  ╚═══╝
```

### ⚡ Automated LinkedIn Networking Using Selenium

![Profile Views](https://komarev.com/ghpvc/?username=realnishil\&color=00ff00\&style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-00ff00?style=for-the-badge)
![Selenium](https://img.shields.io/badge/Selenium-Automation-00ff00?style=for-the-badge)
![Chrome](https://img.shields.io/badge/Chrome-Supported-00ff00?style=for-the-badge)
![Maintained](https://img.shields.io/badge/Maintained-Yes-00ff00?style=for-the-badge)

### 🚀 Developed by @realnishil

```text
root@realnishil:~# ./linkedin-autoconnect-bot
[ ACCESS GRANTED ]
```

</div>

---

# 🎯 Overview

LinkedIn AutoConnect Bot is a Python-based automation project that uses Selenium WebDriver to automatically navigate LinkedIn's suggested connections section and send connection requests.

This project demonstrates:

* 🤖 Browser Automation
* 🌐 Dynamic Web Navigation
* 🔍 Element Detection
* ⚡ Selenium WebDriver Usage
* 🛠 Automation Workflow Design

The script opens LinkedIn, allows manual authentication, collects suggested connections, and attempts to send connection requests automatically.

---

# ⚠️ Disclaimer

> This project is created strictly for educational and learning purposes.

LinkedIn may change its interface, selectors, security mechanisms, or Terms of Service at any time.

Users are solely responsible for how they use this project.

---

# 🔥 Features

## 🔐 Manual Authentication

* Opens LinkedIn login page
* User logs in manually
* Avoids storing credentials in code

## 🌐 Automatic Navigation

Automatically navigates to:

```text
LinkedIn → My Network → Suggested Connections
```

## 📜 Dynamic Scrolling

Loads additional connection suggestions by scrolling the page.

## 👤 Profile Collection

Identifies and collects suggested profiles dynamically.

## 📨 Auto Connection Requests

Attempts to locate and click the Connect button automatically.

## 🎭 Human-Like Delays

Uses randomized waiting times to mimic natural user activity.

---

# 🛠 Tech Stack

```yaml
Language:
  - Python

Automation:
  - Selenium WebDriver

Browser:
  - Google Chrome

Driver Management:
  - webdriver-manager

Built-in Modules:
  - time
  - random
```

---

# 📂 Project Structure

```text
linkedin-autoconnect-bot-by-nishil/
│
├── main.py
├── README.md
│
└── requirements.txt
```

---

# ⚡ Installation

## Clone Repository

```bash
git clone https://github.com/realnishil/linkedin-autoconnect-bot-by-nishil.git

cd linkedin-autoconnect-bot-by-nishil
```

---

# 📦 Prerequisites

## Python

```bash
Python 3.8+
```

## Install Dependencies

```bash
pip install selenium webdriver-manager
```

### Note

The following modules are included with Python and do not require installation:

```python
import time
import random
```

---

# 🚀 Usage

Run the script:

```bash
python main.py
```

---

# ⚙️ Workflow

```text
┌─────────────────────┐
│ Launch Chrome       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Open LinkedIn       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Manual Login        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Open Suggestions    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Collect Profiles    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Send Requests       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Process Complete    │
└─────────────────────┘
```

---

# 🧠 Core Functions

## login_and_setup()

Responsible for:

* Opening LinkedIn
* Waiting for manual authentication
* Initial browser setup

```python
login_and_setup()
```

---

## get_suggested_connections()

Responsible for:

* Opening LinkedIn Suggestions page
* Loading more profiles
* Collecting profile elements

```python
get_suggested_connections()
```

---

## send_connection_request(profile)

Responsible for:

* Opening profile
* Finding Connect button
* Sending request
* Applying random delay

```python
send_connection_request(profile)
```

---

# 💻 Example Output

```text
Opening LinkedIn...
Please log in manually.

Logged in.
Navigating to Suggestions...

Found suggestion: John Doe
Found suggestion: Jane Smith
Found suggestion: Alex Johnson

✅ Connection request sent!
✅ Connection request sent!
✅ Connection request sent!

Process Completed.
```

---

# 🕶 Terminal View

```text
root@realnishil:~/linkedin-autoconnect-bot#

[+] Launching Browser...
[+] Opening LinkedIn...
[+] Waiting For Authentication...

[+] Authentication Successful

[+] Loading Suggested Connections...
[+] Collecting Profiles...

[+] Found: John Doe
[+] Found: Jane Smith
[+] Found: Alex Johnson

[✓] Connection Request Sent
[✓] Connection Request Sent
[✓] Connection Request Sent

[+] Task Finished Successfully
```

---

# 🚧 Future Improvements

* [ ] Headless Mode Support
* [ ] Better Profile Detection
* [ ] Connection Notes Support
* [ ] CSV Export Functionality
* [ ] Logging System
* [ ] User Filters
* [ ] Advanced Error Handling
* [ ] Dashboard Interface
* [ ] Multi-Account Support

---

# 🔒 Security Notes

This project:

✅ Does not store LinkedIn credentials

✅ Uses manual login

✅ Uses browser automation only

✅ Uses randomized delays

❌ Does not bypass authentication

❌ Does not exploit LinkedIn systems

---

# 👨‍💻 Author

## Nishil Bhimani

```text
Student | Learner | Tech Enthusiast
Cybersecurity | OSINT | Pentesting
Reverse Engineering | Forensics

GEU'28 | CSE Undergraduate
```

### Connect

GitHub: https://github.com/realnishil

Repository: https://github.com/realnishil/linkedin-autoconnect-bot-by-nishil

---

<div align="center">

## ⚡ "Automate the repetitive. Learn the powerful."

```text
root@realnishil:~#

sudo python3 main.py

[ ACCESS GRANTED ]
[ NETWORKING AUTOMATED ]
[ SESSION ACTIVE ]
```

⭐ Star the repository if you found this project useful.

Made with ❤️ and Python by Nishil Bhimani

</div>
