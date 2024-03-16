import pika
import json
from utils.terminal.nmap import nmap_scan
from utils.terminal.zap import zap_results, zap_scan
from django.conf import settings

def receive_scan_request():

    global print_output 
    print_output = []  

    def callback(ch, method, properties, body):
        data = json.loads(body)
        url = data.get('url')
        record_instance = data.get('instance')

        if url:
            record_instance.status = "RECEIVED BY WORKER"
            try:
                result_data = process_data(url)
                record_instance.result = json.dumps(result_data)  # Corrected json.dumps
            except Exception as e:
                record_instance.status = "TEST-ERROR"
                ch.basic_reject(delivery_tag=method.delivery_tag, requeue=True)
        else:
            ch.basic_reject(delivery_tag=method.delivery_tag, requeue=True)
            record_instance.status = "TEST-ERROR - URL MISSING"
            
        print_output.append(record_instance.status)  # Append status to print_output
    
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
        "nmap": nmap_result.data if hasattr(nmap_result, 'data') else None,
        "zap": zap_result.data if hasattr(zap_result, 'data') else None
    }
    print_and_append("Processed data: " + str(data))  # Or you can return this data if needed

    return data

def print_and_append(message):
    global print_output  # Access the global print_output variable

    print(message)
    print_output.append(message)
