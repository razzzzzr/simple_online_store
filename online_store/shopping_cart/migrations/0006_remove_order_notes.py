# Generated by Django 4.1.7 on 2023-03-09 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0005_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='notes',
        ),
    ]
