import requests
from ss import *
api_address= "http://newsapi.org/v2/top-headlines?country=us&apikey=4efce9f1a48949049e3becb4c5f1b628"
jason_data = requests.get(api_address).json()
ar=[]
def news():
    for i in range(3):
        ar.append("Number, " + str(i+1) + jason_data["articles"][i]["title"]+".")
    return ar

# arr=news()
# print(arr)