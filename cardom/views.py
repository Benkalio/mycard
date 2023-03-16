from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

def mycard(request, month):
  if month == 'january':
    card_text = 'January is for setting goals and practicing meditation'
  elif month == 'february':
    card_text = 'February is for gaining muscles and building strength'
  elif month == 'march':
    card_text = 'March is for improving skills'
  else: 
    return HttpResponseNotFound('This is not a valid month at the moment.')
  return HttpResponse(card_text)
