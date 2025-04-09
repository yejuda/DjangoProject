from django.urls import path
from restaurant_list.views import restaurant_list

urlpatterns = [
    path('', restaurant_list, name='restaurant')
]