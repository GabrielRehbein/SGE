from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Brand
from .forms import BrandForm


class BrandListView(LoginRequiredMixin, ListView):
    model = Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('name')
        if search:
            return queryset.filter(name__icontains=search)
        return queryset


class BrandCreateView(LoginRequiredMixin, CreateView):
    model = Brand
    template_name = 'brand_create.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand_list')


class BrandDetailView(LoginRequiredMixin, DetailView):
    model = Brand
    template_name = 'brand_detail.html'
    context_object_name = 'brands'


class BrandDeleteView(LoginRequiredMixin, DeleteView):
    model = Brand
    template_name = 'brand_delete.html'
    context_object_name = 'brands'
    success_url = reverse_lazy('brand_list')

class BrandUpdateView(LoginRequiredMixin, UpdateView):
    model = Brand
    template_name = 'brand_update.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand_list')
