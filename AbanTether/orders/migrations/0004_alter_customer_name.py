# Generated by Django 4.2.4 on 2023-08-13 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_customer_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
