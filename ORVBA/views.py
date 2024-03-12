from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View,CreateView
from ORVBA.forms import *
from django.contrib.auth.views import LoginView

# Create your views here.
# class SigninView(LoginView):
#     template_name="login.html"
#     # form_class=UserForm
    
#     def get_success_url(self):
#         return reverse("signin")
    
# class SignupView(CreateView):
#     template_name="login.html"
#     form_class= UserForm

#     def get_success_url(self) -> str:
#         return reverse("signin")
    
#     def form_valid(self, form):
#         user = form.save()
#         return super().form_valid(form)