from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'brand', 'category', 'description', 'serie_number', 'cost_price', 'selling_price')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'control-form',}),
            'brand': forms.Select(attrs={'class': 'control-form',}),
            'category': forms.Select(attrs={'class': 'control-form',}),
            'description': forms.Textarea(attrs={'class': 'control-form', 'rows': 3}),
            'serie_number': forms.TextInput(attrs={'class': 'control-form',}),
            'cost_price': forms.NumberInput(attrs={'class': 'control-form',}),
            'selling_price': forms.NumberInput(attrs={'class': 'control-form',}),     
        }
        labels = {
            'title': 'Título',
            'brand': 'Marca',
            'category': 'Categoria',
            'description': 'Descrição',
            'serie_number': 'Número de Série',
            'cost_price': 'Preço de Custo',
            'selling_price': 'Preço de Venda',
        }
