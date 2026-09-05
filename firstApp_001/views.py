from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def display(request):
    now = datetime.datetime.now()
    html = f"<html><body><h1>Hello, World!</h1><p>The current time is: {now}</p></body></html>"
    return HttpResponse(html)