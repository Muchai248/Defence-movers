"""
OSINT Modules for the backend
Includes OSINT analysis, data processing, ML analysis, and API collection
"""

import re
import time
import json
import hashlib
import socket
import os
from typing import Dict, List, Any, Tuple
from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup


@dataclass
class Entity:
    """Represents an extracted entity"""
    value: str
    type: str
    confidence: float


class OSINTAnalyzer:
    """OSINT analysis module"""

    def __init__(self):
        # Patterns for entity extraction
        self.patterns = {
            'ip': r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'url': r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w .-]*/?',
            'domain': r'\b(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}\b',
            'phone': r'\b\+?[\d\s-]{10,}\b',
            'hashtag': r'#[A-Za-z0-9_]+',
            'username': r'@[A-Za-z0-9_]+',
            'crypto': r'\b(?:0x)?[a-fA-F0-9]{40,}\b'
        }

    def extract_entities(self, text: str) -> Dict[str, List[str]]:
        """Extract entities from text"""
        entities = {}

        for entity_type, pattern in self.patterns.items():
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                entities[entity_type] = list(set(matches))  # Remove duplicates

        return entities

    def analyze_entity(self, entity: str, entity_type: str) -> Dict[str, Any]:
        """Perform OSINT analysis on a single entity"""
        result = {
            'entity': entity,
            'type': entity_type,
            'timestamp': time.time()
        }

        if entity_type == 'ip':
            result.update(self.analyze_ip(entity))
        elif entity_type == 'domain':
            result.update(self.analyze_domain(entity))
        elif entity_type == 'email':
            result.update(self.analyze_email(entity))
        elif entity_type == 'url':
            result.update(self.analyze_url(entity))

        return result

    def analyze_ip(self, ip: str) -> Dict[str, Any]:
        """Analyze IP address"""
        try:
            # Basic IP info (in production, use actual OSINT APIs)
            return {
                'geolocation': 'Unknown',
                'isp': 'Unknown',
                'reputation': 'neutral',
                'notes': 'Connect to Shodan/VirusTotal for detailed analysis'
            }
        except Exception as e:
            return {'error': str(e)}

    def analyze_domain(self, domain: str) -> Dict[str, Any]:
        """Analyze domain"""
        try:
            return {
                'whois': 'Available via WHOIS',
                'dns_records': 'Available via DNS lookup',
                'ssl_info': 'Available via SSL certificate lookup',
                'notes': 'Connect to WHOIS/DNS APIs for detailed analysis'
            }
        except Exception as e:
            return {'error': str(e)}

    def analyze_email(self, email: str) -> Dict[str, Any]:
        """Analyze email address"""
        try:
            domain = email.split('@')[1]
            return {
                'domain': domain,
                'domain_reputation': 'Unknown',
                'breach_check': 'Check HaveIBeenPwned',
                'notes': 'Connect to breach databases for verification'
            }
        except Exception as e:
            return {'error': str(e)}

    def analyze_url(self, url: str) -> Dict[str, Any]:
        """Analyze URL"""
        try:
            return {
                'status': 'Accessible',
                'content_type': 'text/html',
                'security_headers': 'Check via security scanner',
                'notes': 'Connect to URL analysis services'
            }
        except Exception as e:
            return {'error': str(e)}


class DataProcessor:
    """Data processing module"""

    def __init__(self):
        pass

    def process_text(self, text: str) -> Dict[str, Any]:
        """Process and analyze text data"""
        return {
            'character_count': len(text),
            'word_count': len(text.split()),
            'line_count': len(text.split('\n')),
            'sentence_count': len(re.split(r'[.!?]+', text)),
            'avg_word_length': sum(len(word) for word in text.split()) / len(text.split()) if text.split() else 0
        }

    def extract_keywords(self, text: str, top_n: int = 10) -> List[Tuple[str, int]]:
        """Extract top keywords from text"""
        words = re.findall(r'\b\w+\b', text.lower())
        word_freq = {}

        for word in words:
            if len(word) > 3:  # Filter short words
                word_freq[word] = word_freq.get(word, 0) + 1

        return sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:top_n]


class MLAnalyzer:
    """Machine learning analysis module"""

    def __init__(self):
        # In production, load actual ML models
        self.models_loaded = False

    def analyze_text(self, text: str) -> Dict[str, Any]:
        """Analyze text using ML techniques"""
        return {
            'sentiment': self.analyze_sentiment(text),
            'topics': self.extract_topics(text),
            'language': self.detect_language(text),
            'classification': self.classify_text(text)
        }

    def analyze_sentiment(self, text: str) -> Dict[str, Any]:
        """Analyze sentiment of text"""
        # Simplified sentiment analysis
        positive_words = ['good', 'great', 'excellent', 'positive', 'success']
        negative_words = ['bad', 'terrible', 'negative', 'failure', 'error']

        text_lower = text.lower()
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)

        if positive_count > negative_count:
            sentiment = 'positive'
        elif negative_count > positive_count:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'

        return {
            'sentiment': sentiment,
            'confidence': 0.7,
            'positive_count': positive_count,
            'negative_count': negative_count
        }

    def extract_topics(self, text: str) -> List[str]:
        """Extract topics from text"""
        # Simplified topic extraction
        keywords = ['security', 'network', 'data', 'analysis', 'threat',
                   'intelligence', 'investigation', 'malware', 'phishing']

        text_lower = text.lower()
        found_topics = [kw for kw in keywords if kw in text_lower]

        return found_topics if found_topics else ['general']

    def detect_language(self, text: str) -> str:
        """Detect language of text"""
        # Simplified language detection
        if re.search(r'[à-üÀ-Ü]', text):
            return 'likely_non_english'
        return 'english'

    def classify_text(self, text: str) -> str:
        """Classify text into categories"""
        text_lower = text.lower()

        if any(word in text_lower for word in ['attack', 'breach', 'hack', 'malware']):
            return 'security_incident'
        elif any(word in text_lower for word in ['ip', 'domain', 'url', 'email']):
            return 'osint_reconnaissance'
        elif any(word in text_lower for word in ['report', 'analysis', 'findings']):
            return 'analysis_report'
        else:
            return 'general'


class APICollector:
    """API collection module for OSINT data gathering"""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'OSINT-Tool/1.0'
        })

    def collect_shodan_data(self, query: str) -> Dict[str, Any]:
        """Collect data from Shodan (requires API key)"""
        # Placeholder - requires actual Shodan API key
        return {
            'service': 'Shodan',
            'query': query,
            'results': [],
            'note': 'Configure SHODAN_API_KEY environment variable'
        }

    def collect_virustotal_data(self, resource: str) -> Dict[str, Any]:
        """Collect data from VirusTotal (requires API key)"""
        # Placeholder - requires actual VirusTotal API key
        return {
            'service': 'VirusTotal',
            'resource': resource,
            'results': [],
            'note': 'Configure VIRUSTOTAL_API_KEY environment variable'
        }

    def scan_url(self, url: str) -> Dict[str, Any]:
        """Scan URL using multiple services"""
        return {
            'url': url,
            'services': ['VirusTotal', 'URLScan', 'Shodan'],
            'status': 'Configure API keys for scanning'
        }

    def check_email_breach(self, email: str) -> Dict[str, Any]:
        """Check if email has been in data breaches (legitimate security check)"""
        return {
            'email': email,
            'service': 'HaveIBeenPwned',
            'status': 'Configure HIBP_API_KEY for breach checking',
            'note': 'Used for legitimate security awareness'
        }

    def lookup_domain_whois(self, domain: str) -> Dict[str, Any]:
        """Lookup WHOIS information for a domain (public record)"""
        return {
            'domain': domain,
            'service': 'WHOIS',
            'status': 'Publicly available domain registration data',
            'note': 'Use python-whois for actual lookups'
        }

    def check_ssl_certificate(self, domain: str) -> Dict[str, Any]:
        """Check SSL certificate information (public data)"""
        return {
            'domain': domain,
            'service': 'SSL Certificate Lookup',
            'status': 'Public SSL certificate information',
            'note': 'Valid for security analysis'
        }


class NetworkRecon:
    """Network reconnaissance for authorized security testing"""

    def __init__(self):
        pass

    def perform_ping(self, host: str) -> Dict[str, Any]:
        """Ping a host to check connectivity (authorized network)"""
        return {
            'host': host,
            'test': 'Ping',
            'status': 'Requires system ping command',
            'note': 'Only test networks you have authorization to scan'
        }

    def perform_traceroute(self, host: str) -> Dict[str, Any]:
        """Traceroute to a host (authorized network)"""
        return {
            'host': host,
            'test': 'Traceroute',
            'status': 'Requires system traceroute command',
            'note': 'Only trace networks you have authorization to test'
        }

    def scan_ports(self, host: str, ports: List[int]) -> Dict[str, Any]:
        """Scan specific ports on a host (authorized security testing)"""
        return {
            'host': host,
            'ports': ports,
            'test': 'Port Scan',
            'status': 'Use nmap for actual port scanning',
            'note': 'Port scanning requires explicit authorization'
        }

    def check_dns_records(self, domain: str) -> Dict[str, Any]:
        """Check DNS records for a domain (public data)"""
        return {
            'domain': domain,
            'test': 'DNS Lookup',
            'record_types': ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME'],
            'status': 'Use dnspython for actual DNS lookups',
            'note': 'DNS records are public information'
        }


class VulnerabilityScanner:
    """Vulnerability scanning for authorized targets"""

    def __init__(self):
        pass

    def scan_cves(self, target: str) -> Dict[str, Any]:
        """Scan for known CVEs (public vulnerability database)"""
        return {
            'target': target,
            'database': 'NVD (National Vulnerability Database)',
            'status': 'Query public CVE databases',
            'note': 'Use CVE API for vulnerability information'
        }

    def check_http_headers(self, url: str) -> Dict[str, Any]:
        """Check HTTP security headers (legitimate security assessment)"""
        return {
            'url': url,
            'check': 'Security Headers',
            'headers_to_check': [
                'Strict-Transport-Security',
                'Content-Security-Policy',
                'X-Frame-Options',
                'X-Content-Type-Options',
                'X-XSS-Protection'
            ],
            'note': 'Standard security assessment'
        }

    def analyze_ssl_tls(self, domain: str) -> Dict[str, Any]:
        """Analyze SSL/TLS configuration (legitimate security assessment)"""
        return {
            'domain': domain,
            'check': 'SSL/TLS Configuration',
            'checks': [
                'Certificate validity',
                'Protocol versions',
                'Cipher suites',
                'Certificate chain'
            ],
            'note': 'Use tools like testssl.sh for detailed analysis'
        }


class ThreatIntel:
    """Threat intelligence gathering for security awareness"""

    def __init__(self):
        pass

    def check_ip_reputation(self, ip: str) -> Dict[str, Any]:
        """Check IP reputation against threat intelligence feeds"""
        return {
            'ip': ip,
            'feeds': [
                'AbuseIPDB',
                'VirusTotal',
                'Spamhaus',
                'Talos Intelligence'
            ],
            'status': 'Requires API keys for threat intel feeds',
            'note': 'Used for security awareness and defense'
        }

    def check_domain_reputation(self, domain: str) -> Dict[str, Any]:
        """Check domain reputation against threat intelligence feeds"""
        return {
            'domain': domain,
            'feeds': [
                'VirusTotal',
                'URLhaus',
                'PhishTank'
            ],
            'status': 'Requires API keys for threat intel feeds',
            'note': 'Used for security awareness and defense'
        }

    def get_malware_hashes(self, file_hash: str) -> Dict[str, Any]:
        """Check malware hash against threat databases"""
        return {
            'hash': file_hash,
            'databases': [
                'VirusTotal',
                'Hybrid Analysis',
                'MalwareBazaar'
            ],
            'status': 'Requires API keys for malware databases',
            'note': 'Used for malware analysis and defense'
        }


class SocialMediaAnalyzer:
    """Social media OSINT analysis for legitimate research"""

    def __init__(self):
        pass

    def analyze_username(self, username: str) -> Dict[str, Any]:
        """Analyze username across platforms (public data only)"""
        return {
            'username': username,
            'platforms': [
                'Twitter/X',
                'Instagram',
                'Facebook',
                'LinkedIn',
                'GitHub',
                'Reddit'
            ],
            'check_status': 'Public profile analysis only',
            'note': 'Only analyze publicly available profiles',
            'legal_note': 'Do not use for harassment or stalking'
        }

    def extract_profiles(self, text: str) -> List[str]:
        """Extract social media profile links from text"""
        patterns = {
            'twitter': r'(?:https?://)?(?:www\.)?(?:twitter|x)\.com/[\w]+',
            'instagram': r'(?:https?://)?(?:www\.)?instagram\.com/[\w]+',
            'linkedin': r'(?:https?://)?(?:www\.)?linkedin\.com/in/[\w-]+',
            'github': r'(?:https?://)?(?:www\.)?github\.com/[\w]+',
            'reddit': r'(?:https?://)?(?:www\.)?reddit\.com/user/[\w]+'
        }

        profiles = []
        for platform, pattern in patterns.items():
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches:
                profiles.append(f"{platform}: {match}")

        return profiles

    def analyze_hashtags(self, text: str) -> Dict[str, Any]:
        """Analyze hashtags for trending topics"""
        hashtags = re.findall(r'#\w+', text)
        return {
            'hashtags': hashtags,
            'count': len(hashtags),
            'unique_count': len(set(hashtags)),
            'note': 'Hashtag analysis for OSINT research'
        }


class GeolocationAnalyzer:
    """IP geolocation analysis for legitimate security research"""

    def __init__(self):
        self.session = requests.Session()

    def get_ip_geolocation(self, ip: str) -> Dict[str, Any]:
        """Get geolocation data for an IP address"""
        try:
            # Using free ip-api.com (no API key required for basic use)
            response = self.session.get(f'http://ip-api.com/json/{ip}', timeout=5)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return {
                        'ip': ip,
                        'country': data.get('country'),
                        'country_code': data.get('countryCode'),
                        'region': data.get('regionName'),
                        'city': data.get('city'),
                        'zip': data.get('zip'),
                        'lat': data.get('lat'),
                        'lon': data.get('lon'),
                        'timezone': data.get('timezone'),
                        'isp': data.get('isp'),
                        'org': data.get('org'),
                        'as': data.get('as'),
                        'source': 'ip-api.com',
                        'note': 'Public geolocation data'
                    }
                else:
                    return {'error': data.get('message', 'Unknown error')}
            else:
                return {'error': f'API error: {response.status_code}'}
        except Exception as e:
            return {'error': str(e)}

    def get_local_ip(self) -> Dict[str, Any]:
        """Get local IP information"""
        try:
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            return {
                'hostname': hostname,
                'local_ip': local_ip,
                'note': 'Local network information'
            }
        except Exception as e:
            return {'error': str(e)}


class HashAnalyzer:
    """File hash analysis for malware detection"""

    def __init__(self):
        pass

    def calculate_file_hash(self, file_path: str, algorithm: str = 'sha256') -> Dict[str, Any]:
        """Calculate hash of a file"""
        try:
            hash_func = hashlib.new(algorithm)
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b''):
                    hash_func.update(chunk)
            return {
                'file': file_path,
                'algorithm': algorithm,
                'hash': hash_func.hexdigest(),
                'status': 'Hash calculated successfully'
            }
        except Exception as e:
            return {'error': str(e)}

    def calculate_string_hash(self, text: str, algorithm: str = 'sha256') -> Dict[str, Any]:
        """Calculate hash of a string"""
        try:
            hash_func = hashlib.new(algorithm)
            hash_func.update(text.encode('utf-8'))
            return {
                'text': text[:50] + '...' if len(text) > 50 else text,
                'algorithm': algorithm,
                'hash': hash_func.hexdigest(),
                'status': 'Hash calculated successfully'
            }
        except Exception as e:
            return {'error': str(e)}

    def check_hash_virustotal(self, file_hash: str, api_key: str = None) -> Dict[str, Any]:
        """Check hash against VirusTotal (requires API key)"""
        if not api_key:
            return {
                'hash': file_hash,
                'status': 'API key required',
                'note': 'Configure VIRUSTOTAL_API_KEY in .env file'
            }

        try:
            url = f'https://www.virustotal.com/api/v3/files/{file_hash}'
            headers = {'x-apikey': api_key}
            response = requests.get(url, headers=headers, timeout=10)

            if response.status_code == 200:
                data = response.json()
                return {
                    'hash': file_hash,
                    'source': 'VirusTotal',
                    'data': data,
                    'status': 'Check successful'
                }
            else:
                return {'error': f'API error: {response.status_code}'}
        except Exception as e:
            return {'error': str(e)}


class ShodanAPI:
    """Shodan API integration for security research"""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv('SHODAN_API_KEY')
        self.base_url = 'https://api.shodan.io'
        self.session = requests.Session()

    def search(self, query: str) -> Dict[str, Any]:
        """Search Shodan for devices"""
        if not self.api_key:
            return {
                'query': query,
                'status': 'API key required',
                'note': 'Configure SHODAN_API_KEY in .env file'
            }

        try:
            url = f'{self.base_url}/shodan/host/search?key={self.api_key}&query={query}'
            response = self.session.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()
                return {
                    'query': query,
                    'total': data.get('total', 0),
                    'results': data.get('matches', [])[:10],  # Limit to 10 results
                    'source': 'Shodan',
                    'status': 'Search successful'
                }
            else:
                return {'error': f'API error: {response.status_code}'}
        except Exception as e:
            return {'error': str(e)}

    def host_info(self, ip: str) -> Dict[str, Any]:
        """Get information about a specific host"""
        if not self.api_key:
            return {
                'ip': ip,
                'status': 'API key required',
                'note': 'Configure SHODAN_API_KEY in .env file'
            }

        try:
            url = f'{self.base_url}/shodan/host/{ip}?key={self.api_key}'
            response = self.session.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()
                return {
                    'ip': ip,
                    'data': data,
                    'source': 'Shodan',
                    'status': 'Query successful'
                }
            else:
                return {'error': f'API error: {response.status_code}'}
        except Exception as e:
            return {'error': str(e)}


class VirusTotalAPI:
    """VirusTotal API integration for malware analysis"""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv('VIRUSTOTAL_API_KEY')
        self.base_url = 'https://www.virustotal.com/api/v3'
        self.session = requests.Session()

    def scan_url(self, url: str) -> Dict[str, Any]:
        """Scan a URL"""
        if not self.api_key:
            return {
                'url': url,
                'status': 'API key required',
                'note': 'Configure VIRUSTOTAL_API_KEY in .env file'
            }

        try:
            scan_url = f'{self.base_url}/urls'
            headers = {'x-apikey': self.api_key}
            data = {'url': url}
            response = self.session.post(scan_url, headers=headers, data=data, timeout=10)

            if response.status_code == 200:
                data = response.json()
                analysis_id = data.get('data', {}).get('id')
                return {
                    'url': url,
                    'analysis_id': analysis_id,
                    'source': 'VirusTotal',
                    'status': 'Scan initiated'
                }
            else:
                return {'error': f'API error: {response.status_code}'}
        except Exception as e:
            return {'error': str(e)}

    def get_report(self, resource: str) -> Dict[str, Any]:
        """Get analysis report for a resource"""
        if not self.api_key:
            return {
                'resource': resource,
                'status': 'API key required',
                'note': 'Configure VIRUSTOTAL_API_KEY in .env file'
            }

        try:
            url = f'{self.base_url}/urls/{resource}'
            headers = {'x-apikey': self.api_key}
            response = self.session.get(url, headers=headers, timeout=10)

            if response.status_code == 200:
                data = response.json()
                return {
                    'resource': resource,
                    'data': data,
                    'source': 'VirusTotal',
                    'status': 'Report retrieved'
                }
            else:
                return {'error': f'API error: {response.status_code}'}
        except Exception as e:
            return {'error': str(e)}


class BlueTeamMonitor:
    """Blue team monitoring and detection tools"""

    def __init__(self):
        pass

    def analyze_log_entry(self, log_line: str) -> Dict[str, Any]:
        """Analyze a single log entry for security events"""
        # Common security indicators in logs
        security_keywords = [
            'failed', 'denied', 'unauthorized', 'attack', 'intrusion',
            'malware', 'virus', 'exploit', 'injection', 'brute force',
            'ssh', 'login', 'authentication', 'permission', 'access'
        ]

        log_lower = log_line.lower()
        found_keywords = [kw for kw in security_keywords if kw in log_lower]

        # Extract IP addresses
        ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', log_line)

        # Extract timestamps (common formats)
        timestamps = re.findall(r'\d{4}-\d{2}-\d{2}[\sT]\d{2}:\d{2}:\d{2}', log_line)

        return {
            'log_line': log_line[:200] + '...' if len(log_line) > 200 else log_line,
            'security_keywords_found': found_keywords,
            'ip_addresses': ips,
            'timestamps': timestamps,
            'severity': 'high' if any(kw in ['attack', 'intrusion', 'malware', 'exploit'] for kw in found_keywords) else 'medium' if found_keywords else 'low',
            'note': 'Basic log analysis for security monitoring'
        }

    def detect_suspicious_activity(self, logs: List[str]) -> Dict[str, Any]:
        """Detect suspicious patterns in logs"""
        suspicious_patterns = {
            'multiple_failed_logins': 0,
            'brute_force_indicators': 0,
            'injection_attempts': 0,
            'unusual_access': 0
        }

        for log in logs:
            log_lower = log.lower()
            if 'failed' in log_lower and 'login' in log_lower:
                suspicious_patterns['multiple_failed_logins'] += 1
            if 'brute' in log_lower or 'force' in log_lower:
                suspicious_patterns['brute_force_indicators'] += 1
            if 'injection' in log_lower or 'sql' in log_lower:
                suspicious_patterns['injection_attempts'] += 1
            if 'unauthorized' in log_lower or 'forbidden' in log_lower:
                suspicious_patterns['unusual_access'] += 1

        return {
            'total_logs_analyzed': len(logs),
            'suspicious_patterns': suspicious_patterns,
            'risk_level': 'high' if any(v > 5 for v in suspicious_patterns.values()) else 'medium' if any(v > 0 for v in suspicious_patterns.values()) else 'low',
            'note': 'Suspicious activity detection for security monitoring'
        }

    def monitor_port_activity(self, ports: List[int]) -> Dict[str, Any]:
        """Check if ports are listening (authorized network only)"""
        results = {}
        for port in ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex(('localhost', port))
                sock.close()
                results[port] = 'open' if result == 0 else 'closed'
            except Exception as e:
                results[port] = f'error: {str(e)}'

        return {
            'ports_checked': ports,
            'results': results,
            'note': 'Port monitoring for local system only',
            'warning': 'Only monitor systems you have authorization to monitor'
        }


class LogAnalyzer:
    """Comprehensive log analysis for incident response"""

    def __init__(self):
        pass

    def parse_apache_log(self, log_line: str) -> Dict[str, Any]:
        """Parse Apache/Nginx access log format"""
        # Common log format pattern
        pattern = r'(\S+) \S+ \S+ \[([\w:/]+\s[+\-]\d{4})\] "(.+?)" (\d{3}) (\d+) "([^"]*)" "([^"]*)"'
        match = re.match(pattern, log_line)

        if match:
            return {
                'ip': match.group(1),
                'timestamp': match.group(2),
                'request': match.group(3),
                'status_code': match.group(4),
                'size': match.group(5),
                'referrer': match.group(6),
                'user_agent': match.group(7),
                'parsed': True
            }
        else:
            return {
                'log_line': log_line[:100],
                'parsed': False,
                'note': 'Could not parse as Apache log format'
            }

    def analyze_access_patterns(self, logs: List[str]) -> Dict[str, Any]:
        """Analyze access patterns in web logs"""
        status_codes = {}
        user_agents = {}
        ips = {}

        for log in logs:
            # Extract status codes
            status_match = re.search(r'\s(\d{3})\s', log)
            if status_match:
                code = status_match.group(1)
                status_codes[code] = status_codes.get(code, 0) + 1

            # Extract IPs
            ip_match = re.match(r'^(\S+)', log)
            if ip_match:
                ip = ip_match.group(1)
                ips[ip] = ips.get(ip, 0) + 1

        return {
            'total_requests': len(logs),
            'status_codes': status_codes,
            'top_ips': sorted(ips.items(), key=lambda x: x[1], reverse=True)[:10],
            'note': 'Access pattern analysis for security monitoring'
        }


class IncidentResponse:
    """Incident response tools and procedures"""

    def __init__(self):
        pass

    def create_incident_report(self, incident_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a structured incident report"""
        return {
            'incident_id': f"INC-{int(time.time())}",
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'severity': incident_data.get('severity', 'medium'),
            'type': incident_data.get('type', 'security_incident'),
            'description': incident_data.get('description', ''),
            'affected_assets': incident_data.get('affected_assets', []),
            'indicators': incident_data.get('indicators', []),
            'actions_taken': incident_data.get('actions_taken', []),
            'status': 'open',
            'note': 'Incident report for documentation and tracking'
        }

    def check_iocs(self, ioc_list: List[str]) -> Dict[str, Any]:
        """Check indicators of compromise against threat feeds"""
        results = {}
        for ioc in ioc_list:
            if re.match(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', ioc):
                results[ioc] = {'type': 'ip', 'check': 'threat_intel_required'}
            elif re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', ioc):
                results[ioc] = {'type': 'email', 'check': 'breach_database_required'}
            elif re.match(r'^[a-fA-F0-9]{32,}$', ioc):
                results[ioc] = {'type': 'hash', 'check': 'malware_database_required'}
            else:
                results[ioc] = {'type': 'unknown', 'check': 'manual_verification_required'}

        return {
            'total_iocs': len(ioc_list),
            'results': results,
            'note': 'IOC checking requires API integration with threat feeds'
        }

    def generate_response_checklist(self, incident_type: str) -> Dict[str, Any]:
        """Generate incident response checklist based on incident type"""
        checklists = {
            'malware': [
                'Isolate affected systems',
                'Identify malware variant',
                'Scan for other infections',
                'Collect malware samples',
                'Determine entry point',
                'Contain the threat',
                'Eradicate malware',
                'Recover systems',
                'Document lessons learned'
            ],
            'phishing': [
                'Identify phishing targets',
                'Block malicious emails',
                'Reset compromised credentials',
                'Analyze phishing campaign',
                'Educate affected users',
                'Update email filters',
                'Monitor for follow-up attacks',
                'Document incident'
            ],
            'brute_force': [
                'Identify source IP',
                'Block source IP',
                'Review authentication logs',
                'Check for successful breaches',
                'Strengthen authentication',
                'Implement rate limiting',
                'Monitor for continued attempts',
                'Document incident'
            ]
        }

        return {
            'incident_type': incident_type,
            'checklist': checklists.get(incident_type, ['Assess situation', 'Contain threat', 'Investigate', 'Recover', 'Document']),
            'note': 'Incident response checklist for guidance'
        }
