from pyrogram import Client
import csv

from config import *

username = "username"
chat = "chat title / username"

with (Client(username, apiID, apiHash)) as app:
    chatID = None
    for dialog in app.iter_dialogs():
        if (dialog.chat.username == chat):
            chatID = dialog.chat.id
            break
    print(chatID)