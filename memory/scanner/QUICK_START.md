# Quick Start Guide - Run the Tools

## Step 1: Install the Tools

Run the installation script (requires sudo):

```bash
cd /home/sankofaconnectsolutions/memory/scanner
sudo bash quick_install.sh
```

Or install manually:

```bash
sudo apt update && sudo apt install -y nmap wireshark tcpdump nikto recon-ng
```

## Step 2: Test Each Tool

### Test Nmap (Network Scanner)

Scan your own local machine:

```bash
nmap -sV localhost
```

**Expected output**: Shows open ports and services on your local machine

### Test TCPdump (Packet Capture)

Capture 10 packets on your loopback interface:

```bash
sudo tcpdump -i lo -c 10
```

**Expected output**: Displays 10 network packets from local traffic

### Test Nikto (Web Scanner)

If you have a local web server running:

```bash
nikto -h http://localhost
```

**Expected output**: Scans localhost for web server vulnerabilities

**Note**: If no web server is running, start one first:
```bash
# Python simple HTTP server (for testing)
python3 -m http.server 8000
# Then in another terminal:
nikto -h http://localhost:8000
```

### Test Recon-ng (OSINT Framework)

Start the framework:

```bash
recon-ng
```

Once inside Recon-ng:
```bash
modules search
exit
```

**Expected output**: Lists available OSINT modules

### Test Wireshark (Network Analyzer)

Start Wireshark GUI:

```bash
wireshark
```

**Expected output**: Opens Wireshark graphical interface

## Step 3: Practice Safely

### Safe Practice Environment

1. **Use localhost** - Test on your own machine first
2. **Use your home network** - Test systems you own
3. **Virtual machines** - Set up isolated test environments
4. **Authorized practice platforms** - TryHackMe, HackTheBox

### Example Practice Session

```bash
# 1. Scan your own machine
nmap -sV localhost

# 2. Capture some local traffic
sudo tcpdump -i lo -c 20

# 3. Start a test web server
python3 -m http.server 8000

# 4. In another terminal, scan it
nikto -h http://localhost:8000

# 5. Explore OSINT framework
recon-ng
```

## Common Commands Summary

| Tool | Command | Purpose |
|------|---------|---------|
| Nmap | `nmap -sV localhost` | Scan local ports |
| TCPdump | `sudo tcpdump -i lo -c 10` | Capture 10 packets |
| Nikto | `nikto -h http://localhost` | Scan web server |
| Recon-ng | `recon-ng` | Start OSINT framework |
| Wireshark | `wireshark` | Start GUI analyzer |

## Troubleshooting

### "Permission denied" errors
Run with sudo:
```bash
sudo tcpdump -i lo
sudo nmap -sS localhost
```

### "Command not found"
Install the tool:
```bash
sudo apt install <tool_name>
```

### Wireshark needs permissions
Add user to wireshark group:
```bash
sudo usermod -aG wireshark $USER
# Then log out and back in
```

## Next Steps

1. Read detailed guides for each tool in this directory
2. Practice on your own systems
3. Explore tool documentation online
4. Use authorized platforms for advanced practice

## Safety Reminders

✅ **DO:**
- Scan your own systems
- Get written authorization before scanning others
- Use tools for learning and defensive security
- Document your activities

❌ **DON'T:**
- Scan networks without authorization
- Use tools for illegal activities
- Intercept others' communications
- Attack systems you don't own
