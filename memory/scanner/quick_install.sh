#!/bin/bash
# Quick installation script for legitimate security scanner tools
# Run this with: sudo bash quick_install.sh

echo "=========================================="
echo "Installing Security Scanner Tools"
echo "=========================================="
echo ""

# Update package list
echo "Updating package list..."
sudo apt update

# Install all tools
echo "Installing tools..."
sudo apt install -y nmap wireshark tcpdump nikto recon-ng

echo ""
echo "=========================================="
echo "Installation Complete!"
echo "=========================================="
echo ""
echo "Verifying installations..."
echo ""

# Verify installations
echo "Nmap version:"
nmap --version | head -n 1

echo ""
echo "Wireshark version:"
wireshark --version | head -n 1

echo ""
echo "TCPdump version:"
tcpdump --version | head -n 1

echo ""
echo "Nikto version:"
nikto -Version 2>&1 | head -n 1

echo ""
echo "Recon-ng:"
echo "Run 'recon-ng' to start the framework"
echo ""

echo "=========================================="
echo "All tools installed successfully!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Read the individual tool guides in this directory"
echo "2. Start with safe localhost tests"
echo "3. See INSTALLATION.md for detailed setup instructions"
