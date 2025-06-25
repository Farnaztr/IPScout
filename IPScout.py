import socket
import subprocess
ports={
    21: "File transfer (FTP)",
    22: "Secure remote login(SSH)",
    25: "Email sending(SMTP)",
    53:"Domain Name System(DNS)",
    80:"Regular web server(HTTP)",
    443:"Secure web server(HTTPS)",
    110:"Old email receiving(POP3)",
    143:"Modern email receiving(IMAP)",
    3306:"MySQL database access",
    3389:"Windowa remote desktop(RDP)"
}
ip_input=input("Enter the local IP Address:").strip()
print("\nChecking...\n")

device_check=subprocess.run(["ping","-n","2",ip_input],stderr=subprocess.PIPE,stdout=subprocess.PIPE)
if device_check.returncode==0:
    print("Devie is +Online+")
else:
    print("Device is -Offline-")
try:
        Host=socket.gethostbyaddr(ip_input)[0]
        print(f"Hostname:{Host}")
except socket.herror:
     print("\n!We couldn't find the Hostname!")
print("\n\nport Status...\n")
for number_port, desc in ports.items():
     sockets=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     sockets.settimeout(4)
     result=sockets.connect_ex((ip_input,number_port))
     open_close="+Open+" if result==0 else "-Closed-"
     print(f"port {number_port}: {open_close} - {desc}")
     sockets.close()