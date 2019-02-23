#!/usr/bin/env
# -*- coding: utf-8 -*-
import json
import requests
import sys

TOKEN = #coloque seu token aqui
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

class ChatBot:
    def get_url(self,url):
        response = requests.get(url)
        content = response.content.decode("utf-8")
        return content

    def get_json_from_url(self,url):
        content = self.get_url(url)
        js = json.loads(content)
        return js
 
    def get_updates(self,offset=None):
        url = URL + "getUpdates?timeout=50" 
        if offset:
            url += "&offset={}".format(offset)
        js = self.get_json_from_url(url)
        return js

    def get_last_update_id(self,updates):
        update_ids = []
        for update in updates["result"]:
            update_ids.append(int(update["update_id"]))
        updatefim = max(update_ids)
        return updatefim

    
    def echo_all(self,updates):
        #updates = updates["id"]
        for update in updates["result"]:
        #update = updates
            try:
                text = update["message"]["text"]
                chat = update["message"]["chat"]["id"]
                name = update["message"]["from"]["first_name"]
                user = update["message"]["from"]["username"]
                #text = msg.verificaMsg(text,)
                #self.send_message(text, chat)
                return text,chat,name,user
            except Exception as e:
                print(e)

    def send_message(self,text, chat_id):
        #url = URL + "sendMessage?text={}&chat_id={}".format(text.encode('utf-8'), chat_id)
        url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
        self.get_url(url)

