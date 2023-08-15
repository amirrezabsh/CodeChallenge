from django.db import models
from users.models import CustomUser
# Create your models here.
# orders/models.py


class Order(models.Model):
    customer = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, blank=False, null=False)
    currency = models.CharField(max_length=10, null=False, blank=False)
    amount = models.PositiveIntegerField(blank=False, null=False)
    is_checkedout = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.amount} {self.currency} by {self.customer.username}"
