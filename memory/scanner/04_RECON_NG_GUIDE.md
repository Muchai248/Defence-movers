# Recon-ng - OSINT Framework Guide

## What is Recon-ng?

Recon-ng is a full-featured Open Source Intelligence (OSINT) framework that automates the process of gathering information from public sources. It helps with:
- Domain reconnaissance
- Email discovery
- Social media information gathering
- Public data analysis

## Installation

```bash
sudo apt install recon-ng
```

## Basic Usage

### Start Recon-ng

```bash
recon-ng
```

### Interactive Mode

Once in Recon-ng, you can use modules to gather information:

```bash
# List available modules
modules search

# Load a module
modules import recon/domains-hosts/hackertarget

# Set options
options set DOMAIN example.com

# Run the module
run
```

## Educational Example

```bash
# Start recon-ng
recon-ng

# Load a domain reconnaissance module
modules import recon/domains-hosts/bing_domain_web

# Set your target domain
options set DOMAIN example.com

# Run the module
run

# Output explanation:
# - Returns subdomains discovered for the target domain
# - Uses public search engines (Bing)
# - Only gathers publicly available information
```

## Legal Note
- ✅ Gather publicly available information
- ✅ Research domains you own or have authorization to investigate
- ✅ Educational OSINT research
- ❌ Use for targeted harassment = Illegal
- ❌ Use for stalking = Illegal
- ❌ Gather private/non-public information = Illegal

## Common Commands Reference

```bash
# Start the framework
recon-ng

# List all modules
modules list

# Search for specific modules
modules search <keyword>

# Load a module
modules import <module_path>

# View module options
options list

# Set an option
options set <OPTION> <value>

# Run the module
run

# Exit
exit
```

## Popular Modules

```bash
# Domain reconnaissance
recon/domains-hosts/bing_domain_web
recon/domains-hosts/google_site_web

# Email discovery
recon/contacts-gather/http/web/contacts_search

# Social media
recon/contacts-credentials/haveibeenpwned

# DNS information
recon/domains-hosts/hackertarget
```

## What Recon-ng Cannot Do
- Does not access private information
- Does not hack into systems
- Only uses public APIs and search engines
- Gathers information that is already publicly available

## Safety Tips
1. Only gather information about domains you own or have authorization
2. Respect privacy and terms of service
3. Use findings for legitimate security research
4. Don't use for harassment or stalking
