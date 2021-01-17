from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
import json
from django_redis import get_redis_connection
from htnproject.models import School, Course

redis = get_redis_connection('default')

class VideoConsumer(AsyncJsonWebsocketConsumer):

    @database_sync_to_async
    def check_if_school_exists(self, pin):
        return School.objects.filter(school_id = pin).exists()

    @database_sync_to_async
    def check_if_course_exists(self, course):
        return Course.objects.filter(code = course).exists()

    async def connect(self):
        self.session_name = self.scope['url_route']['kwargs']['session_name']
        self.session_group = 'session_%s' % self.session_name

        await self.channel_layer.group_add(
            self.session_group,
            self.channel_name
        )

        await self.accept()
    
    async def receive_json(self, content):
        if content['type'] == 'add_student_to_queue':
            await self.add_student_to_queue(content)
        elif content['type'] == 'remove_student_from_queue':
            await self.remove_student_from_queue(content)
        
    async def add_student_to_queue(self, content):
        course = content['data']['course']
        first_name = content['data']['first_name']
        pin = content['data']['pin']
        if not await self.check_if_school_exists(pin):
            await self.send_json({
                "status": "failure",
                "element": "first_name",
                "message": "The pin you have provided is invalid."
            })
        elif not await self.check_if_course_exists(course):
            await self.send_json({
                "status": "failure",
                "element": "course",
                "message": "The course code provided is invalid."
            })
        else:
            redis.rpush(course + "-student", self.session_name + ":" + first_name)
            await self.send_json({
                "status": "success",
                "message": "You are now in queue!"
            })
            print(redis.lindex("ENG4U-student", 0))
        # Add the user to the redis cache with the appropriate key.
    
    async def remove_student_from_queue(self, content):
        pass
        # Remove the user from the redis cache or terminate their session if they are in one.

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.session_group,
            self.channel_name
        )