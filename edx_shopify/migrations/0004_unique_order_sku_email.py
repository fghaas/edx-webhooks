# Generated by Django 2.2.14 on 2020-07-24 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edx_shopify', '0003_fsm_protected'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='orderitem',
            constraint=models.UniqueConstraint(fields=('order', 'sku', 'email'), name='unique_order_sku_email'),
        ),
    ]
