# TCPdump - Packet Capture Tool Guide

## What is TCPdump?

TCPdump is a powerful command-line packet analyzer that captures and displays network traffic. It's essential for:
- Network troubleshooting
- Security monitoring
- Protocol analysis
- Debugging network applications

## Installation

```bash
sudo apt install tcpdump
```

## Basic Usage

### Capture packets on a specific interface

```bash
sudo tcpdump -i eth0
```

**What it does**: Captures and displays all network traffic on the eth0 interface in real-time.

### Capture specific port traffic

```bash
sudo tcpdump -i eth0 port 80
```

**What it does**: Captures only HTTP traffic (port 80) on the eth0 interface.

## Educational Example

```bash
# Capture HTTP traffic on your local machine
sudo tcpdump -i lo port 80

# Output explanation:
# - Shows packet headers for HTTP traffic
# - Displays source/destination IP and ports
# - Shows TCP flags (SYN, ACK, etc.)
# - Useful for understanding network communication
```

## Legal Note
- ✅ Capture traffic on networks you own
- ✅ Capture traffic you have authorization to inspect
- ✅ Use for troubleshooting your own systems
- ❌ Capture traffic on networks without authorization = Illegal
- ❌ Intercept others' communications = Illegal

## Common Commands Reference

```bash
# Capture on specific interface
sudo tcpdump -i eth0

# Capture specific port
sudo tcpdump port 80

# Capture specific protocol
sudo tcpdump icmp

# Save to file
sudo tcpdump -w capture.pcap

# Read from file
sudo tcpdump -r capture.pcap

# Display in ASCII
sudo tcpdump -A

# Display verbose output
sudo tcpdump -v

# Limit number of packets
sudo tcpdump -c 100

# Filter by host
sudo tcpdump host 192.168.1.1

# Filter by source
sudo tcpdump src 192.168.1.1

# Filter by destination
sudo tcpdump dst 192.168.1.1
```

## Advanced Filters

```bash
# HTTP traffic
sudo tcpdump tcp port 80

# DNS traffic
sudo tcpdump udp port 53

# SSH traffic
sudo tcpdump port 22

# Traffic from specific IP
sudo tcpdump src 192.168.1.100

# Traffic to specific IP
sudo tcpdump dst 192.168.1.100

# Complex filter (HTTP from specific IP)
sudo tcpdump tcp port 80 and src 192.168.1.100

# Exclude traffic
sudo tcpdump not port 22
```

## What TCPdump Cannot Do
- Does not modify network traffic
- Does not inject packets
- Only captures and displays (passive)
- Cannot decrypt encrypted traffic

## Safety Tips
1. Only capture on networks you own/authorize
2. Don't capture sensitive data (passwords, private info)
3. Delete capture files after analysis
4. Use loopback interface for local testing
5. Be mindful of disk space (captures can be large)
