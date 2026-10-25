#!/usr/bin/env python3
"""
Test script for Brain UI modules
"""

import sys
import json
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from osint_modules import (
    GeolocationAnalyzer,
    HashAnalyzer,
    BlueTeamMonitor,
    SocialMediaAnalyzer,
    LogAnalyzer,
    IncidentResponse
)

print("=" * 60)
print("Testing Brain UI Modules")
print("=" * 60)

# Test 1: Geolocation
print("\n1. Testing Geolocation Analyzer...")
geo = GeolocationAnalyzer()
result = geo.get_ip_geolocation('8.8.8.8')
print(json.dumps(result, indent=2))

# Test 2: Hash Analysis
print("\n2. Testing Hash Analyzer...")
hash_analyzer = HashAnalyzer()
result = hash_analyzer.calculate_string_hash('test string', 'sha256')
print(json.dumps(result, indent=2))

# Test 3: Blue Team Monitor
print("\n3. Testing Blue Team Monitor...")
blue_team = BlueTeamMonitor()
result = blue_team.analyze_log_entry('Failed login from 192.168.1.1')
print(json.dumps(result, indent=2))

# Test 4: Social Media
print("\n4. Testing Social Media Analyzer...")
social = SocialMediaAnalyzer()
result = social.extract_profiles('Check https://twitter.com/user and https://github.com/user')
print(json.dumps(result, indent=2))

# Test 5: Log Analyzer
print("\n5. Testing Log Analyzer...")
log_analyzer = LogAnalyzer()
result = log_analyzer.parse_apache_log('192.168.1.1 - - [15/Jan/2025:10:30:00 +0000] "GET /index.html HTTP/1.1" 200 1234')
print(json.dumps(result, indent=2))

# Test 6: Incident Response
print("\n6. Testing Incident Response...")
ir = IncidentResponse()
result = ir.create_incident_report({
    'severity': 'high',
    'type': 'phishing',
    'description': 'Test incident'
})
print(json.dumps(result, indent=2))

print("\n" + "=" * 60)
print("All tests completed successfully!")
print("=" * 60)
