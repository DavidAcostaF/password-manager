from django.shortcuts import render
from django.views.generic import CreateView, FormView, TemplateView

from .models import Password

from cryptography.fernet import Fernet

# Create your views here.


class Home(TemplateView):
    template_name = "password_manager/home.html"

    def get(self, request, *args, **kwargs):
        user = request.user
        # .orger_by("-created_at")  # to get the latest password first
        password = Password.objects.filter(author=user)
        context = {"password": password}

        return render(request, self.template_name, context)


class SavePassword(CreateView):
    model = Password
    
    def post(self,request,*args,**kwargs):
        user = request.user
        password = request.POST.get("password")
        title= request.POST.get("title")
        if password and title:
            password_encrypted = encrypt(password)
            password_created = Password.objects.create(author=user,title=title,password=password_encrypted)
            password_created.save()

            success = {
                'success':' Password saved successfully',
                'title': 'title',
                'id': password_created.id,
            }


def encrypt(password):
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted = f.encrypt(password.encode())
    return encrypted
        
def decrypt(password):
    key = Fernet.generate_key()
    f = Fernet(key)
    decrypted = f.decrypt(password.encode())
    return decrypted
