from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# request -> response
# request handler
# action
def say_hello(request):
    # Pull data from db
    # Transform
    # Send email
    return HttpResponse("Hello World")
