from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from .views import home




urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', home, name='home'),

    path('api/v1/', include('brands.urls')),
    path('api/v1/', include('categories.urls')),
    path('api/v1/', include('suppliers.urls')),
    path('api/v1/', include('inflows.urls')),
    path('api/v1/', include('outflows.urls')),
    path('api/v1/', include('products.urls')),
]
