from django.urls import path
from api import views

urlpatterns = [
    path('',views.airplanes),
    path('results',views.result)
]