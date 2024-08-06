from django.shortcuts import render
from .metrics import get_metric_products

def home(request):
    context = {
        'product_metrics': get_metric_products()
    }
    return render(request, 'home.html', context)