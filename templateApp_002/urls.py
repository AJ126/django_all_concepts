from django.urls import path
from . import views

urlpatterns = [
    path('simple_temp/', views.simple_temp, name='simple_temp'),
    path('dynamic_temp/', views.dynamic_temp, name='dynamic_temp'),
    path('show_img/', views.show_data, name='show_img'),
]