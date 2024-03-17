from django.urls import *
from home import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('query/', views.query, name="query"),
]
