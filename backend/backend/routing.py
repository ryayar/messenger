from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path, re_path
from .consumers import MyConsumer, MyConsumer

from . import consumers

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/chat/", MyConsumer),
    ]),
})
