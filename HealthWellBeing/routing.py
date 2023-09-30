from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from HealthWellBeing import consumers

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/some_path/", consumers.SomeConsumer.as_asgi()),
        # Add here your Url-enpoints, and consumers.
    ]),
})
