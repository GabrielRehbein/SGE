from django.test import TestCase
from django.db.utils import IntegrityError
from .models import Outflow
from products.models import Product
from brands.models import Brand
from categories.models import Category


class OutflowModelTests(TestCase):

    def test_create_outflow(self):
        self.brand = Brand.objects.create(name="Marca Teste")
        self.category = Category.objects.create(name="Categoria Teste")
        self.product = Product.objects.create(
            title="Produto Teste",
            brand=self.brand,
            category=self.category,
            description="Descrição do Produto",
            serie_number="123456",
            cost_price=10.00,
            selling_price=20.00,
            quantity=50,
        )
        outflow = Outflow.objects.create(product=self.product, quantity=8, description='Saída de 8 Produtos')
        self.assertEqual(outflow.product, self.product)
        self.assertEqual(outflow.quantity, 8)
        self.assertEqual(outflow.description, 'Saída de 8 Produtos')

    def test_protect_delete_on_product(self):
        self.brand = Brand.objects.create(name="Marca Teste")
        self.category = Category.objects.create(name="Categoria Teste")
        self.product = Product.objects.create(
            title="Produto Teste",
            brand=self.brand,
            category=self.category,
            description="Descrição do Produto",
            serie_number="123456",
            cost_price=10.00,
            selling_price=20.00,
            quantity=50,
        )
        self.outflow = Outflow.objects.create(product=self.product, quantity=5)

        with self.assertRaises(IntegrityError):
            self.product.delete()
