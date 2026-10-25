#!/usr/bin/env python3
"""
Search specific IP address with full analysis
"""

import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from osint_modules import GeolocationAnalyzer, BlueTeamMonitor, ThreatIntel

IP_ADDRESS = "185.220.101.9"

print("=" * 70)
print(f"IP SEARCH: {IP_ADDRESS}")
print("=" * 70)

# 1. Geolocation Analysis
print("\n📍 GEOLOCATION ANALYSIS")
print("-" * 70)
geo = GeolocationAnalyzer()
geo_result = geo.get_ip_geolocation(IP_ADDRESS)
print(json.dumps(geo_result, indent=2))

# 2. Threat Intelligence Check
print("\n🛡️ THREAT INTELLIGENCE")
print("-" * 70)
threat = ThreatIntel()
threat_result = threat.check_ip_reputation(IP_ADDRESS)
print(json.dumps(threat_result, indent=2))

# 3. Port Monitoring (if this were a local IP)
print("\n🔌 PORT MONITORING STATUS")
print("-" * 70)
blue_team = BlueTeamMonitor()
print("Note: Port monitoring only works for localhost (127.0.0.1)")
print("For remote IPs, use authorized port scanning tools with proper authorization")

print("\n" + "=" * 70)
print("Search completed")
print("=" * 70)
