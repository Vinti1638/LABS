import requests 
import json 
 
 
def openweathermap(): 
    city = input('City: ') 
    res = requests.get( 
        f'https://api.openweathermap.org/data/2.5/weather?lang=ru&q={city}&appid=37b8a9fc997181408c923c5c248a5864&units=metric') 
    data = res.json() 
 
    if res.status_code == 200: 
        print(f'погода в {city}:', data['weather'][0]['description']) 
        print(f'температура: {data["main"]["temp"]} по Цельсию') 
        print(f'давление: {data["main"]["pressure"]} гекто-паскаль') 
        print(f'влажность: {data["main"]["humidity"]}%') 
 
    else: 
        print("Error", data) 
 
 
def open_notify(): 
    res = requests.get( 
        f'http://api.open-notify.org/iss-now.json') 
    data = res.json() 
 
    if res.status_code == 200: 
        print() 
        print(f'longitude: {data["iss_position"]["longitude"]}') 
        print(f'latitude: {data["iss_position"]["latitude"]}') 
    else: 
        print("Error", data) 
 
 
openweathermap() 
open_notify()