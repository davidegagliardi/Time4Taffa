import telegram
import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from database import getLanguage

from restaurant import opening

def get_today_menu(lang):
    url = "http://api.tf.fi/taffa/"+lang+"/today/"
    data = requests.get(url)
    return data.text

def generate_message(chat_id):
    lang = getLanguage(chat_id)
    msg = list()
    if opening():
        if lang == "en":
            msg.append('Hey, time for Taffa❗')
            open = 'Opening hours: ' + opening()
            msg.append(open)
            msg.append('Today\'s menu ⬇️')
        if lang == "fi":
            msg.append('Hei, aika Taffalle❗')
            open = 'Aukioloajat: ' + opening()
            msg.append(open)
            msg.append('Tämän päivän valikko ⬇️')
        if lang == "sv":
            msg.append('Hej, dags för Taffa❗')
            open = 'Öppettider: ' + opening()
            msg.append(open)
            msg.append('Dagens meny ⬇️')
        msg.append(" ")
        msg.append(get_today_menu(lang))
    else:
        if lang == "en":
            msg.append('Hey, Taffa is closed❗')
        if lang == "fi":
            msg.append('Hei, Taffa on suljettu❗')
        if lang == "sv":
            msg.append('Hej, Taffa är stängd❗')
    message = "\n".join(msg)
    return message