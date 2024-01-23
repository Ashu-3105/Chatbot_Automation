import requests
from ss import *
api_address='http://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=apiid'
jason_data=requests.get(api_address).json()
# print(jason_data)
def temp():
    # temprature =round(jason_data['main']['temp'][0]-273,1)
    temprature = jason_data['main']['temp']
    return temprature
def description():
    des = jason_data["weather"][0]["description"]
    return des

# print(f"temperature is {round(temp()-273,1)} celsius.")
# print(description())
