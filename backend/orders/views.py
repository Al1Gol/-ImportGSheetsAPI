import imp
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import OrdersSerializer
from .models import Orders
from datetime import datetime

from g_sheets.run import get_sheet
from cbrf.cb import get_rate

# Create your views here.
class OrderViewSet(ModelViewSet):
    serializer_class = OrdersSerializer

    def get_queryset(self):
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
        return Orders.objects.all()
    
