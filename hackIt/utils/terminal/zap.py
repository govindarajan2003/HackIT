import json
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from zapv2 import ZAPv2
import subprocess
'''
command = [
    "zap.sh",
    "-daemon",
    "-config",
    "api.key=msi9aud5e2id3udm0ijh80uu37"
]

# Run the command
process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
'''

api_key = 'msi9aud5e2id3udm0ijh80uu37'

zap = ZAPv2(apikey=api_key, 
            proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
        )

def zap_scan(url):
    # Initiate ZAP scans: spider and active scan
    zap.spider.scan(url)
    zap.ascan.scan(url)
    
def zap_results():
    # Retrieve ZAP scan results
    alerts = zap.core.alerts()

    # Serialize alerts to JSON
    alerts_json = json.dumps(alerts)
    
    parsed_data = zap_parse_data(alerts_json)
    # Return JSON response
   # process.terminate()
    return Response(parsed_data, status=HTTP_200_OK, content_type='application/json')

def zap_parse_data(json_data):
    summary = {}
    detailed_report = []

    data = json.loads(json_data)
    
    for entry in data:
        risk_rating = entry['risk']
        if risk_rating not in summary:
            summary[risk_rating] = 1
        else:
            summary[risk_rating] += 1

        vulnerability = {
            'Vulnerability Summary': entry['name'],
            'Risk Rating': entry['risk'],
            'Confidence Rating': entry.get('confidence', ''),  # Handling if 'confidence' key is missing
            'Description': entry['description'],
            'Details to Reproduce the Instance': entry.get('url', '')  # Handling if 'url' key is missing
        }
        detailed_report.append(vulnerability)

    formatted_data = {
        "Summary": {
            "No. of Total Vulnerabilities Identified": sum(summary.values()),
            "No. of Total Vulnerabilities Identified grouped on Risk Rating": summary
        },
        "Detailed Report": detailed_report
    }
    return formatted_data


'''
def zap_results():
    
    # Retrieve ZAP scan results
    alerts = zap.core.alerts()

    # Serialize alerts to JSON
    alerts_json = json.dumps(alerts)
    
    parsed_data = zap_parse_data(alerts_json)
    # Return JSON response
    return Response(alerts_json, status=HTTP_200_OK, content_type='application/json')

def zap_parse_data(json_data):
    data = json.loads(json_data)  # Parse the JSON data

    # Count total vulnerabilities and group by risk rating
    total_vulnerabilities = len(data)
    risk_ratings = {}
    for vulnerability in data:
        risk = vulnerability['risk']
        if risk in risk_ratings:
            risk_ratings[risk] += 1
        else:
            risk_ratings[risk] = 1

    # Format the summary section
    summary = f"### Summary\n- **No. of Total Vulnerabilities Identified:** {total_vulnerabilities}\n- **No. of Total Vulnerabilities Identified grouped on Risk Rating:**\n"
    for risk, count in risk_ratings.items():
        summary += f"  - {risk}: {count}\n"

    # Format the detailed report section
    detailed_report = "### Detailed Report\n"
    for i, vulnerability in enumerate(data, start=1):
        detailed_report += f"{i}. **Vulnerability Summary:**\n   - {vulnerability['name']}\n"
    detailed_report += "2. **Risk Rating:**\n"
    for risk, count in risk_ratings.items():
        detailed_report += f"   - {risk}: {count}\n"
    detailed_report += "3. **Confidence Rating:** (Not provided in the data)\n"
    detailed_report += "4. **Description:**\n"
    for i, vulnerability in enumerate(data, start=1):
        detailed_report += f"   - {vulnerability['description']}\n"
    detailed_report += "5. **Details to Reproduce the Instance:** (Not provided in the data)\n"

    return summary + "\n" + detailed_report
'''
