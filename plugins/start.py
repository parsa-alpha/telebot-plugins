import sspps
import telebot
from telebot import types
import json
import os
import config

bot = telebot.TeleBot(config.token)
class start(sspps.Plugin):
    enabled = True
    def __init__(self):
        plugin_name = 'start'
        print ("pligin " + plugin_name + " activated")
    def activate(self):
        @bot.message_handler(commands=['start'])
        def send_welcome(message):
            bot.reply_to(message, "plugin is running")

        @bot.message_handler(func=lambda message: True)
        def echo_all(message):
            bot.reply_to(message, message.text)

        bot.polling()
#by parsa alemi