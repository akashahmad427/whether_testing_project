import requests
from django.shortcuts import render
from .forms import Data
def weather(request):
    if request.method =='POST':
        fm = Data(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['Enter_city']
            print('city name',name)
            api_key = 'a4cd856ecf28ebc0a5e7562b569b1b4c'
            city = name # Replace with the city you want to get weather data for
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

            response = requests.get(url).json()

            temperature = response['main']['temp']
            humidity = response['main']['humidity']
            description = response['weather'][0]['description']
            # name=response['name']
            country=response['sys']['country']
            context = {
                'temperature': temperature,
                'humidity': humidity,
                'description': description,
                'country':country
            }
            short = name
            fm=Data()
            return render(request, 'weather.html',{'shortname':short,'weather':context,'form':fm})
    else:
        fm=Data()
        return render(request, 'weather.html',{'form':fm})
