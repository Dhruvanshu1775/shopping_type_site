# Generated by Django 3.1.2 on 2021-03-02 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0008_order_detail_productprice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order_detail',
            old_name='name',
            new_name='username',
        ),
    ]
