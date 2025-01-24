import os
from decouple import config


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')


import django
django.setup()

from brands.models import Brand
from inflows.models import Inflow
from outflows.models import Outflow
from categories.models import Category
from suppliers.models import Supplier
from products.models import Product

def create_data_for_tests():
    brand = Brand.objects.create(
    name="Exemplo de Marca",
    description="Descrição da marca."
    )

    category = Category.objects.create(
        name="Exemplo de Categoria",
        description="Descrição da categoria."
    )

    supplier = Supplier.objects.create(
        name="Exemplo de Fornecedor",
        description="Descrição do fornecedor."
    )

    product = Product.objects.create(
        title="Exemplo de Produto",
        brand=brand,
        category=category,
        description="Descrição do produto.",
        serie_number="12345ABC",
        cost_price=10.50,
        selling_price=15.75,
        quantity=100
    )

    inflow = Inflow.objects.create(
        supplier=supplier,
        product=product,
        quantity=50,
        description="Entrada de estoque."
    )

    outflow = Outflow.objects.create(
        product=product,
        quantity=20,
        description="Saída de estoque."
    )

if __name__ == '__main__':
    create_data_for_tests()