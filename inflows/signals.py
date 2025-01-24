from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Inflow
from ai.agents import SGEAgent


@receiver(post_save, sender=Inflow)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:
        if instance.quantity > 0:
            product = instance.product
            product.quantity += instance.quantity
            product.save()

@receiver(post_save, sender=Inflow)
def ai_generates_outflow_stock_insights(sender, instance, **kwargs):
    sge_agent = SGEAgent()
    ai_response = sge_agent.invoke()
