from channels.generic.websocket import WebsocketConsumer
import json

from asgiref.sync import async_to_sync

class testconsumer(WebsocketConsumer):
    def disconnect(self,*args,**kwargs):
        print('hello disconnected')
        # Called when the socket closes

    def receive(self, text_data):
        print(text_data)
        self.send(text_data=json.dumps({'status': 'recived data '}))

    def connect(self):

        self.room_name = "test_consumer"

        self.room_group_name = "test_group_name"
        async_to_sync(self.channel_layer.group_add)
        (self.room_name, self.room_group_name)
        self.accept()
        self.send(text_data=json.dumps({'status': 'connected from djagno channels '}))


















