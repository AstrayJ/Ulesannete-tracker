from __future__ import unicode_literals
from django.contrib.auth import login
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.shortcuts import redirect
from .forms import NewUserForm
from .models import *
from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
import calendar
from .utils import Calendar
from .forms import EventForm
def home_page_view(request):
   return render(request,"LandingPage.html")

def login_page_view(request):
   return render(request, "index.html")

def kalender_view(request):
    return render(request, "KALENDER.HTML")


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
    return render(request, 'KALENDER2.html', locals())



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

def kalender_view(request):
    return render(request, "KALENDER.HTML")
   


    #return render(request=request, template_name="main/register.html", context={"register_form":form})


def index(request):
    return HttpResponse('hello')

class CalendarView(generic.ListView):
    model = Event
    template_name = 'KALENDER2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('kalender'))
    return render(request, 'event.html', {'form': form})

