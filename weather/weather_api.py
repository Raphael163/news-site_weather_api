import requests
from token_weather import token_weather

def weath(request):
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
    return (request,result)