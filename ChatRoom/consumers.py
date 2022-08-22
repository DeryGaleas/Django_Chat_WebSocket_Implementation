import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)("chat", self.channel_name)
        self.accept()
       
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("chat", self.channel_name)
        print("el usuario se ha desconectado")

    # Receive message from WebSocket
    def receive(self, text_data):
        self.user = self.scope["user"]
        print(self.user.username)
        print(text_data)
        async_to_sync(self.channel_layer.group_send)(
            "chat",
            {
                "type":"chat.message",
                "data":json.dumps({
                    "text": text_data,
                    "user": self.user.username
                    
                    
                } )    
            }
        )



    def chat_message(self, event):
        self.send(text_data=event["data"])

  
       