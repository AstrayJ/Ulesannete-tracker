from django.urls import path, include
from django.contrib import admin
from . import views

<<<<<<< HEAD

urlpatterns = [
    path('admin', admin.site.urls),
=======
appname = 'cal'
urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.index, name='index'),
    path('kalender/', views.CalendarView.as_view(), name='kalender'),
    path('kalender/Uus', views.event, name='Uus'),
	path('kalender/event_edit', views.event, name='event_edit'),
>>>>>>> 047a75789cc2f142f72fbf8d03ffb66d7c7032c6
]
