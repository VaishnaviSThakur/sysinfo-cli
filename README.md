# sysinfo-cli

A small Python command line tool that shows basic system information on Linux and Ubuntu.

## What it shows
- Operating system and kernel version
- Number of CPU cores
- Free and total memory (read from /proc/meminfo)
- Free and total disk space
- System uptime (read from /proc/uptime)

## Requirements
- Python 3
- Linux or Ubuntu (it reads files from /proc)

## Usage
python3 sysinfo.py
python3 sysinfo.py --path /home

## Example output
OS      : Linux 6.8.0
CPU     : 4 cores
Memory  : 5.2 GB free of 7.7 GB
Disk    : 120.4 GB free of 250.0 GB (/)
Uptime  : 3h 25m

## Why I built it
I built this project to learn how Linux exposes system information and to practise Python, Git and GitHub.

## Future ideas
- Show CPU usage
- Add colour output
- Add JSON output
