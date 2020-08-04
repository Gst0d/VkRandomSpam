# -*- coding: utf-8 -*-
from vk_messages import MessagesAPI
import random
from vk_messages.utils import get_random
login, password = 'Логин', 'Пароль'                                

messages = MessagesAPI(login=login, password=password)                                
slova = ['Я дубовая роща','Я купил себе пива']   
messages.method('messages.send', user_id='Сюда айпи жертвый', message=(random.choice(slova)),random_id=get_random()) #Отправляет сообщенией из массива "slova"
#Я не смог сделать цикл внутри одного скрипта, поэтому run.py зацикленно открывает bot.py и закрывает.
#Если вы смогли доработать скрипт, по возможности отправьте мне, чему то научусь. 
#Автор: Vk.com/Idelikme

