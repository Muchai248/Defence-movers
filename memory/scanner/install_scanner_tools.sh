#!/bin/bash
# Install legitimate security scanner tools for educational purposes
# Only for use on systems you own or have authorization to test

echo "=========================================="
echo "Security Scanner Tools Installation"
echo "Educational Purpose Only"
echo "=========================================="

# Update package list
echo "Updating package list..."
sudo apt update

# Install Nmap (Network Mapper)
echo "Installing Nmap..."
sudo apt install -y nmap

# Install Wireshark (Network Protocol Analyzer)
echo "Installing Wireshark..."
sudo apt install -y wireshark

# Install TCPdump (Packet Capture)
echo "Installing TCPdump..."
sudo apt install -y tcpdump

# Install Nikto (Web Server Scanner)
echo "Installing Nikto..."
sudo apt install -y nikto

# Install Recon-ng (OSINT Framework)
echo "Installing Recon-ng..."
sudo apt install -y recon-ng

# Install additional tools
echo "Installing additional security tools..."
sudo apt install -y curl wget git python3-pip

echo "=========================================="
echo "Installation Complete!"
echo "=========================================="
echo ""
echo "Tools installed:"
echo "  - Nmap: Network discovery and security auditing"
echo "  - Wireshark: Network protocol analyzer"
echo "  - TCPdump: Packet capture tool"
echo "  - Nikto: Web server scanner"
echo "  - Recon-ng: OSINT reconnaissance framework"
echo ""
echo "See individual tool directories for usage instructions."
