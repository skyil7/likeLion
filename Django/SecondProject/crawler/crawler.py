import requests
from bs4 import BeautifulSoup

temparr = []
datearr = []
dict = {}

def getTemp():
    response = requests.get("https://weather.naver.com/rgn/townWetr.nhn?naverRgnCd=09140104").text

    soup = BeautifulSoup(response,'html.parser')

    temp = soup.select('.nm .temp')

    for i in temp:
        temparr.extend(i.contents)

    return temparr
