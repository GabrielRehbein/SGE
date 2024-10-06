from django.contrib import admin
from .models import Outflow


class OutflowAdmin(admin.ModelAdmin):
    search_fields = ('product__title',)
    list_display = ('product', 'quantity', 'description', 'created_at', 'updated_at',)


admin.site.register(Outflow, OutflowAdmin)
