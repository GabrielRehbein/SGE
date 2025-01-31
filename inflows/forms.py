from django import forms
from .models import Inflow


class InflowForm(forms.ModelForm):

    class Meta:
        model = Inflow
        fields = ('supplier', 'product', 'quantity', 'description',)
        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'supplier': 'Fornecedor',
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

    
        if quantity <= 0:
            raise forms.ValidationError(
                f'A quantidade {quantity} é invalida.'
            )
        return quantity
