import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ConsumidorWebsocket(AsyncWebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            'msg': 'Prueba'
        }))
    
    def disconnect(self, close_code):
        pass
    
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.send(text_data=json.dumps({
            'message': message
        }))