from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contents/',views.content, name='content'),
    path('<int:id>/',views.updateData, name='updateData'),
    path('deletedata/<int:id>/',views.deleteData, name='deleteData'),
]

