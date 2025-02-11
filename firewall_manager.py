import os
import subprocess

def run_command(command):
    """Execute a shell command and return the output."""
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return result.decode("utf-8")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.output.decode('utf-8')}")
        return None

def list_rules():
    """List all iptables rules."""
    print("Listing current iptables rules...")
    rules = run_command("iptables -L -v -n")
    if rules:
        print(rules)

def add_rule(protocol, port, action):
    """Add a firewall rule for a specific protocol and port."""
    command = f"iptables -A INPUT -p {protocol} --dport {port} -j {action}"
    print(f"Adding rule: {command}")
    run_command(command)

def delete_rule(protocol, port):
    """Delete a firewall rule for a specific protocol and port."""
    command = f"iptables -D INPUT -p {protocol} --dport {port} -j ACCEPT"
    print(f"Deleting rule: {command}")
    run_command(command)

def main():
    """Main menu for the firewall manager."""
    while True:
        print("\nFirewall Rule Manager")
        print("1. List Rules")
        print("2. Add Rule")
        print("3. Delete Rule")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_rules()
        elif choice == "2":
            protocol = input("Enter protocol (tcp/udp): ")
            port = input("Enter port number: ")
            action = input("Enter action (ACCEPT/DROP): ")
            add_rule(protocol, port, action)
        elif choice == "3":
            protocol = input("Enter protocol (tcp/udp): ")
            port = input("Enter port number: ")
            delete_rule(protocol, port)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
