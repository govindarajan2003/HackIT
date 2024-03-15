from django.shortcuts import render
from django.http import HttpResponse

from django.conf import settings
from django.http import JsonResponse

from utils.rabbitMQ.send import send_scan_request
from utils.rabbitMQ.receive import receive_scan_request,process_data

def send_data(request):
    if request.method == 'POST':
        input_data = request.POST.get('input_data')
        send_scan_request(input_data)
        response_data = {'message': 'Scan request sent successfully', 'input_data': input_data}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid request method'})
        
def receive_data(request):
    result=receive_scan_request()
    return JsonResponse(result)

def home_view(request):
    return render(request, 'home.html')





'''

class TerminalView(APIView):
    def get(self, request):
        command_id = request.data.get("id", None)
        data = None
        status = HTTP_400_BAD_REQUEST
        if command_id:
            data = {
                "zap": "zap.sh -quickout",
                "nmap": "nmap ",
            }
            status = HTTP_200_OK
        
        else:
            status = HTTP_400_BAD_REQUEST
        
        return Response(
            data = data,
            content_type = "application/json",
            status = status
        )
    
    def post(self, request):
        # Get URL from request data
        url = request.data.get("url")

        # Check if URL is provided
        if not url:
            return Response(
                {"error": "URL is required"},
                status=HTTP_400_BAD_REQUEST
            )

        # Perform scans
        nmap_result = nmap_scan(url)
        zap_scan(url)
        zap_result = zap_results()

        # Check if nmap scan was successful
        if nmap_result is None:
            return Response(
                {"error": "Failed to execute nmap scan"},
                status=HTTP_400_BAD_REQUEST
            )

        # Check if Zap scan was successful
        if zap_result is None:
            return Response(
                {"error": "Failed to execute zap scan"},
                status=HTTP_400_BAD_REQUEST
            )

        # Combine results into a single dictionary
        data = {
            "nmap": nmap_result.data if hasattr(nmap_result, 'data') else None,
            "zap": zap_result.data if hasattr(zap_result, 'data') else None
        }

        return Response(data, status=HTTP_200_OK)

    '''