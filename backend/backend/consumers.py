import asyncio
import json
from pyexpat import model
from djangochannelsrestframework import permissions
from djangochannelsrestframework import mixins
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer.generics import (ObserverModelInstanceMixin, action)
from rest_framework import status
from rest_framework.utils.serializer_helpers import ReturnList
from typing import Tuple


from orders.models import Orders
from orders.serializers import OrdersSerializer
from g_sheets.run import get_sheet
from cbrf.cb import get_rate


class OrdersConsumer(ObserverModelInstanceMixin, mixins.ListModelMixin, GenericAsyncAPIConsumer):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = (permissions.AllowAny,)

    @action()
    def list(self, **kwargs) -> Tuple[ReturnList, int]:
        orders_db = Orders.objects.all().delete() #Clear orders db
        import_orders = get_sheet()['values']     #Get data from Google Sheets
        current_rate = get_rate()                 #Get rate  data from the bank

        #Go through the data from the table and fill db with new data
        for i in import_orders:
            orders_db = Orders(
                id = i[0], 
                order = i[1],
                sum_dol = i[2],
                sum_rub = str(round(int(i[2]) * current_rate, 2)).replace(',', '.'),
                delivery_time = i[3])
            orders_db.save()

        #Base class actions
        queryset = self.filter_queryset(self.get_queryset(**kwargs), **kwargs)
        serializer = self.get_serializer(
            instance=queryset, many=True, action_kwargs=kwargs
        )
        return serializer.data, status.HTTP_200_OK

