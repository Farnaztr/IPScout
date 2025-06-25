import socket
import subprocess

ports = {
    21: "File Transfer Protocol (FTP)",
    22: "Secure Shell (SSH)",
    25: "Simple Mail Transfer Protocol (SMTP)",
    53: "Domain Name System (DNS)",
    80: "Hypertext Transfer Protocol (HTTP)",
    110: "Post Office Protocol v3 (POP3)",
    143: "Internet Message Access Protocol (IMAP)",
    443: "Hypertext Transfer Protocol Secure (HTTPS)",
    3306: "MySQL Database",
    3389: "Windows Remote Desktop (RDP)"
}

ip_input = input("Enter the local IP Address: ").strip()
print("\nChecking connectivity...\n")

device_check = subprocess.run(["ping", "-n", "2", ip_input], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
if device_check.returncode == 0:
    print("Device is ONLINE ✅")
else:
    print("Device is OFFLINE ❌")

try:
    host = socket.gethostbyaddr(ip_input)[0]
    print(f"Hostname: {host}")
except socket.herror:
    print("Hostname could not be resolved!")

print("\nPort Status Check:\n")
for port_number, description in ports.items():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    result = sock.connect_ex((ip_input, port_number))
    status = "Open" if result == 0 else "Closed"
    print(f"Port {port_number}: {status} - {description}")
    sock.close()
