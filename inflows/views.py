from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Inflow
from .forms import InflowForm


class InflowListView(ListView):
    model = Inflow
    context_object_name = 'inflows'
    template_name = 'inflow_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('products')
        if search:
            return queryset.filter(products__title__icontains=search)
        return queryset
    

class InflowDetailView(DetailView):
    model = Inflow
    context_object_name = 'inflows'
    template_name = 'inflow_detail.html'



class InflowCreateView(CreateView):
    model = Inflow
    context_object_name = 'inflows'
    template_name = 'inflow_create.html'
    form_class = InflowForm
    success_url = reverse_lazy('inflow_list')




