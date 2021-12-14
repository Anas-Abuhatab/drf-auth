from django.urls import path
from .views import Carlist, CarDetail ,CarCreate


urlpatterns = [
    path('', Carlist.as_view(), name= 'car_list'),
    path('<int:pk>/', CarDetail.as_view(), name='car_details'),
    path('create/', CarCreate.as_view(), name='car_create'),
]