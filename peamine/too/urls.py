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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kalender/', home_page_view),
<<<<<<< HEAD
    path("login/", login_page_view),
=======
    path("accounts/", include("django.contrib.auth.urls")),
>>>>>>> 88a3aa3d38736a406f3c9642419a1763fe2783c5
]
