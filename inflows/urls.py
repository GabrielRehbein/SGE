from django.urls import path
from .views import InflowListView, InflowCreateView, InflowDetailView, InflowListCreateAPIView, RetrieveAPIView


urlpatterns = [
    path('inflows/list/', InflowListView.as_view(), name='inflow_list'),
    path('inflows/create/', InflowCreateView.as_view(), name='inflow_create'),
    path('inflows/<int:pk>/detail/', InflowDetailView.as_view(), name='inflow_detail'),


    path('api/v1/inflows/', InflowListCreateAPIView.as_view(), name='inflow_list_create_api'),
    path('api/v1/inflows/<int:pk>/', RetrieveAPIView.as_view(), name='inflow_retrieve_api'),
]
