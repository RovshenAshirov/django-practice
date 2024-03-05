from django.urls import path
from playground.views import say_hello

# URLConf
urlpatterns = [
    path('hello/', say_hello),
]
