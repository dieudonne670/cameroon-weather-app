from django.conf import settings
from django.shortcuts import render
import requests

def index(request):
    weather_data = None
    error = None
    debug = None

    if request.method == "POST":
        city = request.POST.get("city_name").strip()
        api_key = settings.OPENWEATHER_API_KEY
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city},CM&units=metric&appid={api_key}"

        response = requests.get(url).json()
        print("DEBUG:", response)
        debug = response

        if response.get("cod") == 200:
            weather_data = {
                "city": city,
                "temp": response["main"]["temp"],
                "description": response["weather"][0]["description"],
                "icon": response["weather"][0]["icon"],
                "humidity": response["main"]["humidity"],
                "wind": response["wind"]["speed"]
            }

        else:
            error = f"{city} was not found in Cameroon."

    return render(request, "weather/weather.html", {
        "weather": weather_data,
        "error": error,
        "debug": debug
    })