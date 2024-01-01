import requests
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


while True:
    send_message('9516430', run())
    sleep(10)

