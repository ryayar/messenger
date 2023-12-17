from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from django.urls import path
from .consumers import MyConsumer  # замените на свой Consumer

websocket_urlpatterns = [
    path('ws/chat/', MyConsumer.as_asgi()),
    # Замените 'your_endpoint' на конкретный эндпоинт для WebSocket
]

application = ProtocolTypeRouter({
    "https": get_asgi_application(),
    "http": get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    )
})
