from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Outflow
from .forms import OutflowForm


class OutflowListView(ListView):
    model = Outflow
    context_object_name = 'outflows'
    template_name = 'outflow_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('products')
        if search:
            return queryset.filter(products__title__icontains=search)
        return queryset
    

class OutflowDetailView(DetailView):
    model = Outflow
    context_object_name = 'outflows'
    template_name = 'outflow_detail.html'



class OutflowCreateView(CreateView):
    model = Outflow
    context_object_name = 'outflows'
    template_name = 'outflow_create.html'
    form_class = OutflowForm
    success_url = reverse_lazy('outflow_list')




