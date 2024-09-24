from django.urls import path
from .views import SupplierListView, SupplierCreateView, SupplierDetailView, SupplierDeleteView, SupplierUpdateView, SupplierListCreateAPIView, SupplierRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('suppliers/list/', SupplierListView.as_view(), name='supplier_list'),
    path('suppliers/create/', SupplierCreateView.as_view(), name='supplier_create'),
    path('suppliers/<int:pk>/detail/', SupplierDetailView.as_view(), name='supplier_detail'),
    path('suppliers/<int:pk>/delete/', SupplierDeleteView.as_view(), name='supplier_delete'),
    path('suppliers/<int:pk>/update/', SupplierUpdateView.as_view(), name='supplier_update'),

    path('api/v1/suppliers/', SupplierListCreateAPIView.as_view(), name='supplier_update_list_create_api'),
    path('api/v1/suppliers/<int:pk>/', SupplierRetrieveUpdateDestroyAPIView.as_view(), name='supplier_update_retrieve_update_destroy_api'),
]