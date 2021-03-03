from django.contrib import admin
from .models import user_data,admin_panel,product,order_detail
# Register your models here.

admin.site.register(user_data)
admin.site.register(admin_panel)
admin.site.register(product)
admin.site.register(order_detail)

