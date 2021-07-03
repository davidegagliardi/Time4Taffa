#!/usr/bin/env python
import os
import telegram

from database import getAllUsers
from menu import generate_message
from restaurant import opening
import requests

def dailyMenu():
    if opening():
        userlist = getAllUsers()
        users = [x[0] for x in userlist]
        for user in users:
            message = generate_message(user)
            bot = telegram.Bot(token=os.environ['TOKEN'])
            bot.sendMessage(chat_id=user, text=message)