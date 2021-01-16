from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels import Group
import json

class VideoConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'video_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        print(f"Added {self.channel_name} channel to video")
        await self.accept()
    
    async def receive_json(self, content):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                # func that will receive this data and send data to socket
                "type": content['type'],
                "data": content['data'],
            })


    async def send_offer(self, event):
        await self.send_json(event["data"])

    async def send_answer(self, event):
        await self.send_json(event["data"])

    async def send_ice_candidate(self, event):
        await self.send_json(event["data"])

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )