from django.urls import path
from django.contrib import admin

appname = 'kal'
urlpatterns = [path('admin', admin.site.urls),
]
