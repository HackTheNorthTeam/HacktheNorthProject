from django.urls import re_path
from channels.routing import route
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/video/(?P<room_name>\w+)/$', consumers.VideoConsumer.as_asgi()),
]

channel_routing = [
    route("websocket.connect", consumers.connect),
    route("websocket.disconnect", consumers.disconnect),
]