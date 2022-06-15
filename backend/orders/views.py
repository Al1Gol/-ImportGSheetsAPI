from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import OrdersSerializer
from .models import Orders

# Create your views here.
class OrderViewSet(ModelViewSet):
    serializer_class = OrdersSerializer

    def get_queryset(self):
        return Orders.objects.all()