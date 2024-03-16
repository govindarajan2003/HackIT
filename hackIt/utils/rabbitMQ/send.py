import pika
import json

from terminal.models import Records

def send_scan_request(record_instance):
    
    status = record_instance.status


    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='scan_requests')
    
    message = {'url':record_instance.url,'instance':record_instance}
    
    channel.basic_publish(exchange='',
                            routing_key='scan_requests',
                            body = message
                            )
    
    print("[x] sent",record_instance.url)
    connection.close()

