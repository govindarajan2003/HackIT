
import json
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from django.http import HttpResponse

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
        
def receive_data(request):
    # Query the database to get the required data
    records = Records.objects.all()
    
    # Serialize the data into a list of dictionaries
    data = [{'id': record.id, 'url': record.url, 'status': record.status} for record in records]

    # Return the serialized data as JSON response
    return JsonResponse(data, safe=False)

def receiver_view(request):
    receive_scan_request()
    

def download_terminal_record(request, id):
    # Fetch the record from the database using the provided id
    record = Records.objects.get(id=id)

    # Parse the 'result' JSON data
    result_data = json.loads(record.result)

    # Initialize variables to store total vulnerabilities and vulnerabilities grouped by risk rating
    total_vulnerabilities = 0
    vulnerabilities_by_rating = {'Low': 0, 'Medium': 0, 'High': 0}

    # Calculate total vulnerabilities and vulnerabilities grouped by risk rating in zap
    if result_data['zap']:
        for item in result_data['zap']['Detailed Report']:
            total_vulnerabilities += 1
            risk_rating = item['Risk Rating']
            try:
                vulnerabilities_by_rating[risk_rating] += 1
            except KeyError:
                # Handle the case where the risk_rating key is not found in the dictionary
                vulnerabilities_by_rating[risk_rating] = 1

    # Create a response with the HTML content
    html_content = f"""
    <html>
    <head><title>Terminal Record</title></head>
    <body>
        <h1>Terminal Record</h1>
        <p><strong>ID:</strong> {record.id}</p>
        <p><strong>URL:</strong> {record.url}</p>
        <p><strong>Status:</strong> {record.status}</p>
        <p><strong>Created At:</strong> {record.created_at}</p>
        <p><strong>Updated At:</strong> {record.updated_at}</p>
        <h2>Result:</h2>
    """

    # Add nmap section if available
    if result_data['nmap']:
        html_content += f"<h3>nmap:</h3><table border='1'><tr><th>Field</th><th>Value</th></tr>"
        for key, value in result_data['nmap'].items():
            html_content += f"<tr><td>{key}</td><td>{value}</td></tr>"
        html_content += "</table>"
    else:
        html_content += "<h3>nmap:</h3><p>None</p>"

    # Add zap section if available
    if result_data['zap']:
        html_content += f"""
        <h3>zap:</h3>
        <p>Total Number of Vulnerabilities Identified: {total_vulnerabilities}</p>
        <p>Number of Vulnerabilities Identified grouped by Risk Rating:</p>
        <table border='1'>
            <tr><th>Risk Rating</th><th>Number of Vulnerabilities</th></tr>
            {"".join(f"<tr><td>{rating}</td><td>{count}</td></tr>" for rating, count in vulnerabilities_by_rating.items())}
        </table>
        <h4>Detailed Report:</h4>
        <table border='1'>
            <tr><th>Vulnerability Summary</th><th>Risk Rating</th><th>Confidence Rating</th><th>Description</th><th>Details to Reproduce the Instance</th></tr>
            {"".join(f"<tr><td>{item['Vulnerability Summary']}</td><td>{item['Risk Rating']}</td><td>{item['Confidence Rating']}</td><td>{item['Description']}</td><td>{item['Details to Reproduce the Instance']}</td></tr>" for item in result_data['zap']['Detailed Report'])}
        </table>
        """
    else:
        html_content += "<h3>zap:</h3><p>None</p>"

    html_content += """
    </body>
    </html>
    """

    # Create a response with the HTML content
    response = HttpResponse(html_content, content_type='text/html')

    # Set the filename for the downloadable file
    response['Content-Disposition'] = f'attachment; filename="{record.url}.html"'

    return response

def home_view(request):
    return render(request, 'home.html')



