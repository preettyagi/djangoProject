from django.urls import path
from . import views

# URL patterns for app1 URLConfig
urlpatterns = [
    path('hello/', views.say_hello, name='say_hello')
]
