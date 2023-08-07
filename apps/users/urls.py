from django.urls import path
from .views import UserLogin, UserRegister,logoutUser

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('register/', UserRegister.as_view(), name='register'),
    path('logout/', logoutUser, name='logout')

]