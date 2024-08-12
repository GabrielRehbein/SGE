from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product
from .forms import ProductForm
from categories.models import Category
from brands.models import Brand
from core.metrics import get_metric_products

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_category = self.request.GET.get('category')
        filter_brand = self.request.GET.get('filter_brand')
        search_title = self.request.GET.get('title')
        search_serie_number = self.request.GET.get('serie_number')

        if filter_category:
            return queryset.filter(category__id__icontains=filter_category)
        if filter_brand:
            return queryset.filter(brand__id__icontains=filter_brand)
        if search_title:
            return queryset.filter(title__icontains=search_title)
        if search_serie_number:
            return queryset.filter(serie_number__icontains=search_serie_number)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        context['product_metrics'] = get_metric_products()
        return context
    
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('product_list')

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'products'

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')



