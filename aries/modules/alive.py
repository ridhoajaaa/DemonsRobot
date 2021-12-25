from telethon import Button

from aries import telethn as tbot
from aries.events import register

PHOTO = "https://telegra.ph/file/d4e700cab0718eae3f8f6.jpg"


@register(pattern=("/alive|/ALIVE"))
async def awake(event):
    event.sender.first_name
    ARIES = "**Alo bang, saya DemonsRobot** \n\n"
    ARIES += "**ALL SYSTEM WORKING PROPERLY**\n\n"
    ARIES += " ☬ ⌊ **Python :** __3.9.7__ ⌉\n\n"
    ARIES += " ☬ ⌊ **Pyrogram :** __1.2.9__ ⌉\n\n"
    ARIES += " ☬ ⌊ **MongoDB :** __2.5.1__ ⌉\n\n"
    ARIES += " ☬ ⌊ **Platform :** __linux__ ⌉\n\n"
    ARIES += " ☬ ⌊ **My Lord** : [d̶d̶o̶x̶ ⸸ ƒ α ᴄ к [🇯🇵]](https://t.me/ddodxy) ☠⌉\n\n"
    ARIES += " ☬ ⌊ **TELETHON : 6.6.6 Latest** ⌉\n\n"
    ARIES += " |||| || ||| |||| || |||||| ||||| || || ||"
    BUTTON = [
        [
            Button.url("Support", "https://t.me/demonszxx"),
            Button.url("Owner", "https://t.me/ddodxy"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=ARIES, buttons=BUTTON)


__mod_name__ = "Alive"
