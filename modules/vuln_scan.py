from core.executor import run_command

def run_nuclei(target):
    cmd = f"nuclei -u {target} -severity medium,high"
    output = run_command(cmd)
    return output.splitlines()