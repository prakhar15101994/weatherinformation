from django.http.response import HttpResponse
from django.shortcuts import render
import requests

#api key= ce7b271f88f406fb2341068682a452aa
# urls=api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

# json format api
# {"coord":{"lon":80.9167,"lat":26.85},"weather":[{"id":721,"main":"Haze","description":"haze","icon":"50d"}],"base":"stations","main":{"temp":307.14,"feels_like":314.14,"temp_min":307.14,"temp_max":307.14,"pressure":1004,"humidity":75},"visibility":5000,"wind":{"speed":1.03,"deg":0},"clouds":{"all":40},"dt":1630823053,"sys":{"type":1,"id":9176,"country":"IN","sunrise":1630801059,"sunset":1630846376},"timezone":19800,"id":1264733,"name":"Lucknow","cod":200}
# Create your views here.
def home(request):
    city=request.GET.get('city', "lucknow")
    url='https://newsapi.org/v2/everything?q=tesla&from=2021-08-05&sortBy=publishedAt&apiKey=de1b9477cb6f451ab973ee747138b4ac'
    data=requests.get(url).json()
    articles=data['article']
    context={'articles': articles}

    
    print(context)
    return render(request, 'home.html', context)