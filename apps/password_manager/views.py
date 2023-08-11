from django.shortcuts import render
from django.views.generic import CreateView, FormView, TemplateView

from .models import Password

# Create your views here.


class Home(TemplateView):
    template_name = "password_manager/home.html"

    def get(self, request, *args, **kwargs):
        user = request.user
        # .orger_by("-created_at")  # to get the latest password first
        password = Password.objects.filter(author=user)
        context = {"password": password}

        return render(request, self.template_name, context)
