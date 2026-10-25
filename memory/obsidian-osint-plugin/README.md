# Obsidian OSINT Plugin

A hybrid Obsidian plugin with Python backend for OSINT (Open Source Intelligence) operations, data analysis, and machine learning.

## Architecture

- **Plugin**: TypeScript-based Obsidian plugin that integrates with Obsidian UI
- **Backend**: Python service for OSINT operations, ML analysis, and data processing
- **Communication**: Local file-based communication via `shared-memory/` directory

## Features

### OSINT Analysis
- Entity extraction (IPs, emails, domains, URLs, phone numbers, crypto addresses)
- WHOIS domain lookups
- DNS record analysis
- SSL certificate information
- Email breach checking (HaveIBeenPwned)
- URL reputation checking

### Network Reconnaissance (Authorized Testing Only)
- Ping and traceroute
- DNS record lookups
- Port scanning (with authorization)
- Network mapping

### Vulnerability Scanning (Authorized Targets Only)
- CVE scanning against public databases
- HTTP security header analysis
- SSL/TLS configuration analysis
- Web application security assessment

### Threat Intelligence
- IP reputation checking (AbuseIPDB, VirusTotal, Spamhaus)
- Domain reputation checking
- Malware hash analysis
- Threat feed integration

### Machine Learning Analysis
- Sentiment analysis
- Topic extraction
- Language detection
- Text classification
- Pattern recognition

### Data Processing
- Text statistics and analysis
- Keyword extraction
- Entity recognition
- Data normalization

## Installation

### Prerequisites

- Node.js v18+
- Python 3.8+
- Obsidian
- Git

### Quick Start

1. Install Python backend dependencies:
   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Install plugin dependencies:
   ```bash
   cd plugin
   npm install
   npm run build
   ```

3. Create shared memory directory:
   ```bash
   cd ..
   mkdir -p shared-memory
   ```

4. Start the Python backend:
   ```bash
   cd backend
   source venv/bin/activate
   python3 main.py
   ```

5. Copy the plugin to your Obsidian vault:
   ```bash
   cp -r plugin ~/.obsidian/plugins/obsidian-osint-plugin
   ```

6. Enable the plugin in Obsidian Settings → Community Plugins

## Documentation

- **[USAGE.md](USAGE.md)** - Detailed usage guide, configuration, and troubleshooting
- **[SECURITY.md](SECURITY.md)** - Legal guidelines, ethical use, and security best practices

## Security & Legal Notice

**IMPORTANT**: This tool is designed for legitimate security research, authorized testing, and defensive security purposes only.

- **Network reconnaissance and vulnerability scanning require explicit authorization**
- Never use against systems you do not own or have permission to test
- Unauthorized use may violate computer crime laws
- See [SECURITY.md](SECURITY.md) for detailed legal guidelines

### Legitimate Use Cases

- **Blue Team**: Monitoring and defending your own systems
- **Red Team**: Authorized penetration testing with written permission
- **OSINT Research**: Gathering publicly available information
- **Security Education**: Learning in controlled lab environments

## Usage

1. Open Obsidian
2. The plugin will be available in the command palette (Ctrl/Cmd + P)
3. Use commands to run OSINT operations
4. Results appear in your notes

### Available Commands

- **Run OSINT Analysis**: Extract entities and perform OSINT lookups
- **Analyze Current Note**: Text analysis and ML insights
- **Start Python Backend**: Signal backend to start

## Configuration

### Plugin Settings

Access in Obsidian: Settings → Community Plugins → OSINT Tool

- **Backend Path**: Path to Python backend directory
- **Shared Memory Path**: Path for file communication
- **Auto Process**: Automatically process backend responses

### API Keys

Create `.env` file in backend directory:

```env
SHODAN_API_KEY=your_key_here
VIRUSTOTAL_API_KEY=your_key_here
HIBP_API_KEY=your_key_here
```

See [USAGE.md](USAGE.md) for detailed setup instructions.

## Project Structure

```
obsidian-osint-plugin/
├── backend/              # Python backend
│   ├── main.py          # Main backend server
│   ├── osint_modules.py # OSINT analysis modules
│   ├── requirements.txt # Python dependencies
│   └── .env.example     # Environment variables template
├── plugin/              # Obsidian plugin
│   ├── main.ts         # Plugin source
│   ├── manifest.json   # Plugin manifest
│   └── package.json    # Node dependencies
├── shared-memory/      # Communication directory
├── USAGE.md            # Usage guide
├── SECURITY.md         # Security and legal guidelines
└── README.md           # This file
```

## Contributing

Contributions are welcome for:
- Additional OSINT modules
- Enhanced ML capabilities
- Bug fixes and improvements
- Documentation improvements

Please ensure all contributions:
- Follow legal and ethical guidelines
- Include appropriate documentation
- Are tested for security issues

## License

MIT License - See LICENSE file for details

## Disclaimer

This tool is provided for educational and legitimate security purposes only. Users are responsible for ensuring their use complies with all applicable laws and regulations. The authors are not responsible for misuse of this software.

## Support

For detailed usage instructions, see [USAGE.md](USAGE.md)
For legal guidelines, see [SECURITY.md](SECURITY.md)

