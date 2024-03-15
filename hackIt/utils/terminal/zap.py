import json

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from zapv2 import ZAPv2

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

    # Return JSON response
    return Response(alerts_json, status=HTTP_200_OK, content_type='application/json')
