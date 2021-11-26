from math import floor
from html import escape
from random import choice
from asyncio import sleep
from .. import loader, utils
from datetime import timedelta
from urllib.parse import quote_plus
from telethon.tl.types import Message
from telethon import events, functions, types, sync
from telethon.tl.functions.users import GetFullUserRequest
from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl.functions.account import UpdateProfileRequest, UpdateUsernameRequest
import asyncio, datetime, inspect, io, json, logging, os, threading, time, random, re, requests, urllib.parse

class MegaMod(loader.Module):
    """MegaMod"""
    strings = {'name': 'Mega'}

    async def watcher(self, message):
        bak = {449434040}
        chat = message.chat_id
        chatid= str(message.chat_id)
        chatik = -435123440
        duel = self.db.get('Дуэлька', 'duel', {})
        jb = "jaba"
        lvl = False
        name = self.me.first_name
        ninja = {-1001733976889, -1001745450607, -1001658628295}

        if chat in ninja:
            if message.sender_id not in {1124824021}:
                if "начать клановую войну" in message.message.casefold():
                    aaa = ""
                    id = 449434040
                    async with message.client.conversation(chat) as conv:
                        response = await conv.wait_event(events.NewMessage(incoming=True, from_users=1124824021, chats=message.chat_id))
                        if "Ваш клан уже" in response.text:
                            aaa =  f"<i>{message.sender.first_name} в поиске</i>"
                            rret = await self.client.get_messages(chatik, ids=id)
                            await rret.edit(aaa)
                    await message.client.send_message(chatik, aaa)
       
