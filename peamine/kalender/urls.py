<<<<<<< HEAD
from django.urls import path
from . import views

=======
from django.urls import path, url
from . import views

app_name = 'kal'
urlpatterns = [url(r'^index/$', views.index, name='index')]
>>>>>>> f726452b778ad5e6e15ee4fe5a4249665ad5befb
