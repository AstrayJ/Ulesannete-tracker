from django.shortcuts import render

# Create your views here.


from django.http.response import HttpResponse
 
 
def home_page_view(request):
   return render(request,"LandingPage.html")

def login_page_view(request):
   return render(request, "index.html")

from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

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
