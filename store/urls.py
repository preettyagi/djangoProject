from django.urls import path
from . import views

# URL patterns for app1 URLConfig
urlpatterns = [
    path('products/', views.product_list, name='products')
]