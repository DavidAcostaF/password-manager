from django.shortcuts import render
from django.views.generic import CreateView, FormView, TemplateView

# Create your views here.


class home(TemplateView):
    template_name = "password_manager/base.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})