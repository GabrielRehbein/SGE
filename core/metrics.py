from django.db.models import Sum
from django.utils.formats import number_format
from products.models import Product
from outflows.models import Outflow


def get_metric_products():

    products = Product.objects.all()
    total_quantity = sum(product.quantity for product in products)
    total_stock_cost = sum(product.cost_price * product.quantity for product in products)
    total_stock_sale = sum(product.selling_price * product.quantity for product in products)
    total_stock_profit = total_stock_sale - total_stock_cost

    product_metrics = {
    'total_quantity': total_quantity,
    'total_stock_cost': number_format(total_stock_cost, decimal_pos=2, force_grouping=True),
    'total_stock_sale': number_format(total_stock_sale, decimal_pos=2, force_grouping=True),
    'total_stock_profit': number_format(total_stock_profit, decimal_pos=2, force_grouping=True)
    }

    return product_metrics

def get_metric_sales():

    outflows = Outflow.objects.all()
    total_cost_value = sum(outflow.quantity * outflow.product.cost_price for outflow in outflows)

    total_sales = Outflow.objects.count()  

    total_products_sold = Outflow.objects.aggregate(
        total_products_sold=Sum('quantity')
        )['total_products_sold'] or 0
    
    total_sales_value = sum(outflow.quantity * outflow.product.selling_price for outflow in outflows)
    total_sales_profit = total_sales_value - total_cost_value

    sales_metrics = {
        'total_sales': total_sales,
        'total_products_sold': total_products_sold,                          #ver oque é melhor
        'total_sales_value': number_format(total_sales_value, decimal_pos=2, force_grouping=True),
        'total_sales_profit': number_format(total_sales_profit, decimal_pos=2, force_grouping=True),
    }

    return sales_metrics
