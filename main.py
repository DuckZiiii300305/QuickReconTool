import argparse
from core.orchestrator import Orchestrator
from core.target_loader import load_targets

def main():
    parser = argparse.ArgumentParser(description="Kali Recon X (krx)")
    parser.add_argument("-t", "--target", help="Single target")
    parser.add_argument("-f", "--file", help="File containing targets")
    parser.add_argument("--mode", choices=["quick", "deep"], default="quick")

    args = parser.parse_args()

    targets = load_targets(args.target, args.file)

    orchestrator = Orchestrator(mode=args.mode)
    orchestrator.run(targets)

if __name__ == "__main__":
    main()