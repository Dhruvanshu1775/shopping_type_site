# Generated by Django 3.1.2 on 2021-03-02 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0012_order_detail_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_detail',
            name='password',
        ),
        migrations.AlterField(
            model_name='order_detail',
            name='product_name',
            field=models.CharField(max_length=20),
        ),
    ]