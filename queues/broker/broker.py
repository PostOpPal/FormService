import functools
import pika, sys, os
from pika.adapters.blocking_connection import BlockingChannel
import json



class Broker:
    connection: pika.BlockingConnection
    channel: BlockingChannel
    queues = {}

    def __init__(self,app):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=app.config.get("QUEUE_BROKER_URI")))
        self.channel = self.connection.channel()

    def queue(self, name):
        def wrapper(funct):
            self.queues[name] = funct
            return funct
        return wrapper

    @staticmethod
    def deserialise(klass):
        def decorator(funct):
            @functools.wraps(funct)
            def wrapper(*args, **kwargs):
                body = args[3]
                deserialise_body = klass(json.loads(body))
                args[3] = deserialise_body
                return funct(*args, **kwargs)
            return wrapper
        return decorator

    @staticmethod
    def _serialize(obj):
        return obj.__dict__

    @staticmethod
    def serialise():
        def decorator(funct):
            @functools.wraps(funct)
            def wrapper(*args, **kwargs):
                response = funct(*args, **kwargs)
                response_json = json.dumps(response.__dict__, default = self._serialize)
                return response_json
            return wrapper
        return decorator


    def create_all(self):
        for queue in self.queues.keys():
            self.channel.queue_declare(queue=queue)
            self.channel.basic_consume(queue=queue, on_message_callback=self.queues[queue], auto_ack=True)

    def run(self):
        #waiting for messages 
        print("Waiting for messages")
        self.channel.start_consuming()
