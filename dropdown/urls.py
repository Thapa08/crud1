from django.urls import path
from . import views

urlpatterns = [
    path('', views.dropdown, name='dropdown'),

]