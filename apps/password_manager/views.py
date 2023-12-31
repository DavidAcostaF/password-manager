import json
from django.shortcuts import render
from django.views.generic import CreateView, FormView, TemplateView, View
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from .models import Password
from .forms import PasswordForm
from .utilities import encrypt, decrypt


# Create your views here.


class Home(TemplateView):
    template_name = "password_manager/home.html"

    def get(self, request, *args, **kwargs):
        user = request.user
        # .orger_by("-created_at")  # to get the latest password first
        password = Password.objects.filter(author=user)
        context = {"passwords": password}
        print(password)
        return render(request, self.template_name, context)


class SavePassword(View):
    form = PasswordForm

    def post(self, request, *args, **kwargs):
        user = request.user
        body_unicode = request.body.decode("utf-8")
        body = json.loads(body_unicode)
        form = self.form(body)
        if form.is_valid():
            password_encrypted = encrypt(body["password"])
            password_created = Password.objects.create(
                author=user, title=body["title"], password=password_encrypted
            )
            password_created.save()

            success = {
                "success": " Password saved successfully",
                "title": "title",
                "id": password_created.id,
            }
            return JsonResponse(success)
        return JsonResponse({"error": "Password not saved"})


class GetPassword(View):
    def get(self, request,id, *args, **kwargs):
        user = request.user
        password_object = Password.objects.get(id=id, author=user)
        password_decrypted = decrypt(password_object.password)
        return JsonResponse({"password": password_decrypted})
