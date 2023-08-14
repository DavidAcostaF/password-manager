from django.urls import path
from .views import Home,SavePassword,GetPassword
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('create_password/', SavePassword.as_view(), name='create_password'),
    path('get_password/<int:id>', GetPassword.as_view(), name='get_password'),
]