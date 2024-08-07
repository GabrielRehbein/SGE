from django.db.models import Sum,F
from django.utils import timezone
from django.utils.formats import number_format
from products.models import Product
from outflows.models import Outflow
from categories.models import Category
from brands.models import Brand


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


def get_daily_sales_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    values = list()

    for date in dates:
        sales_total = Outflow.objects.filter(
            created_at__date=date
        ).aggregate(
            total_sales=Sum(F('product__selling_price') * F('quantity'))
        )['total_sales'] or 0
        values.append(float(sales_total))

    return {
        'dates':dates,
        'values':values,
    }


def get_daily_sales_quantity_data():
    today = timezone.now().date()
    dates = [str(today - timezone.timedelta(days=i)) for i in range(6, -1, -1)]
    values = list()

    for date in dates:
        sales_quantity = Outflow.objects.filter(
            created_at__date=date
        ).count()
        values.append(sales_quantity)

    return dict(
        dates= dates,
        values=values
    )

    
def get_graphic_product_by_category_metric():

    categories = Category.objects.all()
    return {category.name: Product.objects.filter(category=category).count() for category in categories}


def get_graphic_brand_by_category_metric():
    brands = Brand.objects.all()
    return {brand.name: Product.objects.filter(brand=brand).count() for brand in brands}