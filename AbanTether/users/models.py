from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    balance = models.FloatField(max_length=10, default=1000.0) # The default value is 1000 for simplicity
