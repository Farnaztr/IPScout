# 🕷️ IPScout

**Scan the local net. Uncover what's hiding. Stay unseen.**  
> 🔧 Minimalist Python tool for digital recon missions.

**Author:** Farnaz 
📡 **Version:** 1.0  
🧭 **Local Intel Mode:** Activated  
🧠 **Dependencies:** 0  
💻 **Requires:** Python 3.x

---

## 👁 Overview

**IPScout** is a lightweight tactical reconnaissance script for probing live devices and scanning common open ports in your local environment.

No extras. No bloated frameworks. Just raw Python, sockets, and syscalls.

Whether you’re mapping out a dev lab, checking on rogue devices, or building the foundation for a bigger toolchain—IPScout reports what matters.

---

## 🔍 Core Ops

- 🛰️ **Ping Check**  
  Checks device reachability using native `ping`  
  (Windows: `-n`, Linux/macOS: use `-c`)

- 🧠 **Hostname Resolver**  
  Attempts reverse DNS lookup for human-readable names

- 🔐 **TCP Port Scanner**  
  Scans core service ports: FTP, SSH, HTTP(S), SMTP, RDP, MySQL, DNS, and more

- ⏱️ 4-second timeout to prevent stalling on dead air

---

## 🧪 Sample Run

```shell
$ python IPScout.py
Enter the local IP Address: 192.168.0.42

Checking...

Device is +Online+
Hostname: octoprinter.local

port Status...

port 21: -Closed- - File transfer (FTP)
port 22: +Open+ - Secure remote login (SSH)
port 443: +Open+ - Secure web server (HTTPS)
