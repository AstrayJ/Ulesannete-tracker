from django.urls import path
from django.contrib import admin
from . import views

<<<<<<< HEAD
appname = 'kal'
urlpatterns = [path('admin', admin.site.urls),
=======
appname = 'cal'
urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.index, name='index'),
    path('kalender/', views.CalendarView.as_view(), name='kalender'),
    path('kalender/Uus', views.event, name='Uus'),
	path('kalender/event_edit', views.event, name='event_edit'),
>>>>>>> 77919efb53f4e1f0bf695554822aac863573fad4
]
