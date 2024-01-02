import os
import redis
from random import randint
from dotenv import load_dotenv


def load_vocab():
    """ Read all of words of redis database and save on a list """
    for word in redis_client.keys("*"):
        if word.decode('utf-8') != "number_sent":
            definition = redis_client.hget(word, 'definition')
            gride = redis_client.hget(word, 'gride')
            is_send = redis_client.hget(word, 'is_send')

            if definition:
                word_data.append((word, definition.decode('utf-8'), gride.decode('utf-8'), is_send.decode('utf-8')))
        
    return word_data


# Management Words
def get_word():
    """ Find a random word """
    result = []
    while len(result) < 3:
        data = word_data[randint(0, len(word_data)-1)]
        word, definition, gride, is_send = data[0], data[1], data[2], data[3]

        if is_send == 'False':
            redis_client.hset(word, 'is_send', 'True')

            number_sent = int(redis_client.get('number_sent').decode('utf8')) + 1
            redis_client.set("number_sent", number_sent)

            no = f'{number_sent}/{redis_client.dbsize() - 1}'
            
            result.append((word.decode("utf-8"), definition, gride, no))

    return result


def run():
    load_dotenv()
    global redis_client, word_data 

    # redis_client = redis.StrictRedis(host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"), db=0)  
    redis_client = redis.StrictRedis(host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"), password=os.getenv("REDIS_PASSWORD"), db=0)

    word_data = []

    load_vocab()
    return get_word()

run()