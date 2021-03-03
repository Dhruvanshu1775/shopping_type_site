from django import forms
from .models import order_detail

class Userform(forms.ModelForm):
    class Meta:
        model = order_detail
        fields = ['id','username','product_name','productprice','quantity','address',]

        