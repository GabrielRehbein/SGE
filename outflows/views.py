from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import OutflowSerializer
from .models import Outflow
from .forms import OutflowForm
from core.metrics import get_metric_sales



class OutflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Outflow
    context_object_name = 'outflows'
    template_name = 'outflow_list.html'
    paginate_by = 10
    permission_required = 'outflows.view_outflow'
    

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
        
        context['sales_metrics'] = get_metric_sales()
        context['outflows'] = outflows
        return context
    
    
    

class OutflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Outflow
    context_object_name = 'outflows'
    template_name = 'outflow_detail.html'
    permission_required = 'outflows.view_outflow'



class OutflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Outflow
    context_object_name = 'outflows'
    template_name = 'outflow_create.html'
    form_class = OutflowForm
    success_url = reverse_lazy('outflow_list')
    permission_required = 'outflows.add_outflow'


class OutflowListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Outflow.objects.all()
    serializer_class = OutflowSerializer

class OutflowRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Outflow.objects.all()
    serializer_class = OutflowSerializer