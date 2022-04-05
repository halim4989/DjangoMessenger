# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        print("************************************")
        print("************************************")
        # print(self.room_name)
        # print(self.room_group_name)
        # print("************************************")
        # print(self.scope)
        # print(self.scope['url_route'])
        # print(self.scope['url_route']['kwargs'])
        print("************************************")
        print("************************************")

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        print(self.room_group_name)

        await self.accept()


    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        print(close_code)

    # Sendind massage
    # Receive message from WebSocket
    async def receive(self, text_data):
        print("text_data")
        # print(text_data)
        text_data_json = json.loads(text_data)
        print(text_data_json)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'date' : "text_data"
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        print("event")
        print(event)
        message = event['message']
        # date = event['date']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            # 'date': date,
        }))