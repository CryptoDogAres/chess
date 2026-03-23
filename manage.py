#!/usr/bin/env python3
"""
ChessDAO Project Manager
Usage:
    python3 manage.py setup     — Install engine + verify all tools
    python3 manage.py serve     — Start Pikafish engine server
    python3 manage.py analyze   — Run batch analysis on all positions
    python3 manage.py status    — Show project status and progress
    python3 manage.py open      — Open dashboard in browser
    python3 manage.py export    — Export all plans as JSON
"""
import argparse
import json
import os
import subprocess
import sys
import webbrowser
from pathlib import Path

ROOT = Path(__file__).parent
ENGINE_DIR = ROOT / "engine"
PLANS_DIR = ROOT / "plans"
CONTENT_DIR = ROOT / "content"

# Colors
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
RESET = "\033[0m"
BOLD = "\033[1m"

def info(msg): print(f"{BLUE}[棋]{RESET}  {msg}")
def ok(msg):   print(f"{GREEN}[✓]{RESET}  {msg}")
def warn(msg): print(f"{YELLOW}[!]{RESET}  {msg}")
def fail(msg): print(f"{RED}[✗]{RESET}  {msg}")


def cmd_setup(args):
    """Install engine and verify all tools."""
    info("Running setup...")
    setup_script = ROOT / "setup.sh"
    if setup_script.exists():
        subprocess.run(["bash", str(setup_script)], cwd=str(ROOT))
    else:
        fail("setup.sh not found")
        sys.exit(1)


def cmd_serve(args):
    """Start the Pikafish engine server."""
    server = ENGINE_DIR / "server.py"
    if not server.exists():
        fail("engine/server.py not found")
        sys.exit(1)

    port = args.port or 8080
    threads = args.threads or 4
    hash_mb = args.hash or 256

    info(f"Starting Pikafish server on port {port} (threads={threads}, hash={hash_mb}MB)")
    try:
        subprocess.run(
            [sys.executable, str(server),
             "--port", str(port),
             "--threads", str(threads),
             "--hash", str(hash_mb)],
            cwd=str(ENGINE_DIR)
        )
    except KeyboardInterrupt:
        info("Server stopped.")


def cmd_analyze(args):
    """Run batch analysis on position files."""
    analyzer = ENGINE_DIR / "analyze.py"
    if not analyzer.exists():
        fail("engine/analyze.py not found")
        sys.exit(1)

    # Collect all position files
    pos_files = list((CONTENT_DIR / "positions").glob("*.txt"))
    pos_files.append(ENGINE_DIR / "positions.txt")
    pos_files = [f for f in pos_files if f.exists()]

    depth = args.depth or 14
    output = ROOT / "engine" / "full-analysis.json"

    info(f"Analyzing {len(pos_files)} position files at depth {depth}...")

    all_results = []
    for pf in pos_files:
        info(f"  Analyzing {pf.name}...")
        result = subprocess.run(
            [sys.executable, str(analyzer),
             "--file", str(pf),
             "--depth", str(depth),
             "--output", "/dev/stdout"],
            cwd=str(ENGINE_DIR),
            capture_output=True, text=True
        )
        if result.returncode == 0 and result.stdout.strip():
            try:
                data = json.loads(result.stdout)
                all_results.extend(data if isinstance(data, list) else [data])
            except json.JSONDecodeError:
                warn(f"  Could not parse results from {pf.name}")
        else:
            warn(f"  Analysis failed for {pf.name}")
            if result.stderr:
                print(f"    {result.stderr[:200]}")

    with open(output, "w") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    ok(f"Analysis complete: {len(all_results)} positions → {output}")


def cmd_status(args):
    """Show project status and task progress."""
    print()
    print(f"  {BOLD}棋道 ChessDAO — Project Status{RESET}")
    print(f"  {'=' * 40}")
    print()

    # Count files
    html_files = list(ROOT.glob("*.html"))
    overlay_files = list((ROOT / "overlays").glob("*.html"))
    content_files = list(CONTENT_DIR.rglob("*.md")) + list(CONTENT_DIR.rglob("*.txt"))
    position_count = 0
    for pf in list((CONTENT_DIR / "positions").glob("*.txt")) + [ENGINE_DIR / "positions.txt"]:
        if pf.exists():
            with open(pf) as f:
                position_count += sum(1 for line in f if line.strip() and not line.startswith("#"))

    print(f"  {BLUE}Files:{RESET}")
    print(f"    HTML tools:      {len(html_files)}")
    print(f"    OBS overlays:    {len(overlay_files)}")
    print(f"    Content files:   {len(content_files)}")
    print(f"    Positions:       {position_count}")
    print()

    # Check engine
    engine_bin = ENGINE_DIR / "pikafish"
    print(f"  {BLUE}Engine:{RESET}")
    if engine_bin.exists():
        ok("Pikafish binary installed")
    else:
        warn("Pikafish not installed — run: python3 manage.py setup")

    # Check apps
    print(f"\n  {BLUE}Apps:{RESET}")
    for app, name in [("/Applications/OBS.app", "OBS Studio"),
                       ("/Applications/CapCut.app", "CapCut"),
                       ("/Applications/Shotcut.app", "Shotcut")]:
        if os.path.isdir(app):
            ok(f"{name} installed")
        else:
            warn(f"{name} not installed")

    # Plan progress
    print(f"\n  {BLUE}Plan Progress:{RESET}")
    total_done = total_all = complete_plans = 0
    for pf in sorted(PLANS_DIR.rglob("*.json")):
        with open(pf) as f:
            plan = json.load(f)
        done = sum(1 for t in plan["tasks"] if t.get("done"))
        total = len(plan["tasks"])
        total_done += done
        total_all += total
        if done == total:
            complete_plans += 1
            mark = f"{GREEN}✅{RESET}"
        else:
            mark = f"{YELLOW}🔄{RESET}"
        pct = round(done / total * 100) if total else 0
        print(f"    {mark} {plan['title']}: {done}/{total} ({pct}%)")

    pct = round(total_done / total_all * 100) if total_all else 0
    print()
    print(f"  {BOLD}📊 Total: {total_done}/{total_all} tasks ({pct}%) | {complete_plans}/13 plans complete{RESET}")
    print(f"  🔲 Remaining: {total_all - total_done} tasks")
    print()


def cmd_open(args):
    """Open dashboard in browser."""
    target = args.file or "index.html"
    filepath = ROOT / target
    if filepath.exists():
        info(f"Opening {target}...")
        webbrowser.open(f"file://{filepath}")
    else:
        fail(f"{target} not found")


def cmd_export(args):
    """Export all plans as a single JSON file."""
    plans = []
    for pf in sorted(PLANS_DIR.rglob("*.json")):
        with open(pf) as f:
            plans.append(json.load(f))
    output = ROOT / "plans-export.json"
    with open(output, "w") as f:
        json.dump(plans, f, indent=2, ensure_ascii=False)
    ok(f"Exported {len(plans)} plans to {output}")


def main():
    parser = argparse.ArgumentParser(
        description="棋道 ChessDAO Project Manager",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("setup", help="Install engine + verify tools")

    serve_p = sub.add_parser("serve", help="Start engine server")
    serve_p.add_argument("--port", type=int, default=8080)
    serve_p.add_argument("--threads", type=int, default=4)
    serve_p.add_argument("--hash", type=int, default=256)

    analyze_p = sub.add_parser("analyze", help="Batch analyze positions")
    analyze_p.add_argument("--depth", type=int, default=14)

    sub.add_parser("status", help="Show project status")

    open_p = sub.add_parser("open", help="Open in browser")
    open_p.add_argument("file", nargs="?", default="index.html")

    sub.add_parser("export", help="Export plans as JSON")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return

    cmds = {
        "setup": cmd_setup,
        "serve": cmd_serve,
        "analyze": cmd_analyze,
        "status": cmd_status,
        "open": cmd_open,
        "export": cmd_export,
    }
    cmds[args.command](args)


if __name__ == "__main__":
    main()
