# Network Analysis Lab

## Objective

Experiment with basic network analysis techniques and document how systems communicate, respond, and behave across a network.

## Overview

This project focuses on beginner-to-intermediate network analysis. It starts with simple latency testing and can expand into packet capture, service discovery, and deeper troubleshooting workflows.

## Prerequisites

- Python 3.x
- A terminal with access to the `ping` command
- Permission to test the hosts or networks being analyzed

## Usage

Run `ping_test.py` with one or more hostnames or IP addresses:

```bash
python3 ping_test.py example.com 8.8.8.8
```

The script sends four ping requests to each host and prints the average round-trip time when available. If a host is unreachable or the command fails, the script prints a basic error message and continues checking the remaining hosts.

## Actions Taken

- Created a Python-based ping test utility
- Added basic unreachable-host handling
- Documented prerequisites and usage
- Preserved the project focus on practical network behavior analysis

## Key Takeaways

- Latency testing helps show how quickly a host responds
- Simple command-line tools can provide useful network troubleshooting signals
- Clear documentation makes repeated tests easier to run and compare

## Next Steps

- Add packet capture examples
- Explore more advanced latency analysis
- Store test results in structured logs
- Add safer examples for local-only network testing
