from django.shortcuts import render
from .models import Team
from cars.models import Car

def home(request):
  teams = Team.objects.all()
  cars_feature = Car.objects.order_by('-created_date').filter(is_featured=True)
  all_cars = Car.objects.order_by('-created_date')
  model_search = Car.objects.values_list('model', flat=True).distinct()
  city_search = Car.objects.values_list('city', flat=True).distinct()
  year_search = Car.objects.values_list('year', flat=True).distinct()
  body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
  data = {
    'teams': teams,
    'cars_feature': cars_feature,
    'all_cars': all_cars,
    'model_search': model_search,
    'city_search': city_search,
    'year_search': year_search,
    'body_style_search': body_style_search,
  }
  return render(request, 'pages/home.html', data)


def about(request):
  teams = Team.objects.all()
  data = {
    'teams': teams
  }
  return render(request, 'pages/about.html', data)


def services(request):
  return render(request, 'pages/services.html')


def contact(request):
  return render(request, 'pages/contact.html')