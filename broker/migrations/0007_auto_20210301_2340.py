# Generated by Django 3.1.2 on 2021-03-01 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0006_remove_product_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order_detail',
            old_name='prdouct_name',
            new_name='product_name',
        ),
    ]
