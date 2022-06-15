from dataclasses import fields
from rest_framework.serializers import ModelSerializer

from .models import Orders

class OrdersSerializer(ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'order', 'sum_dol', 'sum_rub', 'delivery_time']
