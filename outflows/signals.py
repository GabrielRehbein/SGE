from django.db.models.signals import post_save
from services.notify import Notify
from django.dispatch import receiver
from .models import Outflow

@receiver(post_save, sender=Outflow)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:
        if instance.quantity > 0:
            product = instance.product
            product.quantity -= instance.quantity
            product.save()


@receiver(post_save, sender=Outflow)
def send_outflow_events(sender, instance, **kwargs):
    notify = Notify()
    format = "%d/%m/%Y %H:%M:%S"
    data = {
        'event_type': 'create_outflow',
        'created_at': instance.created_at.strftime(format),
        'product': instance.product.title,
        'quantity': instance.quantity,
        'unitary_cost_price': float(instance.product.cost_price),
        'unitary_selling_price': float(instance.product.selling_price),
        'total_price': float(instance.product.selling_price * instance.quantity),
        'profit': float(instance.product.selling_price * instance.quantity - instance.product.cost_price * instance.quantity), 
        'description': instance.description,
    }
    try:
        notify.send_sale_event(data)
    except:
        pass
    
        