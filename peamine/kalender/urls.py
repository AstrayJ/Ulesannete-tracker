
from django.urls import path
from django.contrib import admin

app_name = 'kal'
urlpatterns = [path('admin', admin.site.urls),
]
