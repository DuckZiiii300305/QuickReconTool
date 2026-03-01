#!/bin/bash

echo "[*] Updating system..."
sudo apt update

echo "[*] Installing required tools..."
sudo apt install -y amass ffuf nmap whatweb nuclei

echo "[*] Installing Python dependencies..."
pip3 install -r requirements.txt

echo "[+] Installation completed."