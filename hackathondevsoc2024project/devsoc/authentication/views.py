from django.shortcuts import render, HttpResponse

def login(request):
    return HttpResponse("Login Page")

def logout(request):
    return HttpResponse("Log out")

