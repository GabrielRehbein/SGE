from django.contrib import admin
from .models import Inflow


class InflowAdmin(admin.ModelAdmin):
    search_fields = ('product__title',)
    list_display = ('supplier', 'product', 'quantity', 'description', 'created_at', 'updated_at',)

admin.site.register(Inflow, InflowAdmin)