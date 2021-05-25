import constants as keys
import logging
from telegram.ext import *
import response as R
import requests
import json

print("Bot is starting")



def fucnforstate(no):
    #print("enter Your statename :")
    res = "Let's see your districtcode And Then Use it to konw the Vaccine slots : \n\n"
    res += R.District_List(no)
    return res

def list():
    res = 'Heyy!!\n Here Just type : state_list\nThen type the code of state then you will get the list of \ndistricts with their district_id\nHave Fun :)'
    return res
def start_command(update, context):
    res = R.myfuc()
    update.message.reply_text(res)

def help_command(update, context):
    
    update.message.reply_text(list())

def handle_message(update, context):
    text = str(update.message.text).lower()
    user = update.effective_user
    if(text=='state_list'):
        resp = R.ListOfState()
        update.message.reply_text(resp)
        return
    
    if(len(text)<=2 and len(text)>0 and (text[0]>='1' and text[1]<='3') and int(text)<=36 and int(text)>0 ):
        let = int(text)
        resp = fucnforstate(let)
        update.message.reply_text(resp)
        return
    
    response = R.sample(text)
   
    #print(response[0])
    if(len(response)==1):
        update.message.reply_text(response[0])
        return
    if(response[0]=='I' and response[1]=='n' and response[2]=='v'):
        res = ''
        for i in response:
            res+=i
        update.message.reply_text(res)    
    else:    
        for i in response :
            update.message.reply_text(i)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    # dp.add_handler(CommandHandler("vaccine", vaccine_command))
    #dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
