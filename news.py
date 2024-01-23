import requests
from ss import *
api_address= "http://newsapi.org/v2/top-headlines?country=us&apikey=apikey"
jason_data = requests.get(api_address).json()
ar=[]
def news():
    for i in range(3):
        ar.append("Number, " + str(i+1) + jason_data["articles"][i]["title"]+".")
    return ar

# arr=news()
# print(arr)
