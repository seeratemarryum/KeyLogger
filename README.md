# Python Keylogger (Educational / Authorized Pen-Testing Only)

> ⚠️ **Important — Read Before Using**
>
> This repository contains a **keylogger** that captures keyboard events and uploads the captured log to an FTP server. **This tool must only be used for educational purposes, authorized penetration testing, or security research on machines you own or for which you have explicit, written permission.** Unauthorized use may be illegal and could result in criminal or civil penalties.

---

## Overview

A small Python proof-of-concept that:

- Listens to keyboard events using `pynput`.
- Logs keys with timestamps to a local file `klog.txt`.
- Uploads the captured log to a remote FTP server (when the script finishes).

This project is intended as a learning example to understand:
- event capture in Python,
- structured logging with timestamps,
- basic FTP file transfer automation.

---

## Repository contents
├── keylogger.py # Main script (listener + FTP upload)
└── README.md # This file


---

## Requirements

- Python 3.8+ (tested on CPython)
- Python package: `pynput`

Install dependencies:

```bash
pip install pynput
