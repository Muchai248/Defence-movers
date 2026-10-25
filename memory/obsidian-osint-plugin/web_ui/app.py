#!/usr/bin/env python3
"""
Brain UI - Neural Memory Visualization for OSINT Data
Web-based interface that displays OSINT data in a brain/neural network visualization
"""

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import json
import sys
import os
from pathlib import Path

# Add parent directory to path to import osint_modules
sys.path.insert(0, str(Path(__file__).parent.parent / 'backend'))
from osint_modules import (
    GeolocationAnalyzer,
    HashAnalyzer,
    BlueTeamMonitor,
    SocialMediaAnalyzer,
    LogAnalyzer,
    IncidentResponse
)

app = Flask(__name__)
CORS(app)

# Initialize analyzers
geo_analyzer = GeolocationAnalyzer()
hash_analyzer = HashAnalyzer()
blue_team = BlueTeamMonitor()
social_media = SocialMediaAnalyzer()
log_analyzer = LogAnalyzer()
incident_response = IncidentResponse()

# Memory store for visualizations
memory_store = {
    'nodes': [],
    'connections': [],
    'last_updated': None
}


@app.route('/')
def index():
    """Render the brain UI"""
    return render_template('brain_ui.html')


@app.route('/api/memory')
def get_memory():
    """Get current memory state"""
    return jsonify(memory_store)


@app.route('/api/analyze', methods=['POST'])
def analyze_data():
    """Analyze data and update memory visualization"""
    data = request.json
    content = data.get('content', '')
    analysis_type = data.get('type', 'general')

    result = {}
    nodes = []
    connections = []

    if analysis_type == 'geolocation':
        ip = data.get('ip', '8.8.8.8')
        result = geo_analyzer.get_ip_geolocation(ip)
        nodes = create_geolocation_nodes(result, ip)
        connections = create_geolocation_connections(nodes)

    elif analysis_type == 'hash':
        result = hash_analyzer.calculate_string_hash(content, 'sha256')
        nodes = create_hash_nodes(result)
        connections = create_hash_connections(nodes)

    elif analysis_type == 'log':
        result = blue_team.analyze_log_entry(content)
        nodes = create_log_nodes(result)
        connections = create_log_connections(nodes)

    elif analysis_type == 'social':
        result = social_media.extract_profiles(content)
        nodes = create_social_nodes(result)
        connections = create_social_connections(nodes)

    elif analysis_type == 'incident':
        result = incident_response.create_incident_report(data.get('incident_data', {}))
        nodes = create_incident_nodes(result)
        connections = create_incident_connections(nodes)

    # Update memory store
    memory_store['nodes'] = nodes
    memory_store['connections'] = connections
    memory_store['last_updated'] = str(result.get('timestamp', 'now'))

    return jsonify({
        'result': result,
        'nodes': nodes,
        'connections': connections
    })


@app.route('/api/reset')
def reset_memory():
    """Reset memory visualization"""
    memory_store['nodes'] = []
    memory_store['connections'] = []
    memory_store['last_updated'] = None
    return jsonify({'status': 'reset'})


def create_geolocation_nodes(data, ip):
    """Create nodes for geolocation visualization"""
    return [
        {
            'id': 'ip',
            'label': ip,
            'type': 'central',
            'x': 50,
            'y': 50,
            'size': 30,
            'color': '#ff6b6b'
        },
        {
            'id': 'country',
            'label': data.get('country', 'Unknown'),
            'type': 'location',
            'x': 30,
            'y': 30,
            'size': 20,
            'color': '#4ecdc4'
        },
        {
            'id': 'city',
            'label': data.get('city', 'Unknown'),
            'type': 'location',
            'x': 70,
            'y': 30,
            'size': 15,
            'color': '#4ecdc4'
        },
        {
            'id': 'isp',
            'label': data.get('isp', 'Unknown'),
            'type': 'network',
            'x': 30,
            'y': 70,
            'size': 15,
            'color': '#ffe66d'
        },
        {
            'id': 'org',
            'label': data.get('org', 'Unknown'),
            'type': 'network',
            'x': 70,
            'y': 70,
            'size': 15,
            'color': '#ffe66d'
        }
    ]


def create_geolocation_connections(nodes):
    """Create connections for geolocation"""
    return [
        {'source': 'ip', 'target': 'country', 'strength': 0.8},
        {'source': 'ip', 'target': 'city', 'strength': 0.6},
        {'source': 'ip', 'target': 'isp', 'strength': 0.7},
        {'source': 'ip', 'target': 'org', 'strength': 0.7}
    ]


def create_hash_nodes(data):
    """Create nodes for hash visualization"""
    hash_value = data.get('hash', 'unknown')[:16] + '...'
    return [
        {
            'id': 'input',
            'label': 'Input',
            'type': 'input',
            'x': 20,
            'y': 50,
            'size': 20,
            'color': '#95e1d3'
        },
        {
            'id': 'hash',
            'label': hash_value,
            'type': 'central',
            'x': 50,
            'y': 50,
            'size': 35,
            'color': '#f38181'
        },
        {
            'id': 'algorithm',
            'label': data.get('algorithm', 'sha256'),
            'type': 'meta',
            'x': 80,
            'y': 50,
            'size': 15,
            'color': '#aa96da'
        }
    ]


def create_hash_connections(nodes):
    """Create connections for hash"""
    return [
        {'source': 'input', 'target': 'hash', 'strength': 1.0},
        {'source': 'hash', 'target': 'algorithm', 'strength': 0.9}
    ]


def create_log_nodes(data):
    """Create nodes for log analysis visualization"""
    severity = data.get('severity', 'low')
    color = '#95e1d3' if severity == 'low' else '#ffe66d' if severity == 'medium' else '#f38181'

    nodes = [
        {
            'id': 'log',
            'label': 'Log Entry',
            'type': 'central',
            'x': 50,
            'y': 50,
            'size': 30,
            'color': color
        }
    ]

    # Add keyword nodes
    keywords = data.get('security_keywords_found', [])
    for i, kw in enumerate(keywords):
        angle = (i / len(keywords)) * 360
        x = 50 + 30 * (angle / 360)
        y = 50 + 30 * (1 if i % 2 else -1)
        nodes.append({
            'id': f'kw_{i}',
            'label': kw,
            'type': 'keyword',
            'x': x,
            'y': y,
            'size': 12,
            'color': '#aa96da'
        })

    # Add IP nodes
    ips = data.get('ip_addresses', [])
    for i, ip in enumerate(ips):
        nodes.append({
            'id': f'ip_{i}',
            'label': ip,
            'type': 'ip',
            'x': 20 + i * 15,
            'y': 80,
            'size': 15,
            'color': '#4ecdc4'
        })

    return nodes


def create_log_connections(nodes):
    """Create connections for log analysis"""
    connections = []
    for node in nodes:
        if node['type'] in ['keyword', 'ip']:
            connections.append({'source': 'log', 'target': node['id'], 'strength': 0.8})
    return connections


def create_social_nodes(profiles):
    """Create nodes for social media visualization"""
    nodes = [
        {
            'id': 'central',
            'label': 'Social',
            'type': 'central',
            'x': 50,
            'y': 50,
            'size': 25,
            'color': '#f38181'
        }
    ]

    platform_colors = {
        'twitter': '#1da1f2',
        'github': '#333',
        'linkedin': '#0077b5',
        'instagram': '#e1306c',
        'reddit': '#ff4500'
    }

    for i, profile in enumerate(profiles[:5]):
        angle = (i / len(profiles)) * 360
        x = 50 + 30 * (angle / 360)
        y = 50 + 30 * (1 if i % 2 else -1)

        platform = profile.split(':')[0] if ':' in profile else 'unknown'
        color = platform_colors.get(platform, '#95e1d3')

        nodes.append({
            'id': f'social_{i}',
            'label': profile.split('/')[-1][:15],
            'type': 'social',
            'x': x,
            'y': y,
            'size': 15,
            'color': color
        })

    return nodes


def create_social_connections(nodes):
    """Create connections for social media"""
    connections = []
    for node in nodes:
        if node['type'] == 'social':
            connections.append({'source': 'central', 'target': node['id'], 'strength': 0.7})
    return connections


def create_incident_nodes(data):
    """Create nodes for incident response visualization"""
    severity = data.get('severity', 'medium')
    color = '#95e1d3' if severity == 'low' else '#ffe66d' if severity == 'medium' else '#f38181'

    return [
        {
            'id': 'incident',
            'label': data.get('incident_id', 'INC'),
            'type': 'central',
            'x': 50,
            'y': 50,
            'size': 35,
            'color': color
        },
        {
            'id': 'type',
            'label': data.get('type', 'unknown'),
            'type': 'meta',
            'x': 30,
            'y': 30,
            'size': 15,
            'color': '#aa96da'
        },
        {
            'id': 'severity',
            'label': severity,
            'type': 'meta',
            'x': 70,
            'y': 30,
            'size': 15,
            'color': color
        },
        {
            'id': 'status',
            'label': data.get('status', 'open'),
            'type': 'meta',
            'x': 50,
            'y': 80,
            'size': 15,
            'color': '#4ecdc4'
        }
    ]


def create_incident_connections(nodes):
    """Create connections for incident response"""
    return [
        {'source': 'incident', 'target': 'type', 'strength': 0.9},
        {'source': 'incident', 'target': 'severity', 'strength': 0.9},
        {'source': 'incident', 'target': 'status', 'strength': 0.8}
    ]


if __name__ == '__main__':
    print("🧠 Brain UI - Neural Memory Visualization")
    print("📡 Starting web server on http://localhost:5000")
    print("🔗 Open your browser to see the brain visualization")
    app.run(host='0.0.0.0', port=5000, debug=True)
