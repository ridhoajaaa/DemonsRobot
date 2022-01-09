import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from aries.events import register
from aries import telethn as tbot


PHOTO = "https://telegra.ph/file/d4e700cab0718eae3f8f6.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**P KTL [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm 𝕯𝖊𝖒𝖔𝖓𝖘 ✘ 𝕽𝖔𝖇𝖔𝖙.** \n\n"
    TEXT += "⚪ **I'm Working Properly** \n\n"
    TEXT += f"⚪ **My Master : [𝗬𝗲𝘀𝗶𝗱𝗼. 🇮🇶](https://t.me/ddodxy)** \n\n"
    TEXT += f"⚪ **Library Version :** `{telever}` \n\n"
    TEXT += f"⚪ **Telethon Version :** `{tlhver}` \n\n"
    TEXT += f"⚪ **Pyrogram Version :** `{pyrover}` \n\n"
    TEXT += "**Thanks For Adding Me Here ❤️**"
    BUTTON = [
        [
            Button.url("Help", "https://t.me/demoonsssss_bot?start=help"),
            Button.url("Support", "https://t.me/demonszxx"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
