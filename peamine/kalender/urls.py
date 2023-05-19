from django.urls import path
from . import views

app_name = 'kal'
urlpatterns = [path('', views.index, name='index')]

"https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html"