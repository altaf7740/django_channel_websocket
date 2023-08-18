import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from myapp.consumers import MyConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectname.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        path("ws/some_path/", MyConsumer.as_asgi()),
    ]),
})
