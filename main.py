import telegram
import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#Variables
taffa_menu = "http://api.tf.fi/taffa/en/today/"
my_token = 'PlaceYourTokenHere'
chat = 'IdOfTheChat'

def get_menu(url=taffa_menu):
    data = requests.get(url)
    return data.text

def send(msg, chat_id=chat, token=my_token):
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text = "\n".join(msg))

def generate_message():
    msg = list()
    msg.append('Hey, time for Taffa❗')
    msg.append('Today\'s menu ⬇️')
    msg.append(" ")
    menu = get_menu()
    msg.append(menu)
    return msg

if __name__ == '__main__':
    message = generate_message()
    send(message)
