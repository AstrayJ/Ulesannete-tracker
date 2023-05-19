<<<<<<< HEAD
from django.urls import path
from . import views

app_name = 'kal'
urlpatterns = [path('', views.index, name='index')]

"https://www.huiwenteo.com/normal/2018/07/24/django-calendar.html"
=======
<<<<<<< HEAD
from django.urls import path
from . import views

=======
from django.urls import path, url
from . import views

app_name = 'kal'
urlpatterns = [url(r'^index/$', views.index, name='index')]
>>>>>>> f726452b778ad5e6e15ee4fe5a4249665ad5befb
>>>>>>> 80d43841a9ef19586ae3d60dd91f6ed00326450a
