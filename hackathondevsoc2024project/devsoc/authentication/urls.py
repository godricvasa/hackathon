from django.urls import *
from authentication  import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
]
