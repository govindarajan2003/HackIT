import pika
import json
from utils.terminal.nmap import nmap_scan
from utils.terminal.zap import zap_results, zap_scan

def receive_scan_request():
    global print_output  # Define print_output as a global variable

    print_output = []  # Initialize an empty list to collect print statements

    def callback(ch, method, properties, body):
        data = json.loads(body)
        url = data.get('url')
        if url:
            # Perform scans here based on the received URL
            print_and_append(f"Received scan request for URL: {url}")
            process_data(url)
            
        else:
            print_and_append("Invalid message format - missing URL")

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the queue
    channel.queue_declare(queue='scan_requests')

    # Consume messages from the queue
    channel.basic_consume(queue='scan_requests',
                          on_message_callback=callback,
                          auto_ack=True)

    print_and_append(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

    # Return the collected print statements
    return print_output

def process_data(url):
    global print_output  # Access the global print_output variable

    nmap_result = nmap_scan(url)
    zap_scan(url)
    zap_result = zap_results()

    # Check if nmap scan was successful
    if nmap_result is None:
        print_and_append("Failed to execute nmap scan")

    # Check if Zap scan was successful
    if zap_result is None:
        print_and_append("Failed to execute zap scan")

    # Combine results into a single dictionary
    data = {
        "nmap": nmap_result.data if hasattr(nmap_result, 'data') else None,
        "zap": zap_result.data if hasattr(zap_result, 'data') else None
    }

    print_and_append("Processed data: " + str(data))  # Or you can return this data if needed

def print_and_append(message):
    global print_output  # Access the global print_output variable

    print(message)
    print_output.append(message)
