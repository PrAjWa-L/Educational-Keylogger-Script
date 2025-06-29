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

## 🚀 Step-by-Step Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/educational-keylogger.git
cd educational-keylogger
