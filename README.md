# Firewall Rule Manager (Linux `iptables`)

This project provides a Python-based command-line tool to manage `iptables` firewall rules on Linux. It allows you to list, add, and delete rules easily.

## Features
- List all current `iptables` rules.
- Add a new firewall rule for a specific protocol and port.
- Delete a firewall rule by specifying protocol and port.
- Supports `tcp` and `udp` protocols.

## Prerequisites
- Python 3.x
- Linux system with `iptables` installed and configured.
- Root privileges (required to modify `iptables` rules).

## Setup and Usage

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Haeshita3942/firewall-rules-manager.git
   cd firewall-rules-manager
