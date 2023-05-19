"""
URL configuration for too project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from kalender.views import home_page_view
from kalender.views import login_page_view
from kalender.views import register_page_view

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('homepage/', home_page_view),
    path("login/", login_page_view),
    path("register/", register_page_view),
<<<<<<< HEAD
    path("kalender/", include ('kal.urls')),
=======
<<<<<<< HEAD
=======
    path("kalender/", include ('kal.urls'),
>>>>>>> f726452b778ad5e6e15ee4fe5a4249665ad5befb
>>>>>>> 80d43841a9ef19586ae3d60dd91f6ed00326450a
]
