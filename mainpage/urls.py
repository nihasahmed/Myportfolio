from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('',views.homepage, name='home' ),
    path('details/<ids>', views.details, name='details'),
    path('shop/',views.shop, name='shop' ),



]
