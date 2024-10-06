from django.urls import path
from .views import OutflowListView, OutflowCreateView, OutflowDetailView, OutflowListCreateAPIView, OutflowRetrieveAPIView


urlpatterns = [
    path('outflows/list/', OutflowListView.as_view(), name='outflow_list'),
    path('outflows/create/', OutflowCreateView.as_view(), name='outflow_create'),
    path('outflows/<int:pk>/detail/', OutflowDetailView.as_view(), name='outflow_detail'),

    path('api/v1/outflows/', OutflowListCreateAPIView.as_view(), name='outflow_list_create_api'),
    path('api/v1/outflows/<int:pk>/', OutflowRetrieveAPIView.as_view(), name='outflow_retrieve_api'),
]
