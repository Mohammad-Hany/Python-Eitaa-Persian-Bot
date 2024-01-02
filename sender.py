import requests
import schedule
import os

from time import sleep
from dotenv import load_dotenv

from manager import run


load_dotenv()

api_url = 'https://eitaayar.ir/api/' + os.getenv("EITAA_TOKEN")

def get_me():
    return requests.get(api_url + '/getme').json()
    
def send_message(chat_id, text):
    params = {
        'chat_id': chat_id,
        'text': text,
        # 'title': title,
        # 'notification_disable': notification_disable,
        # 'id_message_to_reply': id_message_to_reply,
        # 'date': date,
        # 'pin': pin,
        # 'viewCountForDelete': viewCountForDelete,
    }
    return requests.post(api_url + "/sendMessage", data=params).json()

def job():
    send_message('9516430', run())


schedule.every().day.at("06:00").do(job) 
schedule.every().day.at("12:00").do(job)
schedule.every().day.at("15:00").do(job)


while True:
    schedule.run_pending()
    sleep(1)