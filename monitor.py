"""Local continuous monitor: periodic read-only snapshots and alerts."""
import argparse
import datetime as dt
import json
import time
from pathlib import Path
from cryptoshield import collect

def assess(report, threshold=80):
    alerts = []
    for item in report.get("processes", {}).get("items", []):
        if item.get("cpu_percent", 0) >= threshold:
            alerts.append({"type": "high_cpu", "pid": item["pid"], "name": item.get("name"), "cpu_percent": item["cpu_percent"], "severity": "investigate"})
    return alerts

def main():
    parser = argparse.ArgumentParser(description="Local, read-only CryptoShield monitor")
    parser.add_argument("--interval", type=float, default=30)
    parser.add_argument("--samples", type=int, default=10, help="Number of snapshots, 0 means until Ctrl+C")
    parser.add_argument("--threshold", type=float, default=80)
    parser.add_argument("--output", default="cryptoshield-monitor.jsonl")
    args = parser.parse_args()
    if args.interval < 1 or args.samples < 0 or not 0 <= args.threshold <= 100:
        parser.error("interval must be >=1, samples >=0, threshold between 0 and 100")
    count = 0
    try:
        while args.samples == 0 or count < args.samples:
            report = collect(args.threshold)
            entry = {"timestamp_utc": dt.datetime.now(dt.timezone.utc).isoformat(), "alerts": assess(report, args.threshold), "snapshot": report}
            with Path(args.output).open("a", encoding="utf-8") as out:
                out.write(json.dumps(entry) + "\n")
            print(f"Snapshot {count + 1}: {len(entry['alerts'])} investigation alerts")
            count += 1
            if args.samples == 0 or count < args.samples:
                time.sleep(args.interval)
    except KeyboardInterrupt:
        print("Monitoring stopped. No processes were modified.")

if __name__ == "__main__":
    main()
