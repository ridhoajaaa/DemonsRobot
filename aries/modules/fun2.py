# this module only Created in @VegetaRobot ©pegasusXteam

import html
import random
import re

import requests as r
from telegram import MAX_MESSAGE_LENGTH, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, Filters, run_async
from telegram.utils.helpers import escape_markdown

import aries.modules.fun_strings as fun
from aries import DEMONS, DRAGONS, dispatcher
from aries.modules.disable import DisableAbleCommandHandler, DisableAbleMessageHandler
from aries.modules.helper_funcs.alternate import typing_action
from aries.modules.helper_funcs.extraction import extract_user

GN_IMG = "https://telegra.ph/file/1ba41195de67f318fed43.jpg"


@run_async
@typing_action
def goodnight(update, context):
    message = update.effective_message
    first_name = update.effective_user.first_name
    reply = f"*Hey {escape_markdown(first_name)} \nGood Night! 😴*"
    message.reply_photo(GN_IMG, reply, parse_mode=ParseMode.MARKDOWN)


GM_IMG = "https://telegra.ph/file/45fde647ddc20dc75574b.jpg"


@run_async
@typing_action
def goodmorning(update, context):
    message = update.effective_message
    first_name = update.effective_user.first_name
    reply = f"*Hey {escape_markdown(first_name)} \n Ohayo Onii Chan!☀*"
    message.reply_photo(GM_IMG, reply, parse_mode=ParseMode.MARKDOWN)


@run_async
def gbun(update, context):
    user = update.effective_user
    chat = update.effective_chat

    if update.effective_message.chat.type == "private":
        return
    if int(user.id) in DRAGONS or int(user.id) in DEMONS:
        context.bot.sendMessage(chat.id, (random.choice(fun.GBUN)))


@run_async
def gbam(update, context):
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    message = update.effective_message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        gbam_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(gbam_user.first_name)

    else:
        user1 = curr_user
        user2 = bot.first_name

    if update.effective_message.chat.type == "private":
        return
    if int(user.id) in DRAGONS or int(user.id) in DEMONS:
        gbamm = fun.GBAM
        reason = random.choice(fun.GBAM_REASON)
        gbam = gbamm.format(user1=user1, user2=user2, chatid=chat.id, reason=reason)
        context.bot.sendMessage(chat.id, gbam, parse_mode=ParseMode.HTML)


@run_async
def decided(update: Update, context: CallbackContext):
    reply_text = (
        update.effective_message.reply_to_message.reply_text
        if update.effective_message.reply_to_message
        else update.effective_message.reply_text
    )
    reply_text(random.choice(fun.DECIDE))


@run_async
@typing_action
def repoo(update, context):
    update.effective_message.reply_text(fun.REPO)


@run_async
def abuse(update, context):
    context.bot.sendChatAction(
        update.effective_chat.id, "typing"
    )  # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
        message.reply_to_message.reply_text(random.choice(fun.ABUSE_STRINGS))
    else:
        message.reply_text(random.choice(fun.ABUSE_STRINGS))


GOODMORNING_HANDLER = DisableAbleMessageHandler(
    Filters.regex(r"(?i)(goodmorning|good morning)"),
    goodmorning,
    friendly="goodmorning",
)
GOODNIGHT_HANDLER = DisableAbleMessageHandler(
    Filters.regex(r"(?i)(goodnight|good night)"), goodnight, friendly="goodnight"
)
DECIDED_HANDLER = DisableAbleCommandHandler("decided", decided)

REPOO_HANDLER = DisableAbleCommandHandler("repoo", repoo)

GBUN_HANDLER = CommandHandler("gbun", gbun)
GBAM_HANDLER = CommandHandler("gbam", gbam)
ABUSE_HANDLER = DisableAbleCommandHandler("abuse", abuse)

dispatcher.add_handler(GOODMORNING_HANDLER)
dispatcher.add_handler(GOODNIGHT_HANDLER)
dispatcher.add_handler(ABUSE_HANDLER)
dispatcher.add_handler(GBAM_HANDLER)
dispatcher.add_handler(GBUN_HANDLER)
dispatcher.add_handler(DECIDED_HANDLER)
dispatcher.add_handler(REPOO_HANDLER)


# guys this it you like PegasusXteam ask join @allbefin
# © PegasusXteam
