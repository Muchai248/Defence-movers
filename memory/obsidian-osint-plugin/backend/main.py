#!/usr/bin/env python3
"""
OSINT Backend for Obsidian Plugin
Processes requests from Obsidian plugin via local file communication
"""

import os
import json
import time
import threading
from pathlib import Path
from typing import Dict, Any
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from osint_modules import (
    OSINTAnalyzer,
    DataProcessor,
    MLAnalyzer,
    APICollector,
    NetworkRecon,
    VulnerabilityScanner,
    ThreatIntel,
    SocialMediaAnalyzer,
    GeolocationAnalyzer,
    HashAnalyzer,
    ShodanAPI,
    VirusTotalAPI,
    BlueTeamMonitor,
    LogAnalyzer,
    IncidentResponse
)

class SharedMemoryHandler(FileSystemEventHandler):
    """Handles file system events in shared memory directory"""

    def __init__(self, backend: 'OSINTBackend'):
        self.backend = backend
        self.processed_files = set()

    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith('.json'):
            # Avoid processing response files
            if not event.src_path.endswith('_response.json'):
                # Process in a separate thread to avoid blocking
                thread = threading.Thread(target=self.backend.process_request, args=(event.src_path,))
                thread.start()

class OSINTBackend:
    """Main backend for OSINT operations"""

    def __init__(self, shared_memory_path: str = '../shared-memory'):
        self.shared_memory_path = Path(shared_memory_path)
        self.shared_memory_path.mkdir(parents=True, exist_ok=True)

        # Initialize modules
        self.osint_analyzer = OSINTAnalyzer()
        self.data_processor = DataProcessor()
        self.ml_analyzer = MLAnalyzer()
        self.api_collector = APICollector()
        self.network_recon = NetworkRecon()
        self.vuln_scanner = VulnerabilityScanner()
        self.threat_intel = ThreatIntel()
        self.social_media = SocialMediaAnalyzer()
        self.geolocation = GeolocationAnalyzer()
        self.hash_analyzer = HashAnalyzer()
        self.shodan = ShodanAPI()
        self.virustotal = VirusTotalAPI()
        self.blue_team = BlueTeamMonitor()
        self.log_analyzer = LogAnalyzer()
        self.incident_response = IncidentResponse()

        self.running = False

    def process_request(self, request_path: str):
        """Process a request from the Obsidian plugin (runs in thread)"""
        try:
            # Read request
            with open(request_path, 'r') as f:
                request_data = json.load(f)

            print(f"Processing request: {request_data.get('type', 'unknown')}")

            # Process based on type
            response = self.handle_request(request_data)

            # Write response
            response_path = request_path.replace('.json', '_response.json')
            with open(response_path, 'w') as f:
                json.dump(response, f, indent=2)

            print(f"Response written to: {response_path}")

        except Exception as e:
            print(f"Error processing request: {e}")
            # Write error response
            response_path = request_path.replace('.json', '_response.json')
            with open(response_path, 'w') as f:
                json.dump({
                    'type': 'error',
                    'error': str(e),
                    'timestamp': time.time()
                }, f, indent=2)

    def handle_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Route request to appropriate handler"""

        request_type = request.get('type')

        if request_type == 'osint_analysis':
            return self.handle_osint_analysis(request)
        elif request_type == 'analyze':
            return self.handle_analysis(request)
        elif request_type == 'network_recon':
            return self.handle_network_recon(request)
        elif request_type == 'vuln_scan':
            return self.handle_vuln_scan(request)
        elif request_type == 'threat_intel':
            return self.handle_threat_intel(request)
        elif request_type == 'social_media':
            return self.handle_social_media(request)
        elif request_type == 'geolocation':
            return self.handle_geolocation(request)
        elif request_type == 'hash_analysis':
            return self.handle_hash_analysis(request)
        elif request_type == 'shodan_search':
            return self.handle_shodan_search(request)
        elif request_type == 'virustotal_scan':
            return self.handle_virustotal_scan(request)
        elif request_type == 'blue_team_monitor':
            return self.handle_blue_team_monitor(request)
        elif request_type == 'log_analysis':
            return self.handle_log_analysis(request)
        elif request_type == 'incident_response':
            return self.handle_incident_response(request)
        elif request_type == 'start':
            return {'type': 'status', 'status': 'backend_running'}
        else:
            return {'type': 'error', 'error': f'Unknown request type: {request_type}'}

    def handle_osint_analysis(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle OSINT analysis request"""
        content = request.get('content', '')
        file_path = request.get('file', '')

        # Extract entities from content
        entities = self.osint_analyzer.extract_entities(content)

        # Perform OSINT on entities
        results = {}
        for entity_type, entity_list in entities.items():
            results[entity_type] = []
            for entity in entity_list:
                entity_data = self.osint_analyzer.analyze_entity(entity, entity_type)
                results[entity_type].append(entity_data)

        # ML analysis
        ml_insights = self.ml_analyzer.analyze_text(content)

        return {
            'type': 'osint_result',
            'data': {
                'entities': entities,
                'osint_results': results,
                'ml_insights': ml_insights,
                'file': file_path
            },
            'timestamp': time.time()
        }

    def handle_analysis(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle general analysis request"""
        content = request.get('content', '')

        # Data processing
        processed_data = self.data_processor.process_text(content)

        # ML analysis
        ml_results = self.ml_analyzer.analyze_text(content)

        return {
            'type': 'analysis_result',
            'summary': f'Analyzed {len(content)} characters',
            'data': {
                'processed': processed_data,
                'ml': ml_results
            },
            'timestamp': time.time()
        }

    def handle_network_recon(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle network reconnaissance request (authorized testing only)"""
        target = request.get('target', '')
        recon_type = request.get('recon_type', 'ping')

        results = {}

        if recon_type == 'ping':
            results = self.network_recon.perform_ping(target)
        elif recon_type == 'traceroute':
            results = self.network_recon.perform_traceroute(target)
        elif recon_type == 'dns':
            results = self.network_recon.check_dns_records(target)
        elif recon_type == 'port_scan':
            ports = request.get('ports', [22, 80, 443])
            results = self.network_recon.scan_ports(target, ports)

        return {
            'type': 'network_recon_result',
            'data': results,
            'warning': 'Network reconnaissance requires explicit authorization',
            'timestamp': time.time()
        }

    def handle_vuln_scan(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle vulnerability scan request (authorized targets only)"""
        target = request.get('target', '')
        scan_type = request.get('scan_type', 'cve')

        results = {}

        if scan_type == 'cve':
            results = self.vuln_scanner.scan_cves(target)
        elif scan_type == 'http_headers':
            results = self.vuln_scanner.check_http_headers(target)
        elif scan_type == 'ssl_tls':
            results = self.vuln_scanner.analyze_ssl_tls(target)

        return {
            'type': 'vuln_scan_result',
            'data': results,
            'warning': 'Vulnerability scanning requires explicit authorization',
            'timestamp': time.time()
        }

    def handle_threat_intel(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle threat intelligence request"""
        target = request.get('target', '')
        intel_type = request.get('intel_type', 'ip')

        results = {}

        if intel_type == 'ip':
            results = self.threat_intel.check_ip_reputation(target)
        elif intel_type == 'domain':
            results = self.threat_intel.check_domain_reputation(target)
        elif intel_type == 'malware':
            results = self.threat_intel.get_malware_hashes(target)

        return {
            'type': 'threat_intel_result',
            'data': results,
            'timestamp': time.time()
        }

    def handle_social_media(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle social media analysis request"""
        content = request.get('content', '')
        username = request.get('username', '')
        action = request.get('action', 'extract_profiles')

        results = {}

        if action == 'extract_profiles':
            results = self.social_media.extract_profiles(content)
        elif action == 'analyze_username':
            results = self.social_media.analyze_username(username)
        elif action == 'analyze_hashtags':
            results = self.social_media.analyze_hashtags(content)

        return {
            'type': 'social_media_result',
            'data': results,
            'timestamp': time.time()
        }

    def handle_geolocation(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle geolocation request"""
        ip = request.get('ip', '')
        action = request.get('action', 'get_geolocation')

        results = {}

        if action == 'get_geolocation':
            results = self.geolocation.get_ip_geolocation(ip)
        elif action == 'get_local_ip':
            results = self.geolocation.get_local_ip()

        return {
            'type': 'geolocation_result',
            'data': results,
            'timestamp': time.time()
        }

    def handle_hash_analysis(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle hash analysis request"""
        content = request.get('content', '')
        file_path = request.get('file_path', '')
        action = request.get('action', 'calculate_string_hash')
        algorithm = request.get('algorithm', 'sha256')

        results = {}

        if action == 'calculate_string_hash':
            results = self.hash_analyzer.calculate_string_hash(content, algorithm)
        elif action == 'calculate_file_hash':
            results = self.hash_analyzer.calculate_file_hash(file_path, algorithm)
        elif action == 'check_virustotal':
            results = self.hash_analyzer.check_hash_virustotal(content)

        return {
            'type': 'hash_analysis_result',
            'data': results,
            'timestamp': time.time()
        }

    def handle_shodan_search(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle Shodan search request"""
        query = request.get('query', '')
        ip = request.get('ip', '')
        action = request.get('action', 'search')

        results = {}

        if action == 'search':
            results = self.shodan.search(query)
        elif action == 'host_info':
            results = self.shodan.host_info(ip)

        return {
            'type': 'shodan_result',
            'data': results,
            'timestamp': time.time()
        }

    def handle_virustotal_scan(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle VirusTotal scan request"""
        url = request.get('url', '')
        resource = request.get('resource', '')
        action = request.get('action', 'scan_url')

        results = {}

        if action == 'scan_url':
            results = self.virustotal.scan_url(url)
        elif action == 'get_report':
            results = self.virustotal.get_report(resource)

        return {
            'type': 'virustotal_result',
            'data': results,
            'timestamp': time.time()
        }

    def handle_blue_team_monitor(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle blue team monitoring request"""
        log_line = request.get('log_line', '')
        logs = request.get('logs', [])
        ports = request.get('ports', [])
        action = request.get('action', 'analyze_log')

        results = {}

        if action == 'analyze_log':
            results = self.blue_team.analyze_log_entry(log_line)
        elif action == 'detect_suspicious':
            results = self.blue_team.detect_suspicious_activity(logs)
        elif action == 'monitor_ports':
            results = self.blue_team.monitor_port_activity(ports)

        return {
            'type': 'blue_team_result',
            'data': results,
            'timestamp': time.time()
        }

    def handle_log_analysis(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle log analysis request"""
        log_line = request.get('log_line', '')
        logs = request.get('logs', [])
        action = request.get('action', 'parse_apache')

        results = {}

        if action == 'parse_apache':
            results = self.log_analyzer.parse_apache_log(log_line)
        elif action == 'analyze_patterns':
            results = self.log_analyzer.analyze_access_patterns(logs)

        return {
            'type': 'log_analysis_result',
            'data': results,
            'timestamp': time.time()
        }

    def handle_incident_response(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle incident response request"""
        incident_data = request.get('incident_data', {})
        ioc_list = request.get('ioc_list', [])
        incident_type = request.get('incident_type', '')
        action = request.get('action', 'create_report')

        results = {}

        if action == 'create_report':
            results = self.incident_response.create_incident_report(incident_data)
        elif action == 'check_iocs':
            results = self.incident_response.check_iocs(ioc_list)
        elif action == 'generate_checklist':
            results = self.incident_response.generate_response_checklist(incident_type)

        return {
            'type': 'incident_response_result',
            'data': results,
            'timestamp': time.time()
        }

    def start(self):
        """Start the backend server"""
        self.running = True

        # Set up file watcher
        event_handler = SharedMemoryHandler(self)
        observer = Observer()
        observer.schedule(event_handler, str(self.shared_memory_path), recursive=False)
        observer.start()

        print(f"OSINT Backend started", flush=True)
        print(f"Watching shared memory directory: {self.shared_memory_path}", flush=True)
        print("Press Ctrl+C to stop", flush=True)

        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.running = False
            observer.stop()

        observer.join()

    def stop(self):
        """Stop the backend server"""
        self.running = False


def main():
    """Main entry point"""
    import sys

    shared_memory_path = sys.argv[1] if len(sys.argv) > 1 else '../shared-memory'

    backend = OSINTBackend(shared_memory_path)
    backend.start()


if __name__ == '__main__':
    main()
