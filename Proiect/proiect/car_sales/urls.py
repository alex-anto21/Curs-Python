from django.urls import path
# from car_sales.views import home, about
from . import views

urlpatterns = [
    path('', views.home, name='car_sales-home'),
    path('about/', views.about, name='car_sales-about'),
]
