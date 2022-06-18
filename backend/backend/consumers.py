import asyncio
import json
from pyexpat import model
from djangochannelsrestframework import permissions
from djangochannelsrestframework import mixins
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer.generics import (ObserverModelInstanceMixin, action)
from djangochannelsrestframework.observer import model_observer

from orders.models import Orders
from orders.serializers import OrdersSerializer


class OrdersConsumer(ObserverModelInstanceMixin, mixins.ListModelMixin, GenericAsyncAPIConsumer):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = (permissions.AllowAny,)

  #get_obgect нужен для возвращения объекта