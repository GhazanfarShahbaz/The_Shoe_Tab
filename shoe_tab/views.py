from django.shortcuts import render
from .models import shoe_data
from django.http import JsonResponse
# Create your views here.
from shoe_tab.getShoeData import retrieveData

def index(request):
    "The home page for the shoe tab"
    return render(request, 'shoe_tab/index.html')

def adidas(request):
    """Shows all adidas releases"""
    return render(request, 'shoe_tab/adidas.html', {'data': retrieveData("Adidas")})

def nike(request):
    """Shows all adidas releases"""
    return render(request, 'shoe_tab/nike.html', {'data': retrieveData("Nike")})

def air_jordan(request):
    """Shows all jordan releases"""
    return render(request, 'shoe_tab/air_jordan.html', {'data': retrieveData("Air Jordan")})
