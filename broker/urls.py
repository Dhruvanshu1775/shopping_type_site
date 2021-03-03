from django.urls import path
from . import views

urlpatterns = [
    path('',views.login),
    path('register/',views.register,name='register'),
    path('customer/',views.customer,name='customer'),
    path('summary/',views.summary,name='summary'),
    path('place/',views.place,name='place'),
    path('logout/',views.logout,name='logout'),
    path('place/logout/',views.logout),
    path('adminview/',views.adminv,name='adminview'),
    path('place/customer/',views.customer),
    path('customer/logout/',views.logout),
    path('customer/place/',views.place),
    path('delete/<int:id><str:username>',views.delete),
    path('insert/<int:id><str:username>',views.update),
    path('adminview/logout/',views.logout),
]