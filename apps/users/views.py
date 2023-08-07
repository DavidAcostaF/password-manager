from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.views.generic import CreateView, FormView
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse


from .models import User
from .forms import FormLogin, FormRegister


# Create your views here.

class UserRegister(CreateView):
    model = User
    form_class = FormRegister
    template_name = "users/register.html"

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.cleaned_data.pop("password2")
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect("home")
        return render(request, "users/register.html")


# class UserRegister(CreateView):
#     model = User
#     template_name = 'accounts/register.html'
#     form_class = FormRegister
#     success_url = reverse_lazy('home')

#     def post(self,request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         return HttpResponse(status = 204)

class UserLogin(FormView):
    template_name = 'users/login.html'
    form_class = FormLogin  
    success_url = reverse_lazy('home')  

    
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(UserLogin,self).dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(UserLogin,self).form_valid(form)


def logoutUser(request):
    logout(request)
    return redirect('login')
