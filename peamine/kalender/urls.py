from django.urls import path
from django.contrib import admin
from . import views

appname = 'cal'
urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.index, name='index'),
    path('kalender/', views.CalendarView.as_view(), name='kalender'),
<<<<<<< HEAD
    path('Uus/', views.event, name='Uus'),
	path('Muutus/', views.event, name='event_edit'),
=======
    path('kalender/Uus', views.event, name='Uus'),
	path('kalender/event_edit', views.event, name='event_edit'),
>>>>>>> 6ffb3bd3c5509a816a50f4f785407cf6a7ecaafd
]
