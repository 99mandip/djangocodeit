from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    print("Home view is called")

    return HttpResponse("<h1>This is home page</h1>")

def contact(request):
    return HttpResponse("This is contact page, contact us at 9800")
