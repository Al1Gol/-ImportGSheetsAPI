from django.db import models

# Create your models here.

#Orders model
class Orders(models.Model):
    id = models.PositiveSmallIntegerField(verbose_name="№", primary_key=True)
    order = models.PositiveIntegerField (verbose_name="заказ №")
    sum_dol = models.PositiveIntegerField(verbose_name="стоимость,$")
    sum_rub = models.PositiveIntegerField(verbose_name="стоимость,руб.")
    delivery_time = models.DateField(verbose_name="сроки поставки")
    