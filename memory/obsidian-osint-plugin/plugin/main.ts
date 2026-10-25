import { App, Plugin, PluginSettingTab, Setting, Notice, TFile } from 'obsidian';

interface OSINTSettings {
	backendPath: string;
	sharedMemoryPath: string;
	autoProcess: boolean;
}

const DEFAULT_SETTINGS: OSINTSettings = {
	backendPath: '../backend',
	sharedMemoryPath: '../shared-memory',
	autoProcess: true
}

export default class OSINTPlugin extends Plugin {
	settings: OSINTSettings;
	processingInterval: number | null = null;

	async onload() {
		await this.loadSettings();

		// Add ribbon icon
		this.addRibbonIcon('search', 'OSINT Tool', () => {
			this.runOSINTAnalysis();
		});

		// Add command
		this.addCommand({
			id: 'run-osint-analysis',
			name: 'Run OSINT Analysis',
			callback: () => this.runOSINTAnalysis()
		});

		this.addCommand({
			id: 'analyze-current-note',
			name: 'Analyze Current Note',
			callback: () => this.analyzeCurrentNote()
		});

		this.addCommand({
			id: 'start-backend',
			name: 'Start Python Backend',
			callback: () => this.startBackend()
		});

		// Social Media Analysis
		this.addCommand({
			id: 'analyze-social-media',
			name: 'Analyze Social Media Profiles',
			callback: () => this.analyzeSocialMedia()
		});

		// Geolocation
		this.addCommand({
			id: 'get-ip-geolocation',
			name: 'Get IP Geolocation',
			callback: () => this.getIPGeolocation()
		});

		// Hash Analysis
		this.addCommand({
			id: 'calculate-hash',
			name: 'Calculate Hash',
			callback: () => this.calculateHash()
		});

		// Shodan Search
		this.addCommand({
			id: 'shodan-search',
			name: 'Shodan Search',
			callback: () => this.shodanSearch()
		});

		// VirusTotal Scan
		this.addCommand({
			id: 'virustotal-scan',
			name: 'VirusTotal URL Scan',
			callback: () => this.virusTotalScan()
		});

		// Blue Team Tools
		this.addCommand({
			id: 'analyze-log',
			name: 'Analyze Log Entry',
			callback: () => this.analyzeLog()
		});

		this.addCommand({
			id: 'monitor-ports',
			name: 'Monitor Ports',
			callback: () => this.monitorPorts()
		});

		// Incident Response
		this.addCommand({
			id: 'create-incident-report',
			name: 'Create Incident Report',
			callback: () => this.createIncidentReport()
		});

		// Add settings tab
		this.addSettingTab(new OSINTSettingTab(this.app, this));

		// Start auto-processing if enabled
		if (this.settings.autoProcess) {
			this.startAutoProcessing();
		}

		new Notice('OSINT Plugin loaded');
	}

	onunload() {
		if (this.processingInterval) {
			window.clearInterval(this.processingInterval);
		}
		new Notice('OSINT Plugin unloaded');
	}

	async loadSettings() {
		this.settings = Object.assign({}, DEFAULT_SETTINGS, await this.loadData());
	}

	async saveSettings() {
		await this.saveData(this.settings);
	}

	async runOSINTAnalysis() {
		const activeFile = this.app.workspace.getActiveFile();
		if (!activeFile) {
			new Notice('No active file');
			return;
		}

		const content = await this.app.vault.read(activeFile);
		await this.sendToBackend({
			type: 'osint_analysis',
			file: activeFile.path,
			content: content,
			timestamp: Date.now()
		});

		new Notice('OSINT analysis queued');
	}

	async analyzeCurrentNote() {
		const activeFile = this.app.workspace.getActiveFile();
		if (!activeFile) {
			new Notice('No active file');
			return;
		}

		const content = await this.app.vault.read(activeFile);
		await this.sendToBackend({
			type: 'analyze',
			file: activeFile.path,
			content: content,
			timestamp: Date.now()
		});

		new Notice('Note analysis queued');
	}

	async startBackend() {
		await this.sendToBackend({
			type: 'start',
			timestamp: Date.now()
		});
		new Notice('Backend start signal sent');
	}

	async analyzeSocialMedia() {
		const activeFile = this.app.workspace.getActiveFile();
		if (!activeFile) {
			new Notice('No active file');
			return;
		}

		const content = await this.app.vault.read(activeFile);
		await this.sendToBackend({
			type: 'social_media',
			action: 'extract_profiles',
			content: content,
			timestamp: Date.now()
		});
		new Notice('Social media analysis queued');
	}

	async getIPGeolocation() {
		const ip = await this.app.vault.adapter.read(this.settings.sharedMemoryPath + '/temp_ip.txt').catch(() => '');
		if (!ip) {
			new Notice('Please add IP to shared-memory/temp_ip.txt first');
			return;
		}

		await this.sendToBackend({
			type: 'geolocation',
			action: 'get_geolocation',
			ip: ip.trim(),
			timestamp: Date.now()
		});
		new Notice('Geolocation lookup queued');
	}

	async calculateHash() {
		const activeFile = this.app.workspace.getActiveFile();
		if (!activeFile) {
			new Notice('No active file');
			return;
		}

		const content = await this.app.vault.read(activeFile);
		await this.sendToBackend({
			type: 'hash_analysis',
			action: 'calculate_string_hash',
			content: content,
			algorithm: 'sha256',
			timestamp: Date.now()
		});
		new Notice('Hash calculation queued');
	}

	async shodanSearch() {
		const query = await this.app.vault.adapter.read(this.settings.sharedMemoryPath + '/temp_query.txt').catch(() => '');
		if (!query) {
			new Notice('Please add search query to shared-memory/temp_query.txt first');
			return;
		}

		await this.sendToBackend({
			type: 'shodan_search',
			action: 'search',
			query: query.trim(),
			timestamp: Date.now()
		});
		new Notice('Shodan search queued');
	}

	async virusTotalScan() {
		const url = await this.app.vault.adapter.read(this.settings.sharedMemoryPath + '/temp_url.txt').catch(() => '');
		if (!url) {
			new Notice('Please add URL to shared-memory/temp_url.txt first');
			return;
		}

		await this.sendToBackend({
			type: 'virustotal_scan',
			action: 'scan_url',
			url: url.trim(),
			timestamp: Date.now()
		});
		new Notice('VirusTotal scan queued');
	}

	async analyzeLog() {
		const activeFile = this.app.workspace.getActiveFile();
		if (!activeFile) {
			new Notice('No active file');
			return;
		}

		const content = await this.app.vault.read(activeFile);
		const lines = content.split('\n');
		const firstLine = lines[0] || '';

		await this.sendToBackend({
			type: 'blue_team_monitor',
			action: 'analyze_log',
			log_line: firstLine,
			timestamp: Date.now()
		});
		new Notice('Log analysis queued');
	}

	async monitorPorts() {
		await this.sendToBackend({
			type: 'blue_team_monitor',
			action: 'monitor_ports',
			ports: [22, 80, 443, 8080, 3000],
			timestamp: Date.now()
		});
		new Notice('Port monitoring queued');
	}

	async createIncidentReport() {
		await this.sendToBackend({
			type: 'incident_response',
			action: 'create_report',
			incident_data: {
				severity: 'medium',
				type: 'security_incident',
				description: 'Manual incident report',
				affected_assets: [],
				indicators: [],
				actions_taken: []
			},
			timestamp: Date.now()
		});
		new Notice('Incident report creation queued');
	}

	private async sendToBackend(data: any) {
		try {
			const requestId = `request_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
			const requestPath = `${this.settings.sharedMemoryPath}/${requestId}.json`;

			// Write request to shared memory
			await this.app.vault.adapter.write(requestPath, JSON.stringify(data));

			// Wait for response
			this.waitForResponse(requestId);
		} catch (error) {
			new Notice(`Error sending to backend: ${error}`);
		}
	}

	private async waitForResponse(requestId: string) {
		const maxAttempts = 30;
		let attempts = 0;

		const checkInterval = setInterval(async () => {
			attempts++;
			const responsePath = `${this.settings.sharedMemoryPath}/${requestId}_response.json`;

			try {
				if (await this.app.vault.adapter.exists(responsePath)) {
					clearInterval(checkInterval);
					const responseContent = await this.app.vault.adapter.read(responsePath);
					const response = JSON.parse(responseContent);

					// Process response
					this.handleBackendResponse(response);

					// Clean up files
					await this.app.vault.adapter.remove(`${this.settings.sharedMemoryPath}/${requestId}.json`);
					await this.app.vault.adapter.remove(responsePath);
				} else if (attempts >= maxAttempts) {
					clearInterval(checkInterval);
					new Notice('Backend response timeout');
				}
			} catch (error) {
				clearInterval(checkInterval);
				new Notice(`Error checking response: ${error}`);
			}
		}, 1000);
	}

	private async handleBackendResponse(response: any) {
		if (response.type === 'osint_result') {
			// Insert results into current note
			const activeFile = this.app.workspace.getActiveFile();
			if (activeFile) {
				const content = await this.app.vault.read(activeFile);
				const resultsSection = `\n\n## OSINT Results\n\n${JSON.stringify(response.data, null, 2)}`;
				await this.app.vault.modify(activeFile, content + resultsSection);
				new Notice('OSINT results added to note');
			}
		} else if (response.type === 'analysis_result') {
			new Notice(`Analysis complete: ${response.summary}`);
		} else if (response.type === 'social_media_result') {
			const activeFile = this.app.workspace.getActiveFile();
			if (activeFile) {
				const content = await this.app.vault.read(activeFile);
				const resultsSection = `\n\n## Social Media Analysis\n\n${JSON.stringify(response.data, null, 2)}`;
				await this.app.vault.modify(activeFile, content + resultsSection);
				new Notice('Social media analysis added to note');
			}
		} else if (response.type === 'geolocation_result') {
			const activeFile = this.app.workspace.getActiveFile();
			if (activeFile) {
				const content = await this.app.vault.read(activeFile);
				const resultsSection = `\n\n## IP Geolocation\n\n${JSON.stringify(response.data, null, 2)}`;
				await this.app.vault.modify(activeFile, content + resultsSection);
				new Notice('Geolocation data added to note');
			}
		} else if (response.type === 'hash_analysis_result') {
			const activeFile = this.app.workspace.getActiveFile();
			if (activeFile) {
				const content = await this.app.vault.read(activeFile);
				const resultsSection = `\n\n## Hash Analysis\n\n${JSON.stringify(response.data, null, 2)}`;
				await this.app.vault.modify(activeFile, content + resultsSection);
				new Notice('Hash analysis added to note');
			}
		} else if (response.type === 'shodan_result') {
			const activeFile = this.app.workspace.getActiveFile();
			if (activeFile) {
				const content = await this.app.vault.read(activeFile);
				const resultsSection = `\n\n## Shodan Results\n\n${JSON.stringify(response.data, null, 2)}`;
				await this.app.vault.modify(activeFile, content + resultsSection);
				new Notice('Shodan results added to note');
			}
		} else if (response.type === 'virustotal_result') {
			const activeFile = this.app.workspace.getActiveFile();
			if (activeFile) {
				const content = await this.app.vault.read(activeFile);
				const resultsSection = `\n\n## VirusTotal Results\n\n${JSON.stringify(response.data, null, 2)}`;
				await this.app.vault.modify(activeFile, content + resultsSection);
				new Notice('VirusTotal results added to note');
			}
		} else if (response.type === 'blue_team_result') {
			const activeFile = this.app.workspace.getActiveFile();
			if (activeFile) {
				const content = await this.app.vault.read(activeFile);
				const resultsSection = `\n\n## Blue Team Analysis\n\n${JSON.stringify(response.data, null, 2)}`;
				await this.app.vault.modify(activeFile, content + resultsSection);
				new Notice('Blue team analysis added to note');
			}
		} else if (response.type === 'log_analysis_result') {
			const activeFile = this.app.workspace.getActiveFile();
			if (activeFile) {
				const content = await this.app.vault.read(activeFile);
				const resultsSection = `\n\n## Log Analysis\n\n${JSON.stringify(response.data, null, 2)}`;
				await this.app.vault.modify(activeFile, content + resultsSection);
				new Notice('Log analysis added to note');
			}
		} else if (response.type === 'incident_response_result') {
			const activeFile = this.app.workspace.getActiveFile();
			if (activeFile) {
				const content = await this.app.vault.read(activeFile);
				const resultsSection = `\n\n## Incident Response\n\n${JSON.stringify(response.data, null, 2)}`;
				await this.app.vault.modify(activeFile, content + resultsSection);
				new Notice('Incident response data added to note');
			}
		} else if (response.type === 'network_recon_result') {
			const activeFile = this.app.workspace.getActiveFile();
			if (activeFile) {
				const content = await this.app.vault.read(activeFile);
				const resultsSection = `\n\n## Network Reconnaissance\n\n${JSON.stringify(response.data, null, 2)}\n\n**Warning**: ${response.warning}`;
				await this.app.vault.modify(activeFile, content + resultsSection);
				new Notice('Network recon results added to note');
			}
		} else if (response.type === 'vuln_scan_result') {
			const activeFile = this.app.workspace.getActiveFile();
			if (activeFile) {
				const content = await this.app.vault.read(activeFile);
				const resultsSection = `\n\n## Vulnerability Scan\n\n${JSON.stringify(response.data, null, 2)}\n\n**Warning**: ${response.warning}`;
				await this.app.vault.modify(activeFile, content + resultsSection);
				new Notice('Vulnerability scan results added to note');
			}
		} else if (response.type === 'threat_intel_result') {
			const activeFile = this.app.workspace.getActiveFile();
			if (activeFile) {
				const content = await this.app.vault.read(activeFile);
				const resultsSection = `\n\n## Threat Intelligence\n\n${JSON.stringify(response.data, null, 2)}`;
				await this.app.vault.modify(activeFile, content + resultsSection);
				new Notice('Threat intel data added to note');
			}
		}
	}

	public startAutoProcessing() {
		this.processingInterval = window.setInterval(async () => {
			// Check for pending results from backend
			const files = await this.app.vault.adapter.list(this.settings.sharedMemoryPath);
			for (const file of files.files) {
				if (file.endsWith('_response.json')) {
					const content = await this.app.vault.adapter.read(file);
					const response = JSON.parse(content);
					await this.handleBackendResponse(response);
				}
			}
		}, 5000);
	}
}

class OSINTSettingTab extends PluginSettingTab {
	plugin: OSINTPlugin;

	constructor(app: App, plugin: OSINTPlugin) {
		super(app, plugin);
		this.plugin = plugin;
	}

	display(): void {
		const { containerEl } = this;

		containerEl.empty();

		containerEl.createEl('h2', { text: 'OSINT Plugin Settings' });

		new Setting(containerEl)
			.setName('Backend Path')
			.setDesc('Path to Python backend directory')
			.addText(text => text
				.setPlaceholder('../backend')
				.setValue(this.plugin.settings.backendPath)
				.onChange(async (value) => {
					this.plugin.settings.backendPath = value;
					await this.plugin.saveSettings();
				}));

		new Setting(containerEl)
			.setName('Shared Memory Path')
			.setDesc('Path for local file communication')
			.addText(text => text
				.setPlaceholder('../shared-memory')
				.setValue(this.plugin.settings.sharedMemoryPath)
				.onChange(async (value) => {
					this.plugin.settings.sharedMemoryPath = value;
					await this.plugin.saveSettings();
				}));

		new Setting(containerEl)
			.setName('Auto Process')
			.setDesc('Automatically process backend responses')
			.addToggle(toggle => toggle
				.setValue(this.plugin.settings.autoProcess)
				.onChange(async (value) => {
					this.plugin.settings.autoProcess = value;
					await this.plugin.saveSettings();
					if (value) {
						this.plugin.startAutoProcessing();
					} else if (this.plugin.processingInterval) {
						window.clearInterval(this.plugin.processingInterval);
					}
				}));
	}
}
