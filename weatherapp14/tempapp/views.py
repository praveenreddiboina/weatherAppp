from django.shortcuts import render
import requests
# Create your views here.
def tempapp(request):
    #city = "hyderabad"
    city = request.GET.get("city")
    url =f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=bb0fd32a3dcf9b68b4d96e62af87cdc9"
    res = requests.get(url)
    response = res.json() 
    
    payload={
        "city" : response["name"],
        "weather" : response["weather"][0]["main"],
        "kelvin" : (int(response["main"]["temp"])), # in k
        "celcius" : (int(response["main"]["temp"])) -273,
        "pressure" : (int(response["main"]["pressure"])),
        "country" : response["sys"]["country"]

    }

    context = {"response" : payload}


    return render(request, 'index.html',context) 