import socket

def choice(n):
    c = eval(input('Do you want to scan '))

def scan_ports(ip, ports):
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        sock.close()

# Example usage:
ip = "127.0.0.1"
common_ports = [n for n in range(1024)]
scan_ports(ip, common_ports)