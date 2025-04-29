import socket

def choice():
    c = eval(input('Do you want to scan:\n 1- One ip address\n 2- A range of ip addresses\n 3- Distinct multiple ip addresses'))
    return c
def scan_ports(ip, ports):
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        sock.close()
        
def fct(n):
    ip_addr = input('Enter the ip address: ')
    if n == 1:
        ip_addr = input('Enter the port number: ')
        scan_ports(ip_addr,)
    elif n == 2:
        port_1 = input('Enter the first port number: ')
        port_2 = input('Enter the last port number: ')
        scan_ports(ip_addr, [n for n in range(port_1, port_2)])
        

# Example usage:
ip = "127.0.0.1"
common_ports = [n for n in range(1024)]
scan_ports(ip, common_ports)