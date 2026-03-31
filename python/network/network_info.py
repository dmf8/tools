#!/usr/bin/env python3
import argparse
import socket
import subprocess
import re


def check_internet(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.close()
        return True
    except (socket.timeout, socket.error):
        return False


def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return None


def get_mac_address():
    try:
        output = subprocess.check_output(["ip", "link", "show"]).decode()
        mac = re.search(r'link/ether ([0-9a-f:]+)', output)
        if mac:
            return mac.group(1)
        return None
    except Exception:
        return None


def main():
    parser = argparse.ArgumentParser(description="Network information tool")
    parser.add_argument("-i", "--internet", action="store_true", help="Check internet connectivity")
    parser.add_argument("-l", "--local-ip", action="store_true", help="Get local IP address")
    parser.add_argument("-m", "--mac", action="store_true", help="Get MAC address")
    parser.add_argument("-t", "--test")

    args = parser.parse_args()

    if not any([args.internet, args.local_ip, args.mac]):
        parser.print_help()
        return

    if args.internet:
        connected = check_internet()
        print(f"Internet: {'Connected' if connected else 'Disconnected'}")

    if args.local_ip:
        ip = get_local_ip()
        print(f"Local IP: {ip if ip else 'Unknown'}")

    if args.mac:
        mac = get_mac_address()
        print(f"MAC Address: {mac if mac else 'Unknown'}")


if __name__ == "__main__":
    main()
