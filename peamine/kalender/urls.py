from django.urls import path
from django.contrib import admin
from . import views

appname = 'cal'
urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.index, name='index'),
    path('kalender/', views.CalendarView.as_view(), name='kalender'),
    path('Uus/', views.event, name='Uus'),
	path('Muutus', views.event, name='event_edit'),
]
