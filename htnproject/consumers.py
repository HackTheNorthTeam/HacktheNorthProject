from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json

class VideoConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'session_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
    
    async def receive_json(self, content):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": content['type'],
                "data": content['data'],
            })

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )