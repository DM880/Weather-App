from django.shortcuts import render, redirect
import requests
from django.urls import reverse
from .models import *
from decouple import config


api_key = config("API_KEY")

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + api_key

# Create your views here.

def base_city(request):

    if request.method == 'POST':

        try:
            city = request.POST['city']
        except:
            return redirect('city:base_city')

        try:

            city_weather = requests.get(url.format(city)).json()

            weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
            }

            City.objects.create(city_name=city)

            context = {'weather': weather}

            city_history = City.objects.all().order_by("-searched")

            city_count = city_history.count()

            if city_count > 6:

                for n, city in enumerate(city_history):

                    if n > 6:

                        City.objects.filter(city_name= city.city_name).delete()

        except KeyError:
            return redirect('city:base_city')

        return render(request, "base_city.html", context)

    return render(request, "base_city.html")


def latest_search(request):

    cities_history = City.objects.all().order_by('-searched')[:7]

    cities = []

    for city in cities_history:

        city_weather = requests.get(url.format(city)).json()

        weather = {
        'city' : city.city_name,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon'],
        'searched': city.searched
        }

        cities.append(weather)

    cities_datas = {'cities':cities}

    return render(request, "latest_search.html", cities_datas)