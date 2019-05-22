#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging, os, subprocess

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, InlineQueryHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def start(bot, update):
        update.message.reply_text("HI, saya adalah MPD bot")

def mpc_callback(bot, update, args):
    user_says = " ".join(args)
    print (user_says)
    mpcout = os.popen("/home/harry/mpc/func_" + user_says).read()
    if mpcout:
        print (mpcout)
        update.message.reply_text("<b>" + mpcout + "</b>", parse_mode='HTML', quote=False)

def echo(bot, update):
    global s
    s = ""
    words = update.message.text
    words = words.lower()
    res = words.split()
    if words == "mpc": 
        print ("usage mpc blabla")
        update.message.reply_text("<b>Usage mpc blablabla</b>", parse_mode='HTML')
        return
    if not "mpc" in words: return
    #print ("The list of words is : " +  str(res))
    for i in range (0, len (res)):
        #print (res[i])
        s += res[i] + " "
    print (s)
    mpcout = os.popen("/home/harry/mpc/func_" + s).read()
    if mpcout:
        print (mpcout)
        update.message.reply_text("<b>" + mpcout + "</b>", parse_mode='HTML', quote=False)
                     

def main():
    try:
        with open("token.txt", "r") as file:
            token = file.read().strip()

        if not token:
            logging.info("Token file is empty!")
            raise SytemExit

    except FileNotFoundError:
        logging.info("Token file not found!")
        raise SystemExit

    updater = Updater(token)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler("mpc", mpc_callback, pass_args=True))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, echo), group=0)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
