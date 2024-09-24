from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import InflowSerializer
from .models import Inflow
from .forms import InflowForm


class InflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Inflow
    context_object_name = 'inflows'
    template_name = 'inflow_list.html'
    paginate_by = 10
    permission_required = 'inflows.view_inflow'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('products')
        if search:
            return queryset.filter(products__title__icontains=search)
        return queryset
    

class InflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Inflow
    context_object_name = 'inflows'
    template_name = 'inflow_detail.html'
    permission_required = 'inflows.view_inflow'



class InflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Inflow
    context_object_name = 'inflows'
    template_name = 'inflow_create.html'
    form_class = InflowForm
    success_url = reverse_lazy('inflow_list')
    permission_required = 'inflows.add_inflow'


class InflowListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer


class InflowRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer


