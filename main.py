#! /bin/python

from pprint import pprint
import telepot

from config import Config

def handle_msg(msg):
    pprint(msg)
    chat_id = msg['chat']['id']
    BOT.sendMessage(chat_id, 'Bạn vừa nói với mình là: \n```\n' + msg['text'] + '\n```\nphải không?')
    BOT.sendMessage(chat_id, 'Cơ mà NQA không có mặt ở đây để trả lời bạn đâu :)')

BOT = telepot.Bot(Config.BOT_TOKEN)
pprint(BOT.getMe())
BOT.message_loop(handle_msg, 0.1, 20, None, True, 3, True)
