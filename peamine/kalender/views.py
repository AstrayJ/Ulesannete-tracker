from datetime import datetime
from django.contrib.auth import login
from django.contrib import messages
from django.http.response import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from .models import *
from .utils import Calendar
 
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