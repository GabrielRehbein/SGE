from django.urls import path
from .views import BrandListView, BrandCreateView, BrandDetailView, BrandDeleteView, BrandUpdateView, BrandListCreateAPIView, BrandRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('brands/list/', BrandListView.as_view(), name='brand_list'),
    path('brands/create/', BrandCreateView.as_view(), name='brand_create'),
    path('brands/<int:pk>/detail/', BrandDetailView.as_view(), name='brand_detail'),
    path('brands/<int:pk>/delete/', BrandDeleteView.as_view(), name='brand_delete'),
    path('brands/<int:pk>/update/', BrandUpdateView.as_view(), name='brand_update'),

    path('api/v1/brands/', BrandListCreateAPIView.as_view(), name='brand_list_create_api'),
    path('api/v1/brands/<int:pk>/', BrandRetrieveUpdateDestroyAPIView.as_view(), name='brand_retrieve_update_destroy_api'),

]
