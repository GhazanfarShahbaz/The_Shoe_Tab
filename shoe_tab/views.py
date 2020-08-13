from django.shortcuts import render
from .models import shoe_data
from django.http import JsonResponse
from shoe_tab.getShoeData import retrieveData


def index(request):
    "The home page for the shoe tab"
    return render(request, 'shoe_tab/index.html')


def adidas(request):
    """Shows all adidas releases"""
    allReleases, hyped = retrieveData("Adidas")
    return render(request, 'shoe_tab/adidas.html', {'releases': allReleases, 'hyped': hyped})


def nike(request):
    """Shows all Nike releases"""
    allReleases, hyped = retrieveData("Nike")
    return render(request, 'shoe_tab/nike.html', {'releases': allReleases, 'hyped': hyped})


def air_jordan(request):
    """Shows all jordan releases"""
    allReleases, hyped = retrieveData("Air Jordan")
    return render(request, 'shoe_tab/air_jordan.html', {'releases': allReleases, 'hyped': hyped})
