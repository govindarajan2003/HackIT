import pika
import json

from terminal.models import Records

def send_scan_request(record_instance):
    
    status = record_instance.status


    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='scan_requests')
    
    message = {'url':record_instance.url,'status':record_instance.status,'result':record_instance.result,'id':record_instance.id}
    body = json.dumps(message)
    channel.basic_publish(exchange='',
                            routing_key='scan_requests',
                            body = body.encode('utf-8')
                            )
    
    print("[x] sent",record_instance.url)
    connection.close()

