from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

mycards = {
  'january': 'January is for setting goals and practicing meditation',
  'february': 'February is for gaining muscles and building strength', 
  'march': 'March is for gaining muscles and building strength', 
  'april': 'April is for gaining muscles and building strength', 
  'may': 'May is for gaining muscles and building strength', 
  'june': 'June is for gaining muscles and building strength', 
  'july': 'July is for gaining muscles and building strength', 
  'august': 'August is for gaining muscles and building strength', 
  'september': 'September is for gaining muscles and building strength', 
  'october': 'October is for gaining muscles and building strength', 
  'november': 'November is for gaining muscles and building strength', 
  'december': 'December is for gaining muscles and building strength', 
}

# Create your views here.

def mycard_in_numbers(request, month):
  return HttpResponse(month)


def mycard(request, month):
  try:
    card_text = mycards[month]
    return HttpResponse(card_text)
  except: 
    return HttpResponseNotFound('This is not a valid month at the moment.')
