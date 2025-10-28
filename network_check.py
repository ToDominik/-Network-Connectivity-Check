import argparse
import subprocess
import socket
from datetime import datetime

DEFAULT_HOST = "8.8.8.8"
DEFAULT_PORT = 53
log_file = "network_log.txt"

def log(message):
    with open(log_file, "a") as f:
        f.write(f"{datetime.now()} - {message}\n")
    print(message)

def ping_test(host):
    result = subprocess.run(["ping", "-n", "1", host], capture_output=True)
    if result.returncode == 0:
        log(f"Ping to {host} successful")
    else:
        log(f"Ping to {host} failed")

def port_test(host, port):
    s = socket.socket()
    s.settimeout(3)
    try:
        s.connect((host, port))
        log(f"Port {port} on {host} is open")
    except:
        log(f"Port {port} on {host} is closed")
    finally:
        s.close()

parser = argparse.ArgumentParser(description="Network Connectivity Checker")
parser.add_argument("-host", type=str, help="Host to test")
parser.add_argument("-port", type=int, help="Port to test")

args = parser.parse_args()

host = args.host if args.host else DEFAULT_HOST
port = args.port if args.port else DEFAULT_PORT

ping_test(host)
port_test(host, port)