
import PySimpleGUI as sg
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty,InputPeerChannel,InputPeerUser
import sys,os
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon import functions, types


import random
import time
import subprocess
from pickle import dumps, load
import asyncio




async def doSearch(client, word):
    res = []
    res = await client(functions.contacts.SearchRequest(q=word,limit=100))
    return res




class feeder:
    def __init__(self, groupFrom, groupTo):
        self.groupFrom = groupFrom
        self.groupTo = groupTo



############## DECLARATION ####################
megaGroups=[]
groups=['486469468','469496846']
toSearch = ""
newToSearch = ""
result=[]
resultChats=[]
voyelles= ['a','e','i','o','u']
consonnes=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']


api_id = Your_API_Id
api_hash = 'Your_API_HASH'
phone = 'YOUR_PHONE_NUMBER'
client = TelegramClient(phone, api_id, api_hash)
client.connect()




################# Main window #######################
connection_column = [
    [sg.Button("Search")]

]


list_group=[
    [sg.InputText(key="-Word-")],
    [sg.Listbox(values=[], enable_events=True,size=(50,20),key="-SearchResult-", no_scrollbar= False)]
]



layout =[
    [
    sg.Column(connection_column),
    sg.Column(list_group)
    ]
]


window = sg.Window("titre", layout)


if not client.is_user_authorized():
		client.send_code_request(phone)
		client.sign_in(phone, input('Enter the code: '))




async def main():
# LOOP
    while True:
        event, values = window.read()

        if event=="Search":
            toSearch = values["-Word-"]
            print(toSearch)

            result = await doSearch(client,toSearch)
            for r in result.chats:
                resultChats.append(r)

            ########################## voyelles avant
            for v in voyelles:
                newToSearch = toSearch + v
                print("new to search" + toSearch)
                result=await doSearch(client,newToSearch)
                print("nouveau résultats : " + str(len(result.chats)))

                for r in result.chats:
                    resultChats.append(r)

            ########################## consonne après
            for c in consonnes:
                newToSearch = toSearch + c
                print("new to search" + toSearch)
                result=await doSearch(client,newToSearch)
                print("nouveau résultats : " + str(len(result.chats)))

                for r in result.chats:
                    resultChats.append(r)

            titlesToDisplay = []
            for r in resultChats:
                titlesToDisplay.append(r.title)

            window.Element('-SearchResult-').Update(values=titlesToDisplay)


        #fermeture fenetre
        if event == sg.WIN_CLOSED:
            break;

    await client.disconnect()
    window.close()

with client:
    client.loop.run_until_complete(main())










