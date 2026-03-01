from core.executor import run_command

def run_httpx(target):
    cmd = f"echo {target} | httpx -silent -status-code -title"
    output = run_command(cmd)
    return output.splitlines()