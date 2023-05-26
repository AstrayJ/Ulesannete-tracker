
<<<<<<< HEAD
"https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html"
=======
from django.urls import path
from . import views

app_name = 'kal'
urlpatterns = [path('', views.index, name='index'),
path('', views.CalendarView.as_view, name='kalender'),
]
>>>>>>> 4da0716dd5de596fdb1fe83908718fb407b688d7
