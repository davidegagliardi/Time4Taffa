import telegram
import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import datetime

url = 'https://kitchen.kanttiinit.fi/restaurants?ids=3'

def opening():
    data = requests.get(url).json()
    return data[0]['openingHours'][datetime.datetime.today().weekday()]