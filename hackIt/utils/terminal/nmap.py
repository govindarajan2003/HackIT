from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
import subprocess

from utils.constants import vulnerable_ports

def nmap_scan(url):
    if not url:
        return Response(
            data={"error": "URL is required"},
            status=HTTP_400_BAD_REQUEST,
            content_type="application/json"
        )
    
    nmap_command = ["nmap", url]
    completed_process = subprocess.run(nmap_command, stdout=subprocess.PIPE, text=True)
    output = completed_process.stdout
    
    # Parse the output of the nmap command
    parsed_output = parse_nmap_output(output)
    
    if not parsed_output:
        data = {
            "nmap": {},
            "command_status": "Test_error"
        }
        status = HTTP_400_BAD_REQUEST
    else:
        data = {
            "nmap": parsed_output,
            "command_status": "SUCCESS"
        }
        status = HTTP_200_OK
    
    return Response(
        data=data,
        status=status,
        content_type="application/json"
    )

def parse_nmap_output(output):
    result = {}
    current_host = None
    current_ports = []

    lines = output.split('\n')

    for line in lines:
        # Look for lines that start with "Nmap scan report" to identify hosts
        if line.startswith("Nmap scan report for"):
            if current_host:
                result[current_host] = current_ports
                current_ports = []
            current_host = line.split(" ")[-1]
        
        # Look for lines containing port information
        elif "/tcp" in line or "/udp" in line:
            port_info = line.split()
            port = port_info[0].split('/')[0]  # Extract port number
            protocol = port_info[0].split('/')[1]  # Extract protocol
            state = port_info[1]  # State is the next item
            service = port_info[2] if len(port_info) > 2 else ""  # Service can be rest of the line
            
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
    