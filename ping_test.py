#!/usr/bin/env python3

import argparse
import re
import subprocess
import sys


AVERAGE_RTT_PATTERN = re.compile(
    r"(?:round-trip|rtt) min/avg/max/(?:stddev|mdev) = [^/]+/([^/]+)/"
)


def ping_host(host):
    try:
        result = subprocess.run(
            ["ping", "-c", "4", host],
            capture_output=True,
            text=True,
            timeout=15,
        )
    except subprocess.TimeoutExpired:
        print(f"{host}: unreachable (ping timed out)")
        return False
    except OSError as error:
        print(f"{host}: unable to run ping ({error})")
        return False

    output = f"{result.stdout}\n{result.stderr}"

    if result.returncode != 0:
        print(f"{host}: unreachable or no response")
        return False

    match = AVERAGE_RTT_PATTERN.search(output)
    if not match:
        print(f"{host}: ping completed, but average round-trip time was not found")
        return False

    print(f"{host}: average round-trip time {match.group(1)} ms")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Ping one or more hosts and report average round-trip time."
    )
    parser.add_argument("hosts", nargs="+", help="Hostnames or IP addresses to ping")
    args = parser.parse_args()

    failures = 0
    for host in args.hosts:
        if not ping_host(host):
            failures += 1

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
