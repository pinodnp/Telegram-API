#!/usr/bin/env python
# coding: utf-8

# # Connecting to my Telegram Account and getting the Bot ready

import configparser
import json
import sys
import asyncio
import os
import requests
import telegram

from telethon import sync
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.types import (PeerChannel)
from telethon.tl.functions.messages import (GetHistoryRequest)


api_id = #Put here your api_id
api_hash = #Put here your api_hash

phone= #Put here the phone linked to your telegram account

messages_sent=[]
messages_received=["This is a list of all messages received from the messages sent"]

global bot
global TOKEN

TOKEN=#Put here your token
bot=telegram.Bot(token=TOKEN)


# ### Getting the client (No need to run this code more than once, if it gives errors just change the string in telegram client for something else

client = TelegramClient("Your client name here", api_id, api_hash)
await asyncio.sleep(2)
await client.start()

print("Client Created")
 
#Ensure you're authorized
if not client.is_user_authorized():
    client.send_code_request(phone)
    try:
        client.sign_in(phone, input('Enter the code: '))
    except SessionPasswordNeededError:
        client.sign_in(password=input('Password: '))
        


# ### Getting the message from the user account

from apscheduler.schedulers.asyncio import AsyncIOScheduler
import apscheduler.schedulers.blocking

sched= AsyncIOScheduler()

async def getting_text():
    global time
    global location
    global horse
    global target_odds
    global bet_size
    global new_message
    
    username = await client.get_entity('put your bot name here')
    messages=[]
    await asyncio.sleep(1) 
    async for message in client.iter_messages(username, 1):
        messages.append(message.text)
        continue

    new_message= message[0]

    print(new_message)
    
 
sched.add_job(getting_text, 'interval', seconds=5)
sched.start()

#to manually stop the code
sched.shutdown()


# # Code for sending the messages using the Telegram Bot 


async def sending_message():
    if len(messages_sent)==0:
        bot.sendMessage(chat_id="Put here id of the chat you want to send message to", text=new_message)
        last_message=new_message
        print("first message sent")


    elif messages_sent[-1]==new_message:
        print("no new messages")


    elif messages_sent[-1]!=new_message:
        bot.sendMessage(chat_id="Put here id of the chat you want to send message to", text=new_message)
        last_message=new_message
        print("new bet sent")


    try:
        messages_sent.append(last_message) 

    except:
        ("there are not previous messages, wait until next message")

    
sched.add_job(sending_message, 'interval', seconds=5)
sched.start()


#to manually stop the code
sched.shutdown()





