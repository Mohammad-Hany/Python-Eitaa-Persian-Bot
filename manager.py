import os
import redis
from random import randint
from dotenv import load_dotenv

from vocabs import vocabs_information


def load_vocab():
    for word in redis_client.keys("*"):
        definition = redis_client.hget(word, 'definition')
        is_send = redis_client.hget(word, 'is_send')

        if definition:
            word_data.append((word, definition.decode('utf-8'), is_send.decode('utf-8')))

    return word_data

def save_vocab():
    for key in redis_client.keys("*"):
        redis_client.delete(key)

    for word, definition in vocabs_information:
        redis_client.hset(word, 'definition', definition)
        redis_client.hset(word, 'is_send', "False")


# Management Words
def get_word():
    while True:
        word = word_data[randint(0, len(word_data)-1)]
        if word[2] == 'False':
            redis_client.hset(word[0], 'is_send', 'True')
            print('   ', f'{word[0].decode("utf-8")}: {word[1]}')
            return f'{word[0].decode("utf-8")}: {word[1]}'

        print('   Word is already')


def run():
    load_dotenv()
    global redis_client, word_data
    redis_client = redis.StrictRedis(host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"), db=0)
    word_data = []

    # save_vocab()
    load_vocab()
    return get_word()

run()