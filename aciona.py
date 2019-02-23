#!/usr/bin/env
# -*- coding: utf-8 -*-
import time
import sys
from botcore.chatbot import ChatBot
from botlogic.tratarmsg import TratarMsg

chatbot = ChatBot()
msg = TratarMsg()

def main():
    #last_textchat = (None, None)
    last_update_id = None
    while True:
        updates = chatbot.get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = chatbot.get_last_update_id(updates) + 1
            text, chat, name, user = chatbot.echo_all(updates)
            text = msg.msgRecebida(text,chat,name,user,chatbot)
            chatbot.send_message(text,chat)
        time.sleep(0.5)

if __name__ == '__main__':
    main()



