from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('admin', admin.site.urls),
    path('^index/$', views.index, name='index'),
    path('^calendar/$', views.CalendarView.as_view(), name='kalender'),
    path('^event/new/$', views.event, name='Uus'),
	path('^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
]
