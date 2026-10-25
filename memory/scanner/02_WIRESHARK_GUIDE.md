# Wireshark - Network Protocol Analyzer Guide

## Purpose
Network protocol analyzer for capturing and inspecting network packets. Used for troubleshooting, network analysis, and security monitoring.

## Installation
```bash
sudo apt update
sudo apt install wireshark
```

**Note**: During installation, you'll be asked about non-superuser capture. For educational use, you can select "No" and run with sudo.

## Basic Usage

### 1. Start Wireshark
```bash
sudo wireshark
```

### 2. Select Network Interface
- Choose the interface you want to monitor (e.g., eth0, wlan0, lo)
- Click "Start" to begin capturing packets

### 3. Filter Packets
```
# Show only HTTP traffic
http

# Show only traffic to/from specific IP
ip.addr == 192.168.1.1

# Show only TCP traffic
tcp

# Show only traffic on specific port
tcp.port == 80

# Show DNS queries
dns
```

### 4. Analyze Packets
- Click on a packet to see details
- Expand protocol layers (Ethernet, IP, TCP, HTTP)
- Right-click → "Follow TCP Stream" to see full conversation

## Educational Examples

### Example 1: Monitor Your Own Web Traffic
```bash
# Start Wireshark
sudo wireshark

# Select your network interface
# Start capture
# Visit a website in your browser
# Stop capture
# Filter: http
# Analyze the HTTP requests and responses
```

### Example 2: Capture DNS Queries
```bash
# In Wireshark filter bar, type:
dns

# You'll see DNS queries like:
# Query: A example.com
# Response: 93.184.216.34
```

### Example 3: Analyze TCP Handshake
```bash
# Filter for a specific connection
tcp.flags.syn == 1

# You'll see the 3-way handshake:
# SYN → SYN-ACK → ACK
```

## Command Line Alternative (Tshark)
```bash
# Capture packets to file
sudo tshark -i eth0 -w capture.pcap

# Read capture file
tshark -r capture.pcap

# Display HTTP traffic
tshark -r capture.pcap -Y "http"

# Display DNS traffic
tshark -r capture.pcap -Y "dns"
```

## Educational Use Cases

### 1. Understand Network Protocols
- Analyze HTTP request/response structure
- Study TCP handshake process
- Examine DNS resolution

### 2. Troubleshoot Network Issues
- Identify slow connections
- Detect packet loss
- Analyze network latency

### 3. Security Monitoring
- Detect unusual traffic patterns
- Identify potential attacks
- Monitor for suspicious activity

## Legal Note
- ✅ Monitor your own network traffic
- ✅ Analyze traffic you have authorization to inspect
- ❌ Capture traffic on networks without authorization = Illegal
- ❌ Intercept others' communications = Illegal

## Common Filters Reference
```
http                    # HTTP traffic
https                   # HTTPS traffic (encrypted, only see handshake)
dns                     # DNS queries
tcp                     # TCP traffic
udp                     # UDP traffic
ip.addr == 1.2.3.4     # Traffic to/from specific IP
tcp.port == 22         # SSH traffic
icmp                    # Ping and ICMP
```

## What Wireshark Cannot Do
- Does not modify network traffic
- Does not inject packets
- Only captures and analyzes (passive)

## Safety Tips
1. Only capture on networks you own/authorize
2. Don't capture sensitive data (passwords, private info)
3. Delete capture files after analysis
4. Use loopback interface for local testing
