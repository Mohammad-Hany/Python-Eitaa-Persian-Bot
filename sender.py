import requests
import os

from time import sleep
from dotenv import load_dotenv
from datetime import datetime, time

from manager import run


load_dotenv()

api_url = 'https://eitaayar.ir/api/' + os.getenv("EITAA_TOKEN")

def get_me():
    return requests.get(api_url + '/getme').json()
    
def send_message(chat_id, text):
    params = {
        'chat_id': chat_id,
        'text': text,
    }
    return requests.post(api_url + "/sendMessage", data=params).json()


while True:
    target_time = time(2, 30)
    current_time = datetime.now().time()

    if (current_time >= target_time and current_time <= target_time.replace(second=3)):
        for item in run():
            word, definition, gride, no = item[0], item[1], item[2], item[3]
            send_message('9516430', f'{word}: {definition}\n{gride}#     {no}')

            print('   ', f'{word}: {definition} --- #{gride} --- {no}')

    

    print("Waiting....")
    sleep(1)