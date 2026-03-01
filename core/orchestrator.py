import os
import json
from modules.asset_enum import run_amass
from modules.live_hosts import run_httpx
from modules.port_scan import run_nmap
from modules.content_discovery import run_ffuf
from modules.vuln_scan import run_nuclei
from report.report_generator import generate_report

class Orchestrator:

    def __init__(self, mode="quick"):
        self.mode = mode

    def run(self, targets):
        for target in targets:
            print(f"[+] Scanning {target}")

            os.makedirs(f"results/{target}", exist_ok=True)

            data = {}
            data["target"] = target
            data["assets"] = run_amass(target, self.mode)
            data["live_hosts"] = run_httpx(target)
            data["ports"] = run_nmap(target, self.mode)
            data["directories"] = run_ffuf(target)
            data["vulnerabilities"] = run_nuclei(target)

            with open(f"results/{target}/report.json", "w") as f:
                json.dump(data, f, indent=4)

            generate_report(target, data)

            print(f"[+] Finished {target}")