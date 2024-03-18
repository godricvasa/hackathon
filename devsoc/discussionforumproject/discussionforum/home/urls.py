from django.urls import path
from home import views

urlpatterns = [
    path('home/', views.user_profile, name='user_profile'),
]