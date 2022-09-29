from django.shortcuts import render
from django.views.generic import CreateView
from .forms import SignupForm
from django.urls import reverse_lazy

# Create your views here.
# ListView, DetailView
# Create, Delete, UpdateView
class Signup(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
