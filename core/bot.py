import os
import telebot


class Bot:
    chat_nizkopal = 147212481
    chat = -1001667872524

    def __init__(self):
        assert os.getenv("BOT_TOKEN"), "Please, setup BOT_TOKEN with a bot token."
        self.bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

    def send_message_to_nizkopal(self, message):
        self._send_message(self.chat_nizkopal, message)

    def send_message_to_chat(self, message):
        self._send_message(self.chat, message)

    def _send_message(self, chat_id, message):
        self.bot.send_message(chat_id, message)

    def get_updates(self, offset):
        return self.bot.get_updates(offset)


bot = Bot()
