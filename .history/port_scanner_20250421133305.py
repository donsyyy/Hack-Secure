import subprocess

def scan_ports(ip):
    try:
        result = subprocess.check_output(["nmap", "-p-", ip], text=True)
        print(result)
    except subprocess.CalledProcessError as e:
        print("Error:", e)

# Example usage
scan_ports("10.5.23.8")
