# 🛠️ Educational Keylogger (Red Team Simulation Project)

## 🧠 Overview

This is a simple but functional Python-based keylogger designed for **educational purposes**, **red team simulation**, and **ethical hacking labs**. It demonstrates core concepts of input capture (MITRE ATT&CK T1056.001) and stealth execution on Windows systems.

> ⚠️ **DISCLAIMER**  
> This project is for educational use only. Do not deploy or execute this code on systems you do not own or have explicit permission to test. Unauthorized use may be illegal.

---

## 📦 Features

- Captures all printable characters and special keys (Enter, Space, Tab, etc.)
- Logs output to a text file (`log.txt`)
- Runs silently when converted to `.exe`
- Optionally simulates persistence via registry (Windows)
- Works in controlled red team labs and sandbox environments

---

## 🧰 Prerequisites

- Python 3.6 or higher
- Git
- Windows or Linux (demo designed for Windows lab use)

---

## 🚀 Getting Started

Clone the repository, set up the environment, and run the keylogger:

```bash
# 1. Clone the repository
git clone https://github.com/PrAjWa-L/Educational-Keylogger-Script.git
cd Educational-Keylogger-Script

# 2. (Optional) Create and activate a virtual environment
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Linux/macOS:
source venv/bin/activate

# 3. Install dependencies
pip install pynput

# 4. Run the keylogger
python keylogger.py
```
The script logs all keystrokes into (`log.txt`) in the current directory.
Stop it anytime with (`Ctrl + C`).

## 💣 Convert to Executable (Windows Payload Simulation)

Package the script as a stealth executable for red team testing:

```bash
# 1. Install PyInstaller
pip install pyinstaller

# 2. Build the executable (stealth mode)
pyinstaller --noconsole --onefile keylogger.py
```
The executable will be created in the (`dist/`) directory as (`keylogger.exe.`)
This (`.exe`) runs silently in the background.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.





