from django.shortcuts import render, HttpResponse
from .models import Location
import requests
from django.conf import settings

# Create your views here.
def index(request):
    locs = Location.objects.all()
    return render(request, 'index.html', {'locs': locs})

def get_weather(request):
    if request.method == 'POST':
        loc = request.POST.get('search')
        try:
            location = Location.objects.get(name=loc)
        except:
            location = loc
        api_key = settings.GET_API_KEY
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no"
        response = requests.get(url)
        weather_data = response.json()
        
    context = {
        'weather_data': weather_data
    }
    return render(request, 'show-forcast.html', context)