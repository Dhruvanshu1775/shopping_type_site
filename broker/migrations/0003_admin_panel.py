# Generated by Django 3.1.2 on 2021-03-01 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0002_user_data_password2'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_panel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
