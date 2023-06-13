from django.urls import path, include
from django.contrib import admin
from . import views


appname = 'cal'
urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.index, name='index'),
    path('kalender/', views.CalendarView.as_view(), name='kalender'),
    path('kalender/Uus', views.event, name='Uus'),
	path('kalender/event_edit', views.event, name='event_edit'),
]
