# Obsidian OSINT Plugin - Usage Guide

## Table of Contents

1. [Installation](#installation)
2. [Setup](#setup)
3. [Starting the Backend](#starting-the-backend)
4. [Installing the Plugin](#installing-the-plugin)
5. [Using the Plugin](#using-the-plugin)
6. [Configuration](#configuration)
7. [API Key Setup](#api-key-setup)
8. [Example Workflows](#example-workflows)
9. [Troubleshooting](#troubleshooting)

## Installation

### Prerequisites

- **Obsidian**: Download from [obsidian.md](https://obsidian.md)
- **Python 3.8+**: Check with `python3 --version`
- **Node.js 18+**: Check with `node --version`
- **pip**: Python package manager (usually included with Python)
- **npm**: Node.js package manager (usually included with Node.js)

### Clone or Download

If you have this repository:

```bash
cd ~/memory/obsidian-osint-plugin
```

## Setup

### 1. Install Python Backend Dependencies

Navigate to the backend directory:

```bash
cd backend
```

**Create a virtual environment** (required on Ubuntu 24.04+):

```bash
python3 -m venv venv
source venv/bin/activate
```

Install required Python packages:

```bash
pip install -r requirements.txt
```

**Note**: The requirements.txt has been minimized for basic functionality. For additional features (ML, advanced OSINT), uncomment and install optional packages as needed.

**Note**: Some packages may require additional system dependencies. If you encounter errors, you may need to install system packages first:

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3-dev python3-pip build-essential
```

### 2. Install Plugin Dependencies

Navigate to the plugin directory:

```bash
cd ../plugin
```

Install Node.js dependencies:

```bash
npm install
```

Build the plugin:

```bash
npm run build
```

### 3. Create Shared Memory Directory

The plugin uses a local directory for communication between Obsidian and the Python backend:

```bash
cd ..
mkdir -p shared-memory
```

## Starting the Backend

The Python backend must be running for the plugin to function.

### Start the Backend Server

From the obsidian-osint-plugin directory:

```bash
cd backend
source venv/bin/activate  # Activate virtual environment
python3 main.py
```

You should see:

```
OSINT Backend started
Watching shared memory directory: ../shared-memory
Press Ctrl+C to stop
```

**Keep this terminal open** - the backend needs to stay running.

### Starting in Background (Optional)

If you want to run the backend in the background:

```bash
cd backend
nohup bash -c "source venv/bin/activate && python3 main.py" > backend.log 2>&1 &
```

To stop it later:

```bash
# Find the process
ps aux | grep main.py

# Kill the process (replace PID with actual process ID)
kill PID
```

## Installing the Plugin

### Option 1: Copy to Obsidian Plugins Directory

1. Find your Obsidian vault directory
2. Copy the built plugin:

```bash
# Replace ~/.obsidian/plugins/obsidian-osint-plugin with your actual path
cp -r plugin ~/.obsidian/plugins/obsidian-osint-plugin
```

3. Enable the plugin in Obsidian:
   - Open Obsidian
   - Go to Settings → Community Plugins
   - Enable "Community Plugins" (if not already enabled)
   - Find "OSINT Tool" in the list
   - Click "Enable"

### Option 2: Symlink (Development Mode)

For development, you can symlink instead of copying:

```bash
ln -s ~/memory/obsidian-osint-plugin/plugin ~/.obsidian/plugins/obsidian-osint-plugin
```

## Using the Plugin

### Basic Usage

1. **Open Obsidian**
2. **Create or open a note**
3. **Use commands** via:
   - Command Palette: `Ctrl/Cmd + P` → "Run OSINT Analysis"
   - Ribbon icon: Click the search icon in the left sidebar
   - Right-click on note: Select from context menu (if added)

### Available Commands

1. **Run OSINT Analysis**
   - Analyzes the current note for entities (IPs, emails, domains, URLs)
   - Performs OSINT lookups on extracted entities
   - Adds results to the note

2. **Analyze Current Note**
   - Performs text analysis and ML analysis
   - Shows word count, sentiment, topics, classification

3. **Start Python Backend**
   - Sends a signal to start the backend (if configured to start remotely)

### Example: Running OSINT Analysis

1. Create a new note in Obsidian
2. Add some text with entities:

```markdown
# Security Investigation

Target IP: 192.168.1.1
Email: test@example.com
Domain: example.com
URL: https://example.com
```

3. Run "Run OSINT Analysis" from command palette
4. Wait for the analysis to complete
5. Results will be appended to your note:

```markdown
## OSINT Results

{
  "entities": {
    "ip": ["192.168.1.1"],
    "email": ["test@example.com"],
    "domain": ["example.com"],
    "url": ["https://example.com"]
  },
  "osint_results": {
    "ip": [
      {
        "entity": "192.168.1.1",
        "type": "ip",
        "geolocation": "Unknown",
        "isp": "Unknown",
        "reputation": "neutral"
      }
    ],
    ...
  }
}
```

## Configuration

### Plugin Settings

Access plugin settings in Obsidian:

1. Settings → Community Plugins → OSINT Tool → Options

**Available Settings**:

- **Backend Path**: Path to Python backend directory (default: `../backend`)
- **Shared Memory Path**: Path for file communication (default: `../shared-memory`)
- **Auto Process**: Automatically process backend responses (default: true)

### Environment Variables (Backend)

Create a `.env` file in the backend directory:

```bash
cd backend
cp .env.example .env
nano .env
```

Add your API keys:

```env
# OSINT API Keys
SHODAN_API_KEY=your_shodan_api_key_here
VIRUSTOTAL_API_KEY=your_virustotal_api_key_here
HIBP_API_KEY=your_haveibeenpwned_api_key_here

# Optional: Proxy settings
HTTP_PROXY=http://proxy.example.com:8080
HTTPS_PROXY=http://proxy.example.com:8080
```

## API Key Setup

### Shodan API

1. Go to [Shodan](https://developer.shodan.io/)
2. Sign up for an account
3. Get your API key from the dashboard
4. Add to `.env` file:

```env
SHODAN_API_KEY=your_actual_api_key
```

### VirusTotal API

1. Go to [VirusTotal](https://www.virustotal.com/)
2. Sign up for an account
3. Get your API key from your profile
4. Add to `.env` file:

```env
VIRUSTOTAL_API_KEY=your_actual_api_key
```

### HaveIBeenPwned API

1. Go to [HaveIBeenPwned](https://haveibeenpwned.com/API/Key)
2. Purchase an API key (subscription required)
3. Add to `.env` file:

```env
HIBP_API_KEY=your_actual_api_key
```

**Note**: Many OSINT APIs have free tiers for personal/educational use. Check each service's pricing page.

## Example Workflows

### Workflow 1: Phishing Investigation

**Scenario**: You received a phishing email and want to investigate the domain.

1. **Extract information from the email**:
   - Sender email
   - Links/URLs
   - Domain names

2. **Create a note in Obsidian** with the extracted data:

```markdown
# Phishing Investigation - 2025-01-15

Sender: support@secure-login-update.com
URL: https://secure-login-update.com/login
Redirect: https://bit.ly/3xyz123
```

3. **Run OSINT Analysis** on the note

4. **Review results**:
   - Check domain reputation
   - Look up WHOIS information
   - Check SSL certificate
   - Analyze URL shortener redirect

5. **Document findings** in your note

### Workflow 2: Security Research

**Scenario**: You're researching a suspicious IP address.

1. **Create a note**:

```markdown
# IP Investigation - 203.0.113.42

Source: Security alert log
Timestamp: 2025-01-15 10:30:00
Event: Brute force attempt
```

2. **Run OSINT Analysis**

3. **Use the plugin to**:
   - Check IP reputation against threat feeds
   - Look up geolocation
   - Check if IP is on blocklists
   - Document findings

### Workflow 3: Breach Monitoring

**Scenario**: Check if your email appeared in data breaches.

1. **Create a note**:

```markdown
# Breach Check

Email: your.email@example.com
```

2. **Run OSINT Analysis**

3. **Review results** for breach information

### Workflow 4: Authorized Security Assessment

**Scenario**: You have authorization to assess a web application.

1. **Create a note**:

```markdown
# Security Assessment - example.com

Authorization: Contract #12345
Scope: example.com
Date: 2025-01-15
```

2. **Run OSINT Analysis** to gather:
   - DNS records
   - SSL certificate information
   - HTTP security headers
   - Subdomains

3. **Document findings** and recommendations

## Troubleshooting

### Backend Won't Start

**Problem**: `python3 main.py` fails with errors

**Solutions**:
1. Check Python version: `python3 --version` (must be 3.8+)
2. Install dependencies: `pip install -r requirements.txt`
3. Check for missing system packages:
   ```bash
   sudo apt install python3-dev build-essential
   ```
4. Check the error message and install missing dependencies

### Plugin Not Responding

**Problem**: Obsidian plugin doesn't respond to commands

**Solutions**:
1. Verify backend is running
2. Check shared memory path in settings
3. Check Obsidian console for errors:
   - `Ctrl/Cmd + Shift + I` → Console tab
4. Restart Obsidian
5. Check backend.log for errors

### No Results Returned

**Problem**: Analysis runs but no results appear

**Solutions**:
1. Check backend is watching the correct directory
2. Verify shared memory directory exists
3. Check file permissions on shared memory directory
4. Look for error messages in backend output

### API Keys Not Working

**Problem**: API calls fail with authentication errors

**Solutions**:
1. Verify API keys are correct
2. Check if API key has sufficient permissions
3. Verify API key hasn't expired
4. Check if you've exceeded rate limits
5. Test API key manually using curl or Postman

### Permission Errors

**Problem**: Cannot write to shared memory directory

**Solutions**:
1. Check directory permissions:
   ```bash
   ls -la shared-memory/
   ```
2. Fix permissions:
   ```bash
   chmod 755 shared-memory/
   ```
3. Ensure directory is writable by your user

### Module Import Errors

**Problem**: `ModuleNotFoundError` for Python modules

**Solutions**:
1. Install missing module:
   ```bash
   pip install module_name
   ```
2. Check you're using the correct Python environment
3. Try installing in user directory:
   ```bash
   pip install --user module_name
   ```

## Advanced Usage

### Direct Backend Testing

You can test the backend directly without Obsidian:

1. **Create a test request file** in `shared-memory/`:

```bash
cd shared-memory
cat > test_request.json << EOF
{
  "type": "osint_analysis",
  "content": "Contact us at support@example.com or visit https://example.com",
  "file": "test.md",
  "timestamp": 1234567890
}
EOF
```

2. **Wait for response** - the backend will create `test_request_response.json`

3. **Read the response**:

```bash
cat test_request_response.json
```

### Custom Request Types

You can create custom requests for specific operations:

**Network Reconnaissance**:

```json
{
  "type": "network_recon",
  "target": "example.com",
  "recon_type": "dns",
  "timestamp": 1234567890
}
```

**Vulnerability Scan**:

```json
{
  "type": "vuln_scan",
  "target": "https://example.com",
  "scan_type": "http_headers",
  "timestamp": 1234567890
}
```

**Threat Intelligence**:

```json
{
  "type": "threat_intel",
  "target": "203.0.113.42",
  "intel_type": "ip",
  "timestamp": 1234567890
}
```

## Security Best Practices

1. **Never share API keys** - keep them in `.env` file only
2. **Don't commit `.env` to git** - it's in `.gitignore`
3. **Use rate limits** - don't abuse API services
4. **Follow legal guidelines** - see SECURITY.md
5. **Get authorization** - before testing any system you don't own
6. **Document everything** - keep records of authorizations and findings

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the SECURITY.md for legal guidance
3. Check API documentation for each service you use
4. Review error messages carefully - they often indicate the problem

## Next Steps

- Configure API keys for better results
- Explore different analysis types
- Create custom workflows for your use cases
- Integrate with other Obsidian plugins
- Build custom modules for specific OSINT tasks
