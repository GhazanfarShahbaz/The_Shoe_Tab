from django.shortcuts import render

from .models import shoe_data
# Create your views here.


def index(request):
    "The home page for the shoe tab"
    return render(request, 'shoe_tab/index.html')

def shoes(request):
    """Shoe all shoes"""
    shoes = shoe_data.objects.order_by('date_added')
    contex        ,gcx     t = {'topics': topics}
    return render(request, 'shoe_tab/shoe_tab.html', context)