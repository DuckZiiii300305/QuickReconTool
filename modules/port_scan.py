from core.executor import run_command

def run_nmap(target, mode):
    if mode == "quick":
        cmd = f"nmap -F {target}"
    else:
        cmd = f"nmap -sC -sV -O {target}"

    output = run_command(cmd)
    return output.splitlines()