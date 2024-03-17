from django.urls import *
from . import views

urlpatterns = [
    path('home/', views.home),
]
