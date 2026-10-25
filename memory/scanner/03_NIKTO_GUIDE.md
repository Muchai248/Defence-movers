# Nikto - Web Server Scanner Guide

## What is Nikto?

Nikto is a web server scanner that performs comprehensive tests against web servers to identify:
- Potentially dangerous files/programs
- Outdated server versions
- Known security vulnerabilities
- Misconfigurations

## Installation

```bash
sudo apt install nikto
```

## Basic Usage

### Scan your own web server (localhost)

```bash
nikto -h http://localhost
```

**What it does**: Scans the web server running on your local machine and reports potential security issues.

### Scan a specific port

```bash
nikto -h http://localhost:8080
```

## Educational Example

```bash
# Scan your local web server
nikto -h http://localhost

# Output explanation:
# - Server: Apache/2.4.52
# - + OSVDB-3268: /admin/ - Directory listing found
# - + Server banner: Apache/2.4.52 (Ubuntu)
```

## Legal Note
- ✅ Scan your own web servers
- ✅ Scan web servers with written authorization
- ❌ Scan web servers without authorization = Illegal

## Common Commands Reference

```bash
# Basic scan
nikto -h <target>

# Scan with SSL
nikto -h https://<target>

# Scan specific port
nikto -h <target> -p 8080

# Use a specific plugin
nikto -h <target> -plugins testing

# Output to file
nikto -h <target> -output scan_report.txt
```

## What Nikto Cannot Do
- Does not exploit vulnerabilities
- Does not attack web applications
- Only identifies potential issues for review

## Safety Tips
1. Only scan your own web servers
2. Get written authorization before scanning others
3. Review findings with the server owner
4. Use findings to improve security posture
