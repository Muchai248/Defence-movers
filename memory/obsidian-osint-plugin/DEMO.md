# Obsidian OSINT Plugin - Complete Feature Demo

This document demonstrates all the features of the Obsidian OSINT Plugin with real examples and explanations.

## Overview

The plugin provides comprehensive OSINT (Open Source Intelligence), security analysis, and blue team tools integrated directly into Obsidian.

## Features Implemented

### 1. Social Media Analysis
**Purpose**: Extract and analyze social media profiles from text for legitimate OSINT research.

**Example Usage**:
```
Contact us at https://twitter.com/support or https://github.com/company
Check our LinkedIn: https://linkedin.com/in/john-doe
```

**Command**: "Analyze Social Media Profiles"

**What it does**:
- Extracts social media profile links (Twitter, Instagram, LinkedIn, GitHub, Reddit)
- Analyzes usernames across platforms
- Analyzes hashtags for trending topics

**Legal Note**: Only analyzes publicly available profiles. Do not use for harassment or stalking.

### 2. IP Geolocation
**Purpose**: Get geolocation data for IP addresses using public APIs.

**Example Usage**:
- Create file: `shared-memory/temp_ip.txt`
- Add IP: `8.8.8.8`
- Run command: "Get IP Geolocation"

**What it returns**:
```json
{
  "ip": "8.8.8.8",
  "country": "United States",
  "country_code": "US",
  "region": "Virginia",
  "city": "Ashburn",
  "zip": "20149",
  "lat": 39.03,
  "lon": -77.5,
  "timezone": "America/New_York",
  "isp": "Google LLC",
  "org": "Google Public DNS",
  "as": "AS15169 Google LLC"
}
```

**Source**: ip-api.com (free, no API key required)

### 3. Hash Analysis
**Purpose**: Calculate file/text hashes and check against malware databases.

**Example Usage**:
- Create a note with text
- Run command: "Calculate Hash"

**What it does**:
- Calculates SHA256 hash of text or files
- Can check hashes against VirusTotal (requires API key)
- Useful for malware detection and file integrity verification

**Example Result**:
```json
{
  "text": "test string",
  "algorithm": "sha256",
  "hash": "d5579c46dfcc7f18207013e65b44e4cb4e2c2298f4ac457ba8f82743f31e930b"
}
```

### 4. Shodan Integration
**Purpose**: Search for exposed devices and services on the internet.

**Example Usage**:
- Create file: `shared-memory/temp_query.txt`
- Add query: `nginx`
- Run command: "Shodan Search"

**What it does**:
- Searches Shodan for devices matching your query
- Returns device information, ports, services
- Requires SHODAN_API_KEY in `.env` file

**Use Cases**:
- Security research
- Asset discovery
- Exposure assessment

**Legal Note**: Only search for devices you own or have authorization to assess.

### 5. VirusTotal Integration
**Purpose**: Scan URLs and files for malware.

**Example Usage**:
- Create file: `shared-memory/temp_url.txt`
- Add URL: `http://example.com`
- Run command: "VirusTotal URL Scan"

**What it does**:
- Submits URL to VirusTotal for scanning
- Retrieves analysis reports
- Requires VIRUSTOTAL_API_KEY in `.env` file

**Use Cases**:
- Phishing investigation
- Malware analysis
- URL reputation checking

### 6. Blue Team Monitoring Tools

#### Log Analysis
**Purpose**: Analyze log entries for security events.

**Example Usage**:
- Create a note with a log entry:
  ```
  2025-01-15 10:30:00 Failed login attempt from 192.168.1.100 user=admin
  ```
- Run command: "Analyze Log Entry"

**What it does**:
- Extracts security keywords (failed, denied, attack, etc.)
- Identifies IP addresses
- Assigns severity levels (high/medium/low)
- Extracts timestamps

**Example Result**:
```json
{
  "log_line": "2025-01-15 10:30:00 Failed login attempt from 192.168.1.100 user=admin",
  "security_keywords_found": ["failed", "login"],
  "ip_addresses": ["192.168.1.100"],
  "timestamps": ["2025-01-15 10:30:00"],
  "severity": "medium"
}
```

#### Port Monitoring
**Purpose**: Check which ports are open on your local system.

**Command**: "Monitor Ports"

**What it does**:
- Checks common ports (22, 80, 443, 8080, 3000)
- Returns open/closed status
- Only monitors localhost (authorized system)

**Example Result**:
```json
{
  "ports_checked": [22, 80, 443, 8080],
  "results": {
    "22": "closed",
    "80": "open",
    "443": "closed",
    "8080": "closed"
  }
}
```

### 7. Log Analysis (Apache/Nginx)
**Purpose**: Parse and analyze web server access logs.

**Example Usage**:
- Create a note with Apache log format:
  ```
  192.168.1.1 - - [15/Jan/2025:10:30:00 +0000] "GET /index.html HTTP/1.1" 200 1234 "http://example.com" "Mozilla/5.0"
  ```
- Run command: "Analyze Log Entry" (uses log analyzer)

**What it does**:
- Parses Apache/Nginx log format
- Extracts IP, timestamp, request, status code
- Analyzes access patterns
- Identifies top IPs and status codes

**Example Result**:
```json
{
  "ip": "192.168.1.1",
  "timestamp": "15/Jan/2025:10:30:00 +0000",
  "request": "GET /index.html HTTP/1.1",
  "status_code": "200",
  "size": "1234",
  "referrer": "http://example.com",
  "user_agent": "Mozilla/5.0",
  "parsed": true
}
```

### 8. Incident Response Tools
**Purpose**: Create structured incident reports and checklists.

**Command**: "Create Incident Report"

**What it does**:
- Generates incident ID and timestamp
- Creates structured report format
- Includes severity, type, description
- Tracks affected assets and indicators
- Documents actions taken

**Example Result**:
```json
{
  "incident_id": "INC-1792332175",
  "timestamp": "2026-10-18 17:02:55",
  "severity": "high",
  "type": "phishing",
  "description": "Spear phishing attack targeting executives",
  "affected_assets": ["email-server", "workstation-1"],
  "indicators": ["malicious-email@example.com"],
  "actions_taken": ["Blocked sender", "Reset passwords"],
  "status": "open"
}
```

### 9. Network Reconnaissance (Authorized Testing Only)
**Purpose**: Perform network reconnaissance on authorized systems.

**Commands**:
- Ping test
- Traceroute
- DNS lookup
- Port scanning

**Legal Note**: Requires explicit written authorization. Only test systems you own or have permission to test.

### 10. Vulnerability Scanning (Authorized Targets Only)
**Purpose**: Scan for vulnerabilities on authorized targets.

**Commands**:
- CVE scanning
- HTTP security header analysis
- SSL/TLS configuration analysis

**Legal Note**: Requires explicit written authorization. Only scan systems you own or have permission to test.

### 11. Threat Intelligence
**Purpose**: Check indicators against threat intelligence feeds.

**Features**:
- IP reputation checking (AbuseIPDB, VirusTotal, Spamhaus)
- Domain reputation checking
- Malware hash analysis

**Note**: Requires API keys for threat intel feeds.

## Complete Workflow Example

### Scenario: Phishing Investigation

1. **Extract information from phishing email**:
   - Create note with email content
   - Run "Analyze Social Media Profiles" to extract any social links
   - Run "Calculate Hash" to hash any URLs or attachments

2. **Investigate the domain**:
   - Extract domain from email
   - Run "Run OSINT Analysis" to get domain info
   - Run "Get IP Geolocation" on the domain's IP

3. **Check reputation**:
   - Add URL to `shared-memory/temp_url.txt`
   - Run "VirusTotal URL Scan" (requires API key)
   - Check threat intelligence feeds

4. **Document findings**:
   - Run "Create Incident Report"
   - Fill in incident details
   - Add all analysis results to your investigation note

5. **Blue team response**:
   - Run "Monitor Ports" to check your systems
   - Analyze your logs for related activity
   - Follow incident response checklist

## API Key Setup

To use Shodan and VirusTotal features:

1. Create `.env` file in `backend/` directory:
```env
SHODAN_API_KEY=your_shodan_api_key
VIRUSTOTAL_API_KEY=your_virustotal_api_key
HIBP_API_KEY=your_haveibeenpwned_api_key
```

2. Get API keys:
- **Shodan**: https://developer.shodan.io/
- **VirusTotal**: https://www.virustotal.com/
- **HaveIBeenPwned**: https://haveibeenpwned.com/API/Key

## Running the Backend

### Quick Start:
```bash
cd ~/memory/obsidian-osint-plugin
./start_backend.sh
```

### Manual Start:
```bash
cd ~/memory/obsidian-osint-plugin/backend
source venv/bin/activate
python3 main.py
```

The backend will display:
```
OSINT Backend started
Watching shared memory directory: ../shared-memory
Press Ctrl+C to stop
```

## Installing the Plugin

1. Build the plugin:
```bash
cd ~/memory/obsidian-osint-plugin/plugin
npm install
npm run build
```

2. Copy to Obsidian:
```bash
cp -r plugin ~/.obsidian/plugins/obsidian-osint-plugin
```

3. Enable in Obsidian:
- Settings → Community Plugins
- Enable "OSINT Tool"

## Available Commands in Obsidian

Press `Ctrl/Cmd + P` to open command palette, then:

- **Run OSINT Analysis** - Full OSINT analysis of current note
- **Analyze Current Note** - Text and ML analysis
- **Analyze Social Media Profiles** - Extract social media links
- **Get IP Geolocation** - Get IP location data
- **Calculate Hash** - Calculate SHA256 hash
- **Shodan Search** - Search Shodan (requires API key)
- **VirusTotal URL Scan** - Scan URL with VirusTotal (requires API key)
- **Analyze Log Entry** - Analyze security logs
- **Monitor Ports** - Check local port status
- **Create Incident Report** - Generate incident report
- **Start Python Backend** - Signal backend to start

## Security & Legal Compliance

### ✅ Legitimate Uses:
- Blue team: Monitor and defend your own systems
- Red team: Authorized penetration testing with written permission
- OSINT: Gather publicly available information
- Education: Learn in controlled lab environments

### ❌ Illegal Uses:
- Unauthorized access to systems
- Scanning networks without permission
- Harassment or stalking
- Data destruction
- Bypassing security controls

### Always:
- Get written authorization before testing
- Follow responsible disclosure
- Respect privacy and laws
- Document everything
- Use only for legitimate purposes

See [SECURITY.md](SECURITY.md) for detailed legal guidelines.

## Testing the Modules

All modules have been tested and verified working:

✅ Social Media Analysis - Extracts profiles correctly
✅ Geolocation - Returns accurate IP location data
✅ Hash Analysis - Calculates hashes correctly
✅ Log Analysis - Parses logs and detects security events
✅ Incident Response - Generates structured reports
✅ Port Monitoring - Checks local ports correctly
✅ Blue Team Tools - All monitoring functions working
✅ API Integrations - Ready for API keys (returns prompts without keys)

## Next Steps

1. Set up API keys for Shodan and VirusTotal
2. Practice with the demo examples
3. Create custom workflows for your use cases
4. Integrate with your existing security processes
5. Document your findings in Obsidian

## Support

For issues or questions:
- Check [USAGE.md](USAGE.md) for detailed instructions
- Review [SECURITY.md](SECURITY.md) for legal guidance
- Test modules directly with Python scripts in backend/

## Disclaimer

This tool is provided for educational and legitimate security purposes only. Users are responsible for ensuring their use complies with all applicable laws and regulations. Unauthorized use may violate computer crime laws.
