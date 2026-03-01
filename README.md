# QuickReconTool - Quick Reconnaissance Tool

This is a CLI-based automated reconnaissance tool designed for Kali Linux.

## Features

- Asset Enumeration (Amass)
- Live Host Detection (httpx)
- Port Scanning (Nmap)
- Directory Brute-force (ffuf)
- Vulnerability Scan (Nuclei)
- HTML Report Generation

## Installation

```bash
git clone https://github.com/DuckZiiii300305/QuickReconTool.git
cd QuickReconTool
chmod +x install.sh
./install.sh
```

## Usage

### Single target

```bash
python3 main.py -t example.com
```

### Multiple targets

```bash
python3 main.py -f targets.txt
```

### Deep scan

```bash
python3 main.py -t example.com --mode deep
```

## Output

Results will be saved under:

```
results/<target>/
```

Includes:

- `report.json`
- `report.html`
