# -Network-Connectivity-Check

## Description
Automated network connectivity checker (Python & PowerShell) designed to reduce manual troubleshooting by performing ping and port availability tests and saving results to log files for quick analysis.

## Features

Ping test (host reachability)

TCP port availability check

Log results to network_log.txt

Support for custom host and port

## Usage

PowerShell
``` 
# Default (8.8.8.8:53) 
./network_check.ps1

# Custom target 
./network_check.ps1 -Target 1.1.1.1 -Port 443 
```

Python
```
# Default (8.8.8.8:53) 
python network_check.py 

# Custom target 
python network_check.py -host 1.1.1.1 -port 443 
```
