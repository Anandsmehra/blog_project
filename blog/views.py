from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    home_html = "<h1> Welcome to the Home page </h1>"
    return HttpResponse(home_html)

def about(request):
    home_html = "<h1> Welcome to the About page </h1>"
    return HttpResponse(home_html)
