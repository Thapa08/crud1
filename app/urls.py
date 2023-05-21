from django.urls import path
from . import views

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('contents/',views.content, name='content'),
    path('<int:id>/',views.updateData, name='updateData'),
    path('deletedata/<int:id>/',views.deleteData, name='deleteData'),
    path('login/',views.login_user, name='login'),
    path('signup/',views.signup, name='signup'),
    path('changepass/',views.change_pass_logged_in, name='changepass'),
    path('logout/',views.logout_user, name='logout'),
]

