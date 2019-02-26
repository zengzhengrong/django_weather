import requests
from django.shortcuts import render ,redirect
from .models import City
from .froms import CityForm
from django.contrib import messages
from django.conf import settings
from .utils import get_citys_weather
# Create your views here.

def index(request):
    template = 'weather/weather.html'
    APIKEY = getattr(settings,'APIKEY',None)
    form = CityForm()

    citys = [city.name for city in City.objects.all()]
    weather_data = get_citys_weather(APIKEY,citys)

    # print(weather_data)
    context = {
        'citys':weather_data,
        'form':form
    }
    if request.method == 'POST':
        form = CityForm(request.POST)
        if not form.is_valid():
            msg = form['name'].errors.as_text()
            messages.error(request,msg)
            return redirect('weather:index')
        msg = 'Check Success'
        messages.success(request,msg)
        form.save()
        return redirect('weather:index')

    return render(request,template,context)
