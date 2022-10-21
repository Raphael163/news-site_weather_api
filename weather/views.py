from django.shortcuts import render
from token_weather import token_weather
import requests
from .models import News


# Create your views here.


def index(request):
    city = 'Samara'
    url = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token_weather}&units=metric&lang={"ru"}')
    data = url.json()

    description = {
        "city": city,
        "temp": data['main']['temp'],
        "weather": data['weather'][0]['description'],

    }

    result = {"info": description}

    return render(request, 'weather/index.html', result)


def about_news(request):

    city = 'Samara'
    url = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token_weather}&units=metric&lang={"ru"}')
    data = url.json()

    description = {
        "city": city,
        "temp": data['main']['temp'],
        "weather": data['weather'][0]['description'],

    }

    news = News.objects.all()
    context = {
        'news': news,
        "info": description,

    }

    return render(request, 'weather/about_news.html', context=context)
