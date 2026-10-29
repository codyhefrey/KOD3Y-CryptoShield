#!/usr/bin/env python3
"""Read-only cryptojacking triage utility. Python 3.10+."""
import argparse
import datetime as dt
import json
import subprocess
from pathlib import Path

try:
    import psutil
except ImportError:
    psutil = None

def processes(threshold):
    if psutil is None:
        return {"error": "Install psutil: python -m pip install -r requirements.txt", "items": []}
    items = []
    for proc in psutil.process_iter(["pid", "name", "exe"]):
        try:
            cpu = proc.cpu_percent(interval=0.1)
            if cpu >= threshold:
                items.append({"pid": proc.pid, "name": proc.info["name"], "cpu_percent": cpu, "exe": proc.info["exe"]})
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return {"items": sorted(items, key=lambda p: p["cpu_percent"], reverse=True)}

def docker_containers():
    try:
        p = subprocess.run(["docker", "ps", "--format", "{{json .}}"], capture_output=True, text=True, timeout=8, check=False)
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        return {"available": False, "error": type(e).__name__, "items": []}
    if p.returncode:
        return {"available": False, "error": p.stderr.strip()[:300], "items": []}
    items = []
    for line in p.stdout.splitlines():
        try:
            items.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    return {"available": True, "items": items}

def collect(threshold=50):
    return {"timestamp_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "note": "High CPU and Docker presence are investigation leads, not proof of cryptojacking.",
            "processes": processes(threshold), "docker": docker_containers()}

def main():
    parser = argparse.ArgumentParser(description="Read-only cryptojacking investigation")
    parser.add_argument("--cpu-threshold", type=float, default=50)
    parser.add_argument("--output", default="cryptoshield-report.json")
    args = parser.parse_args()
    if not 0 <= args.cpu_threshold <= 100:
        parser.error("--cpu-threshold must be between 0 and 100")
    report = collect(args.cpu_threshold)
    Path(args.output).write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Saved report to {args.output}. No processes were terminated.")

if __name__ == "__main__":
    main()
