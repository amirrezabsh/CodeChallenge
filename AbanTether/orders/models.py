from django.db import models
from .models import Customer
# Create your models here.
# orders/models.py


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    currency = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_checkedout = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
