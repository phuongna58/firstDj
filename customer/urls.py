from django.urls import path
from .views import user_list, user_detail
urlpatterns = [
    path('customer/<int:pk>/', user_detail, name='detail'),
    path('customer', user_list, name='list'),
]

