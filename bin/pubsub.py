from socket_io_emitter import Emitter
import json, os, redis

redis_client = redis.from_url(url=os.getenv('PUBSUB_URL'), db=0)

class Publisher:
    io: Emitter
    def __init__(self):
        self.io = Emitter({'client': redis_client}) #({'url': os.getenv('PUBSUB_URL')})
    
    def emit(self, event:str, payload: dict):
        self.io.Emit(event, json.dumps(payload))

publisher = Publisher()