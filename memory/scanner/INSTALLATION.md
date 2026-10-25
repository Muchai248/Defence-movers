# Installation Instructions for Security Scanner Tools

## Quick Installation

Run this command to install all legitimate security tools:

```bash
sudo apt update && sudo apt install -y nmap wireshark tcpdump nikto recon-ng
```

## Individual Tool Installation

### 1. Nmap (Network Mapper)
```bash
sudo apt install nmap
```

### 2. Wireshark (Network Protocol Analyzer)
```bash
sudo apt install wireshark
```

### 3. TCPdump (Packet Capture)
```bash
sudo apt install tcpdump
```

### 4. Nikto (Web Server Scanner)
```bash
sudo apt install nikto
```

### 5. Recon-ng (OSINT Framework)
```bash
sudo apt install recon-ng
```

## Verification

After installation, verify each tool is installed:

```bash
# Check Nmap
nmap --version

# Check Wireshark
wireshark --version

# Check TCPdump
tcpdump --version

# Check Nikto
nikto -Version

# Check Recon-ng
recon-ng
# Then type: exit
```

## Post-Installation Setup

### Wireshark Non-Root Setup (Optional)

To run Wireshark without sudo (recommended):

```bash
# Add your user to the wireshark group
sudo usermod -aG wireshark $USER

# Log out and log back in for changes to take effect
```

### Recon-ng Module Updates

After installing Recon-ng, update its modules:

```bash
recon-ng
marketplace install all
exit
```

## Quick Start Examples

### Test Nmap on localhost
```bash
nmap -sV localhost
```

### Test TCPdump on loopback
```bash
sudo tcpdump -i lo -c 10
```

### Test Nikto (if you have a local web server)
```bash
nikto -h http://localhost
```

### Start Recon-ng
```bash
recon-ng
```

## Troubleshooting

### Permission Denied Errors

If you get permission errors, run with sudo:

```bash
sudo tcpdump -i eth0
sudo nmap -sS localhost
```

### Wireshark Capture Issues

If Wireshark can't capture packets:

```bash
# Add user to wireshark group (see above)
# Or run with sudo (not recommended for regular use)
sudo wireshark
```

### Nikto Not Found

If Nikto is not found after installation:

```bash
# Update package list
sudo apt update

# Install again
sudo apt install nikto
```

## Next Steps

After installation:
1. Read the individual tool guides in this directory
2. Start with safe localhost tests
3. Practice on your own systems
4. Explore the tool documentation online
