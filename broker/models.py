from django.db import models

# Create your models here.
class user_data(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

class admin_panel(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class product(models.Model):
    product_name = models.CharField(max_length=20)
    product_price = models.IntegerField()

    def __str__(self):
        return self.product_name

class order_detail(models.Model):
    username = models.CharField(max_length=30)
    product_name = models.CharField(max_length=20)
    productprice = models.CharField(max_length=20)
    quantity = models.IntegerField()
    total_price = models.IntegerField()
    address = models.TextField()
    number = models.IntegerField()   

    def __str__(self):
        return self.username
    
