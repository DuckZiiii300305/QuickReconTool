from core.executor import run_command

def run_ffuf(target):
    cmd = f"ffuf -u http://{target}/FUZZ -w /usr/share/wordlists/dirb/common.txt -mc 200,301,302 -of csv"
    output = run_command(cmd)
    return output.splitlines()