import constants as keys
import logging
from telegram.ext import *
import response as R
import requests
import json
import datetime 
    


print("Bot is starting")




def send_message_telegram(message):
    final_telegram_url = keys.api_url_telegram.replace(("__groupid__"), keys.group_id)
    final_telegram_url = final_telegram_url + message
    #print(message)
    response = requests.get(final_telegram_url , headers = keys.browser_header)
    #print(response)

def Runalways():
    current_time = datetime.datetime.now() 

    text = '396:'
    text=text+str(current_time.day)+'-'+str(current_time.month)+'-'+str(current_time.year)
    response = R.sample(text)
      
    for i in response :
        if(i!='Slots Not Available for the selected District and date'):
            send_message_telegram(i)

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
    
    if(len(text)<=2 and len(text)>0 and (text[0]>='1' and text[0]<='9') and int(text)<=36 and int(text)>0 ):
        let = int(text)
        resp = fucnforstate(let)
        update.message.reply_text(resp)
        return
    
    response = R.sample(text)
   
    #print(response[0])
      
    for i in response :
        update.message.reply_text(i)


def error(update, context):
    print(f"Update {update} caused error {context.error}")

Runalways()

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

