import pika
import json



def send_scan_request(url):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='scan_requests')
    message = {'url':url}
    channel.basic_publish(exchange='',
                            routing_key='scan_requests',
                            body = json.dumps(message)
                            )
    
    print("[x] sent",url)
    connection.close()

