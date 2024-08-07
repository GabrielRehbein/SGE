from django.shortcuts import render
from .metrics import get_metric_products, get_metric_sales

def home(request):
    context = {
        'product_metrics': get_metric_products(),
        'sales_metrics': get_metric_sales(),
    }
    return render(request, 'home.html', context)

