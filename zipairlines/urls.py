from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]