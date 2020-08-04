"""Defines URL patters for shoe_tab"""

from django.urls import path
from . import views 

app_name = 'shoe_tab'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('adidas/', views.adidas, name = 'adidas'),
    path('nike/', views.nike, name = 'nike'),
    path('air_jordan/', views.air_jordan, name = 'air_jordan')
]