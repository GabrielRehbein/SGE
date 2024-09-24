from django.urls import path
from .views import ProductListView, ProductCreateView, ProductDeleteView, ProductDetailView, ProductUpdateView, ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('products/list/', ProductListView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/detail/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),

    path('api/v1/products/', ProductListCreateAPIView.as_view(), name='product_list_create_api'),
    path('api/v1/products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product_retrieve_update_destroy_api'),
]

