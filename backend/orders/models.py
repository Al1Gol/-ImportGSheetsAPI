from django.db import models

# Create your models here.

#Orders model
class Orders(models.Model):
    id = models.PositiveSmallIntegerField(verbose_name="№", primary_key=True)
    order = models.PositiveIntegerField (verbose_name="заказ №")
    sum_dol = models.CharField(verbose_name="стоимость,$", max_length=10)
    sum_rub = models.CharField(verbose_name="стоимость,руб.", max_length=10)
    delivery_time = models.CharField(verbose_name="сроки поставки", max_length=10)
    