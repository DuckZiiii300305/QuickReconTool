from core.executor import run_command

def run_amass(domain, mode):
    if mode == "quick":
        cmd = f"amass enum -passive -d {domain}"
    else:
        cmd = f"amass enum -active -brute -d {domain}"

    output = run_command(cmd)
    subdomains = list(set(output.splitlines()))
    return subdomains