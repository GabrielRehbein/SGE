from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from .metrics import get_metric_products, get_metric_sales, get_daily_sales_data, get_daily_sales_quantity_data, get_graphic_product_by_category_metric, get_graphic_brand_by_category_metric


@login_required(login_url='/login/')
def home(request):
    context = {
        'product_metrics': get_metric_products(),
        'sales_metrics': get_metric_sales(),
        'daily_sales_data': json.dumps(get_daily_sales_data()),
        'daily_sales_quantity_data': json.dumps(get_daily_sales_quantity_data()),
        'product_by_category': json.dumps(get_graphic_product_by_category_metric()),
        'product_by_brand': json.dumps(get_graphic_brand_by_category_metric()),
    }
    return render(request, 'home.html', context)

