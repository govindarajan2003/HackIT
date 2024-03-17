from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse

from utils.rabbitMQ.send import send_scan_request
from utils.rabbitMQ.receive import receive_scan_request,process_data
from terminal.models import Records

def send_data(request):
    if request.method == 'POST':
        url = request.POST.get('input_data')

        status = "Scheduled"
        record_instance = Records.objects.create(
            url=url,
            status=status
        )
        record_instance.save()  
        
        send_scan_request(record_instance)

        response_data = {'message': f'Scan request for {url} sent successfully', 'input_data': url}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid request method'})
    
'''def receive_data(request):
    result=receive_scan_request()
    return JsonResponse(result)
'''
def receive_data(request):
    # Query the database to get the required data
    records = Records.objects.all()
    
    # Serialize the data into a list of dictionaries
    data = [{'url': record.url, 'status': record.status} for record in records]
    result = receive_scan_request()

    # Return the serialized data as JSON response
    return JsonResponse(data, safe=False)

def home_view(request):
    return render(request, 'home.html')



