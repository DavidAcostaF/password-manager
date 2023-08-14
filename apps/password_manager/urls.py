from django.urls import path
from .views import Home,SavePassword
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('create_password/', SavePassword.as_view(), name='create_password'),
]