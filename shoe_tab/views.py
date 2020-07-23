from django.shortcuts import render
from .models import shoe_data
# Create your views here.
from shoe_tab.getShoeData import retrieveData

def index(request):
    "The home page for the shoe tab"
    return render(request, 'shoe_tab/index.html')

def shoes(request):
    """Shoe all shoes"""
    return render(request, 'shoe_tab/shoe_tab.html', retrieveData("Nike"))
