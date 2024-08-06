from django.utils.formats import number_format
from products.models import Product


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

