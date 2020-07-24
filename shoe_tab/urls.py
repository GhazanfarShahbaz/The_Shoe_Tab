"""Defines URL patters for shoe_tab"""

from django.urls import path
from . import views 

app_name = 'shoe_tab'
urlpatterns = [
    path('', views.index, name = 'index')
]