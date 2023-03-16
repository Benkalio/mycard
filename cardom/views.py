from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def january(request):
  return HttpResponse("This is the january")


def february(request):
  return HttpResponse("Second month of the year")