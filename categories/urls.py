from django.urls import path
from .views import CategoryListView, CategoryDetailView, CategoryCreateView, CategoryDeleteView, CategoryUpdateView


urlpatterns = [
    path('categories/list/', CategoryListView.as_view(), name='category_list'),
    path('categories/create', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/detail/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
]