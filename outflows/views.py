from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Outflow
from products.models import Product
from .forms import OutflowForm
from core.metrics import get_metric_sales



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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        outflows = Outflow.objects.all()
        
        for outflow in outflows:
            outflow.total_price = outflow.product.selling_price * outflow.quantity
        
        
        context['outflows'] = outflows
        return context
    
    

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




