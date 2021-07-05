#!/usr/bin/env python
import logging
import sqlite3
from sqlite3 import Error

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup

# DB Connection
def loadDB():
    conn = sqlite3.connect('content.sqlite')
    cur = conn.cursor()
    conn.text_factory = str
    cur.executescript('''CREATE TABLE IF NOT EXISTS userdata
    (
    chat_id TEXT NOT NULL PRIMARY KEY UNIQUE, 
    language TEXT);'''
    )
    conn.commit()
    conn.close()

def checkUser(update, id):
    conn = sqlite3.connect('content.sqlite')
    cur = conn.cursor()
    conn.text_factory = str
    if len(cur.execute('''SELECT chat_id FROM userdata WHERE chat_id = ?        
            ''', (id,)).fetchall())>0:
        print('Existing user')
    else:
        cur.execute('''INSERT OR IGNORE INTO userdata (chat_id, language) VALUES (?, ?)''', \
        (id, "en",))
        print('Create new user with EN by default')
    conn.commit()
    conn.close()

def delUser(update, id):
    conn = sqlite3.connect('content.sqlite')
    cur = conn.cursor()
    conn.text_factory = str
    if len(cur.execute('''SELECT chat_id FROM userdata WHERE chat_id = ?        
            ''', (id,)).fetchall())>0:
        print('Existing user')
        cur.execute('''DELETE FROM userdata WHERE chat_id = ?''', \
                    (id,))
        print('Deleted')
    else:
        print('Chat ID not in DB')
    conn.commit()
    conn.close()

def updateLanguage(update, id, lang):
    # Updates user info as inputted.
    conn = sqlite3.connect('content.sqlite')
    cur = conn.cursor()
    conn.text_factory = str
    # Update SQLite database as needed.
    cur.execute('''UPDATE OR IGNORE userdata SET language = ? WHERE chat_id = ?''', \
        (lang, id,))
    print("Setting", lang, "for chat id ", id)
    conn.commit()
    conn.close()

def getLanguage(id):
    conn = sqlite3.connect('content.sqlite')
    cur = conn.cursor()
    conn.text_factory = str
    c = cur.execute('''SELECT language FROM userdata WHERE chat_id = ?''', \
        (id,))
    lang = c.fetchone()[0]
    print("Language for the user is", lang)
    return lang
    conn.close()

def getAllUsers():
    conn = sqlite3.connect('content.sqlite')
    cur = conn.cursor()
    conn.text_factory = str
    sqlstr = "SELECT chat_id FROM userdata"
    cur.execute(sqlstr)
    print("Ritorno gli utenti")
    return cur.fetchall()

