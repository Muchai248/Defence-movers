# Obsidian UI Guide - What You'll See

## How to See the Obsidian UI

Since Obsidian is a desktop application, you need to:

1. **Install Obsidian** (if not already installed):
   - Download from https://obsidian.md
   - Install on your system

2. **Install the Plugin**:
   ```bash
   cd ~/memory/obsidian-osint-plugin/plugin
   npm install
   npm run build
   cp -r plugin ~/.obsidian/plugins/obsidian-osint-plugin
   ```

3. **Open Obsidian** and enable the plugin:
   - Settings → Community Plugins → Enable "OSINT Tool"

## UI Layout

### Command Palette (Ctrl/Cmd + P)

When you press `Ctrl/Cmd + P`, you'll see a search bar at the top. Type "OSINT" or "Analyze" to see the commands:

```
╔══════════════════════════════════════════════════════════╗
║ Command Palette                                          ║
╠══════════════════════════════════════════════════════════╣
║ 🔍 Search commands...                                    ║
║                                                          ║
║ ✅ Run OSINT Analysis                                   ║
║ ✅ Analyze Current Note                                 ║
║ ✅ Analyze Social Media Profiles                        ║
║ ✅ Get IP Geolocation                                  ║
║ ✅ Calculate Hash                                      ║
║ ✅ Shodan Search                                       ║
║ ✅ VirusTotal URL Scan                                 ║
║ ✅ Analyze Log Entry                                   ║
║ ✅ Monitor Ports                                       ║
║ ✅ Create Incident Report                              ║
║ ✅ Start Python Backend                                ║
╚══════════════════════════════════════════════════════════╝
```

### Ribbon Icon (Left Sidebar)

You'll see a search/magnifying glass icon in the left sidebar:
```
┌─────────────────────────────────────────┐
│  📁  📝  🔍  📊  ⚙️                   │
│  Files  Search  OSINT  Graph  Settings  │
└─────────────────────────────────────────┘
```

Clicking the 🔍 icon runs "Run OSINT Analysis".

### Settings Tab

In Settings → Community Plugins → OSINT Tool, you'll see:

```
╔══════════════════════════════════════════════════════════╗
║ OSINT Plugin Settings                                    ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║ Backend Path                                            ║
║ Path to Python backend directory                        ║
║ [../backend...........................]                    ║
║                                                          ║
║ Shared Memory Path                                      ║
║ Path for local file communication                        ║
║ [../shared-memory....................]                    ║
║                                                          ║
║ Auto Process                                            ║
║ Automatically process backend responses                  ║
║ [☑] Enabled                                            ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```

## Example Note with Results

When you run commands, results are added to your note like this:

### Before:
```markdown
# Security Investigation

Contact: support@malicious-site.com
URL: https://example.com/phishing
```

### After running "Run OSINT Analysis":
```markdown
# Security Investigation

Contact: support@malicious-site.com
URL: https://example.com/phishing

## OSINT Results

{
  "entities": {
    "email": ["support@malicious-site.com"],
    "url": ["https://example.com/phishing"],
    "domain": ["malicious-site.com", "example.com"]
  },
  "osint_results": {
    "email": [
      {
        "entity": "support@malicious-site.com",
        "type": "email",
        "domain": "malicious-site.com",
        "domain_reputation": "Unknown",
        "breach_check": "Check HaveIBeenPwned"
      }
    ]
  }
}
```

### After running "Get IP Geolocation":
```markdown
## IP Geolocation

{
  "ip": "8.8.8.8",
  "country": "United States",
  "region": "Virginia",
  "city": "Ashburn",
  "lat": 39.03,
  "lon": -77.5,
  "isp": "Google LLC"
}
```

### After running "Analyze Log Entry":
```markdown
## Blue Team Analysis

{
  "log_line": "2025-01-15 Failed login from 192.168.1.1",
  "security_keywords_found": ["failed", "login"],
  "ip_addresses": ["192.168.1.1"],
  "severity": "medium"
}
```

## Notice Notifications

When commands complete, you'll see pop-up notices at the bottom:

```
┌─────────────────────────────────────────┐
│ ✓ OSINT results added to note          │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ ✓ Geolocation data added to note        │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ ✓ Social media analysis added to note   │
└─────────────────────────────────────────┘
```

## Real-World Workflow Example

### Step 1: Create Investigation Note
```
# Phishing Investigation - 2025-01-18

Email from: support@secure-update-login.com
URL: https://secure-update-login.com/login
Attached file: invoice.pdf
```

### Step 2: Run OSINT Analysis
Press `Ctrl/Cmd + P` → "Run OSINT Analysis"

**Result**: Entities extracted (email, URL, domain)

### Step 3: Check IP Geolocation
- Create `shared-memory/temp_ip.txt` with domain's IP
- Press `Ctrl/Cmd + P` → "Get IP Geolocation"

**Result**: Location data for the IP

### Step 4: Calculate File Hash
- Press `Ctrl/Cmd + P` → "Calculate Hash"

**Result**: SHA256 hash of the note content

### Step 5: Create Incident Report
- Press `Ctrl/Cmd + P` → "Create Incident Report"

**Result**: Structured incident report template

### Final Note:
```markdown
# Phishing Investigation - 2025-01-18

Email from: support@secure-update-login.com
URL: https://secure-update-login.com/login
Attached file: invoice.pdf

## OSINT Results
{...}

## IP Geolocation
{...}

## Hash Analysis
{...}

## Incident Response
{
  "incident_id": "INC-1792332175",
  "timestamp": "2026-10-18 17:02:55",
  "severity": "high",
  "type": "phishing",
  "status": "open"
}
```

## Settings Configuration

To configure the plugin paths:

1. Open Obsidian
2. Go to Settings → Community Plugins → OSINT Tool
3. Adjust paths if needed:
   - **Backend Path**: Where the Python backend is located
   - **Shared Memory Path**: Where the plugin writes request files

Default paths work if you keep the plugin structure as-is.

## Color Coding and Formatting

Obsidian will render the JSON results with syntax highlighting:

```json
{
  "key": "value",        // Strings in quotes
  "number": 123,         // Numbers in blue
  "boolean": true,       // Booleans in bold
  "array": [1, 2, 3]     // Arrays with brackets
}
```

## Keyboard Shortcuts

- `Ctrl/Cmd + P` - Open command palette
- `Ctrl/Cmd + S` - Save note
- `Ctrl/Cmd + /` - Toggle sidebar
- `Ctrl/Cmd + Shift + I` - Open developer console (for debugging)

## Status Bar

At the bottom of Obsidian, you might see:
```
Ready | Word count: 1,234 | Last edited: 2 min ago
```

When the plugin is working, you might see:
```
Ready | Processing OSINT request... | Word count: 1,234
```

## Tips for Best Experience

1. **Keep the backend running** in a separate terminal
2. **Use descriptive note titles** for investigations
3. **Organize results** with headers (##, ###)
4. **Add your own analysis** alongside automated results
5. **Use Obsidian's linking** to connect related notes
6. **Create templates** for common investigation types

## What You'll See in Practice

Here's a typical session:

1. **Open Obsidian** → See your vault
2. **Create new note** → Blank markdown editor
3. **Paste investigation data** → Text in editor
4. **Press Ctrl/Cmd + P** → Command palette opens
5. **Type "Analyze"** → Filter to analysis commands
6. **Select command** → Notice appears "Analysis queued"
7. **Wait 2-3 seconds** → Results appear in note
8. **Review results** → JSON formatted nicely
9. **Add your notes** → Document your findings
10. **Save note** → Investigation documented

## If You Don't Have Obsidian

You can still use the backend directly:

```bash
cd ~/memory/obsidian-osint-plugin/backend
source venv/bin/activate
python3
```

Then in Python:
```python
from osint_modules import GeolocationAnalyzer, BlueTeamMonitor
import json

geo = GeolocationAnalyzer()
print(json.dumps(geo.get_ip_geolocation('8.8.8.8'), indent=2))
```

This gives you the same functionality without the Obsidian UI.

## Summary

The Obsidian UI provides:
- **Command palette** for easy access to all features
- **Ribbon icon** for quick OSINT analysis
- **Settings tab** for configuration
- **Auto-insertion** of results into notes
- **Notice notifications** for status updates
- **JSON formatting** for readable results
- **Markdown integration** for documentation

All features work seamlessly within Obsidian's note-taking environment.
