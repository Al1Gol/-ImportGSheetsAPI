from django.urls import path, re_path

from . import consumers

websocket_urlpatterns = [
    # We use re_path() due to limitations in URLRouter.
    path('', consumers.OrdersConsumer.as_asgi())
]