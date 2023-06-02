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

def index(request):
    return render(request, 'KALENDER.html', locals())



class CalendarView(generic.ListView):
    model = Event
    template_name = 'kalender/KALENDER.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

from django.shortcuts import render

def target_page(request):
    if request.method == 'POST':
        # Retrieve the user's input from the form
        user_input = request.POST.get('user_input')

        # Process the user's input or perform any necessary operations

        # Return a response or render a new template based on the input

        # For example, render a template with the input data
        return render(request, 'kalendertopage.html', {'user_input': user_input})
    else:
        return render(request, 'kalendertopage.html')
    
def peale_input(request):
    return render(request, "pealeinput.html")

   

