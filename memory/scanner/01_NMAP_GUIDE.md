# Nmap (Network Mapper) - Guide

## Purpose
Network discovery and security auditing tool. Used for legitimate network administration and authorized security testing.

## Installation
```bash
sudo apt update
sudo apt install nmap
```

## Basic Usage

### 1. Scan Your Own System (Safe)
```bash
# Scan localhost (your own machine)
nmap localhost

# Scan specific ports
nmap -p 22,80,443 localhost

# Scan with service version detection
nmap -sV localhost
```

### 2. Scan Your Home Network (With Authorization)
```bash
# Scan your home network (e.g., 192.168.1.0/24)
nmap 192.168.1.0/24

# Scan specific host
nmap 192.168.1.100
```

### 3. Common Options
```bash
-sS              # TCP SYN scan (stealth)
-sV              # Service version detection
-O               # OS detection (requires root)
-p 1-65535       # Scan all ports
-A               # Aggressive scan
-T4              # Faster timing
```

## Example: Scan Your Own Machine
```bash
nmap -sV -p 1-1000 localhost
```

**What it does**: Scans ports 1-1000 on your local machine, identifies running services and their versions.

## Educational Example
```bash
# Scan to understand open ports on your system
nmap -sV localhost

# Output explanation:
# PORT    STATE SERVICE  VERSION
# 22/tcp  open  ssh      OpenSSH 8.9p1
# 80/tcp  open  http     Apache 2.4.52
```

## Legal Note
- ✅ Scan your own systems (localhost, your home network)
- ✅ Scan systems with written authorization
- ❌ Scan networks/systems without authorization = Illegal

## Common Commands Reference
```bash
# Quick scan
nmap <target>

# Full scan with service detection
nmap -sV -A <target>

# Scan specific ports
nmap -p 22,80,443 <target>

# UDP scan
nmap -sU <target>

# Script scan (Nmap scripts)
nmap --script=vuln <target>
```

## What Nmap Cannot Do
- Does not exploit vulnerabilities
- Does not attack systems
- Only discovers and identifies services

## Safety Tips
1. Always scan your own systems first
2. Get written authorization before scanning others
3. Keep scans limited to authorized scope
4. Document your scanning activities
