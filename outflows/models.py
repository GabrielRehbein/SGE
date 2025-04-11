from django.db import models
from products.models import Product


class Outflow(models.Model):
    product = models.ForeignKey(Product,
    on_delete=models.PROTECT,
    related_name='outflows')
    quantity = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Saída'
        verbose_name_plural = 'Saídas'

    def __str__(self) -> str:
        return f'{str(self.quantity)}x - {str(self.product)}'
