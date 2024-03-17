import pika
import json
from utils.terminal.nmap import nmap_scan
from utils.terminal.zap import zap_results, zap_scan
from django.conf import settings
from terminal.models import Records
def receive_scan_request():

    global print_output 
    print_output = []  

    def callback(ch, method, properties, body):
        data = json.loads(body)
        id = data.get('id')
        url = data.get('url')
        record_instance = Records.objects.get(id = id)
        
        if url:
            
            record_instance.status = "RECEIVED BY WORKER"
            record_instance.save()
            
            try:
                result_data = process_data(url)
                record_instance.result = json.dumps(result_data)  # Corrected json.dumps
                record_instance.status = "COMPLETED"
                record_instance.save()
                

                
            except Exception as e:
                record_instance.status = "TEST-ERROR"
                record_instance.save()
                ch.basic_reject(delivery_tag=method.delivery_tag, requeue=True)

        else:
            ch.basic_reject(delivery_tag=method.delivery_tag, requeue=True)
            record_instance.status = "TEST-ERROR - URL MISSING"
            record_instance.save()
            
        #print_output.append(status)  # Append status to print_output
    
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='scan_requests')
    channel.basic_consume(queue='scan_requests',
                          on_message_callback=callback,
                          auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

    return print_output

def process_data(url):
    
    global print_output     
    
    zap_scan(url)
    zap_result = zap_results()
    nmap_result = nmap_scan(url)
    
    if nmap_result is None:
        print_and_append("Failed to execute nmap scan")

    elif zap_result is None:
        print_and_append("Failed to execute zap scan")

    if nmap_result is None and zap_result is None:
        raise Exception("Failed to execute zap scan")
    
      
    data = {
        "nmap": nmap_result if nmap_result is not None else None,
        "zap": zap_result.data if hasattr(zap_result, 'data') else None
    }
    print_and_append("Processed data: " + str(data))  # Or you can return this data if needed

    return data

def print_and_append(message):
    global print_output  # Access the global print_output variable

    print(message)
    print_output.append(message)
