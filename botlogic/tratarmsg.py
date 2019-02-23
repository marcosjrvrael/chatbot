#!/usr/bin/env
# -*- coding: utf-8 -*-
import time
import sys
import datetime
from datetime import datetime


class TratarMsg:
    def msgRecebida(self,text,chat,name,user,chatbot):
        text = text.split()
               
        #time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        def Horario(hour):
            hour = int(hour)
            if hour >= 12:
                return "Boa tarde"
            elif hour >= 18 and hour < 0:
                return "Boa noite"
            elif hour >= 0 and hour <= 5:
                return "Esse horario pede dormir, ou um café,"
            elif hour >= 6 and hour < 12:
                return "Bom dia"
        def text_valid(text):
            lista_word = ["sim","Sim","Bora","Demorou","bora","demorou","pode ser","podemos",
                    "Podemos","Pode ser"]
            for x in range(len(text)):
                if text[x] in lista_word:
                    text = text[x]
            return text
        
        lista_res = ["sim","Sim","Bora","Demorou","bora","demorou","pode ser","podemos",
                    "Podemos","Pode ser"]
        
        text = text_valid(text)

        if text in lista_res:
            return """Infelizmente ainda não consigo falar sobre nada
mas estou aprendendo e logo logo vamos bater altos papos!"""

        hour = datetime.now().strftime('%H')
        greetings = Horario(hour)
        text = """Olá\n{0} {1}\nSeu usuario {2} é legal
vamos bater um papo?""".format(greetings,name,user)

        return text

