import subprocess
from utils.constants import vulnerable_ports

def nmap_scan(url):
    
    nmap_command = ["nmap", url]
    completed_process = subprocess.run(nmap_command, stdout=subprocess.PIPE, text=True, check=True)
    output = completed_process.stdout
    parsed_output = parse_nmap_output(output)

    if not parsed_output:
        print("Test_error")
    else:
        print("SUCCESS")
        print(parsed_output)


def parse_nmap_output(output):
    result = {}
    current_host = None
    current_ports = []

    lines = output.split('\n')

    for line in lines:
        if line.startswith("Nmap scan report for"):
            if current_host:
                result[current_host] = current_ports
                current_ports = []
            current_host = line.split(" ")[-1]
        elif "/tcp" in line or "/udp" in line:
            port_info = line.split()
            port = port_info[0].split('/')[0]
            protocol = port_info[0].split('/')[1]
            state = port_info[1]
            service = port_info[2] if len(port_info) > 2 else ""

            recommended_action = "No action Required"
            for service_name, ports in vulnerable_ports.items():
                if port in ports:
                    recommended_action = "Take action"
                    break

            current_ports.append({
                "port": port,
                "protocol": protocol,
                "state": state,
                "service": service,
                "recommended_action": recommended_action
            })

    if current_host:
        result[current_host] = current_ports

    return result
