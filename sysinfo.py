#!/usr/bin/env python3
"""sysinfo - show basic system information on Linux/Ubuntu."""
import argparse
import os
import platform
import shutil


def get_memory():
    """Return (total_gb, available_gb) read from /proc/meminfo."""
    info = {}
    with open("/proc/meminfo") as f:
        for line in f:
            key, value = line.split(":")
            info[key] = int(value.split()[0])  # values are in kB
    return info["MemTotal"] / 1024 / 1024, info["MemAvailable"] / 1024 / 1024


def get_uptime():
    """Return (hours, minutes) read from /proc/uptime."""
    with open("/proc/uptime") as f:
        seconds = int(float(f.read().split()[0]))
    return seconds // 3600, (seconds % 3600) // 60


def main():
    parser = argparse.ArgumentParser(description="Show basic Linux system information")
    parser.add_argument("--path", default="/", help="disk path to check (default: /)")
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"Error: path '{args.path}' does not exist")
        return 1

    total, free_mem = get_memory()
    disk = shutil.disk_usage(args.path)
    hours, minutes = get_uptime()

    print(f"OS      : {platform.system()} {platform.release()}")
    print(f"CPU     : {os.cpu_count()} cores")
    print(f"Memory  : {free_mem:.1f} GB free of {total:.1f} GB")
    print(f"Disk    : {disk.free / 1e9:.1f} GB free of {disk.total / 1e9:.1f} GB ({args.path})")
    print(f"Uptime  : {hours}h {minutes}m")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
