from django.shortcuts import render, HttpResponse

# Create your views here.
def run(request):
 a = 1000/0
 return HttpResponse("Hello world")

