import socket

def choice():
    c = eval(input('\nDo you want to scan:\n 1- One ip address\n 2- A range of ip addresses\n 3- Distinct multiple ip addresses\n'))
    return c

def scan_ports(ip, ports):
    for port in ports:
        if port in [n for n in range(1,65536)]:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} is OPEN.")
            sock.close()
        else: print(f"{port} is not a valid port number.")
        
def fct():
    ip_addr = input('\nEnter the ip address: ')
    n = choice()
    if n == 1:
        port_1 = eval(input('\nEnter the port number: '))
        scan_ports(ip_addr, [port_1])
    elif n == 2:
        port_1 = eval(input('\nEnter the first port number: '))
        port_2 = eval(input('Enter the last port number: '))
        scan_ports(ip_addr, [n for n in range(port_1, port_2+1)])
    elif n == 3:
        L = []
        while True:
            r = input('Enter a port number (or the letter "f" to finish): ')
            if r == 'f':
                break
            else: L.append(eval(r))
        scan_ports(ip_addr, L)
    print(f'Scanning ports on {ip_addr} is complete')

fct()
