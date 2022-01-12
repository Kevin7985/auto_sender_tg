from pyrogram import Client
import csv
from time import sleep

from config import *

username = "username"
chat = "chat title / username"

def lastChatMessage(app, chatID):
    for dialog in app.iter_dialogs():
        if (dialog.chat.id == chatID):
            return dialog.top_message.text

f = open("input.csv", "r", encoding = "utf-8")
reader = csv.reader(f)
with (Client(username, apiID, apiHash)) as app:
    chatID = None
    for dialog in app.iter_dialogs():
        if (dialog.chat.username == chat):
            chatID = dialog.chat.id
            break

    header = False
    for item in reader:
        if not header:
            header = True
            continue

        #### Your writing steps if you write to bot ####

        # app.send_message(chatID, "/start")
        # sleep(2)
        # app.send_message(chatID, item[0])
        # sleep(2)
        # app.send_message(chatID, item[1])
        # sleep(2)
        # app.send_message(chatID, item[2])
        # ans = lastChatMessage(app, chatID)
        # if (ans != "Предмет"):
        #     inp = input("Correct? (Just press Enter): ")
        # sleep(1)
        # app.send_message(chatID, item[3])
        # ans = lastChatMessage(app, chatID)
        # if (ans != "Преподаватель"):
        #     inp = input("Correct? (Just press Enter): ")
        # sleep(1)
        # app.send_message(chatID, item[4])
        # ans = lastChatMessage(app, chatID)
        # if (ans != "Ссылка vk (личная)"):
        #     inp = input("Correct? (Just press Enter): ")
        # sleep(1)
        # app.send_message(chatID, item[5])
        # sleep(2)
        # app.send_message(chatID, item[6])
        # sleep(2)
        # app.send_message(chatID, item[7])
        # sleep(2)
        # app.send_message(chatID, item[8])
        # sleep(2)
        # app.send_message(chatID, item[9])
        # sleep(2)
        # app.send_message(chatID, item[10])
        # sleep(6)