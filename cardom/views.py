from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

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

def index(request):
  list_items = ''
  months = list(mycards.keys())
  
  for month in months:
    capitalized_month = month.capitalize()
    month_path = reverse('card-month', args=[month])
    list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'
    
    
  response_data = f'<ul>{list_items}</ul>'
  return HttpResponse(response_data) 
  

def mycard_in_numbers(request, month):
  months = list(mycards.keys())
  
  if month > len(months):
    return HttpResponseNotFound("Invalid month")
    
  redirect_month = months[month -1]
  
  #build a path with /cardom/january
  redirect_path = reverse("card-month", args=[redirect_month])
  
  return HttpResponseRedirect(redirect_path)


def mycard(request, month):
  try:
    card_text = mycards[month]
    # response_data = f"<h1>{card_text}</h1"
    response_data = render_to_string("cardom/card.html")
    
    return HttpResponse(response_data)
  except: 
    return HttpResponseNotFound('<h1>This is not a valid month at the moment.</h1>')

