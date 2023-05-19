from django.urls import path, url
from . import views

app_name = 'kal'
urlpatterns = [url(r'^index/$', views.index, name='index')]