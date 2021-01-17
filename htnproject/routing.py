from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/video/(?P<session_name>\w+)/$', consumers.VideoConsumer.as_asgi()),
]