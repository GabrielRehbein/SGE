from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Supplier
from .forms import SupplierForm


class SupplierListView(ListView):
    model = Supplier
    context_object_name = 'suppliers'
    template_name = 'supplier_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('name')
        if search:
            return queryset.filter(name__icontains=search)
        return queryset


class SupplierCreateView(CreateView):
    form_class = SupplierForm
    model = Supplier
    template_name = 'supplier_create.html'
    success_url = reverse_lazy('supplier_list')


class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'supplier_detail.html'
    context_object_name = 'suppliers'


class SupplierDeleteView(DeleteView):
    model = Supplier
    context_object_name = 'suppliers'
    template_name = 'supplier_delete.html'
    success_url = reverse_lazy('supplier_list')

class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierForm
    success_url = reverse_lazy('supplier_list')
    template_name = 'supplier_update.html'
    
