
from django.urls import path
from . import views

app_name = 'kal'
urlpatterns = [path('', views.index, name='index'),
path('', views.CalendarView.as_view, name='kalender'),
]
