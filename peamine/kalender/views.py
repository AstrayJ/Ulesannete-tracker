from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib import messages
from django.http.response import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from .models import *

 
def home_page_view(request):
   return render(request,"LandingPage.html")

def login_page_view(request):
   return render(request, "index.html")


def register_page_view(request):
   if request.method == "POST":
      form = NewUserForm(request.POST)
      if form.is_valid():
         user = form.save()
         login(request, user)
         messages.success(request, "Registration successful." )
         return redirect("main:homepage")
      messages.error(request, "Unsuccessful registration. Invalid information.")
   form = NewUserForm()
   return render (request=request, template_name="main/register.html", context={"register_form":form})