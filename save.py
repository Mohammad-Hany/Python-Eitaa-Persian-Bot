import os
import redis
from dotenv import load_dotenv

from vocabs import vocabs_information

load_dotenv()
try:
    redis_client = redis.StrictRedis(host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"), db=0)
except:
    redis_client = redis.StrictRedis(host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"), password=os.getenv("REDIS_PASSWORD"), db=0)
    print('on server')

def save_vocab():
    """ Delete all of words data and then save all of words """

    for key in redis_client.keys("*"):
        redis_client.delete(key)

    redis_client.set("number_sent", 0)

    for word, definition, gride in vocabs_information:
        redis_client.hset(word, 'definition', definition)
        redis_client.hset(word, 'gride', gride)
        redis_client.hset(word, 'is_send', "False")

    print("The words were successfully saved in the database.")

if __name__ == "__main__":
    save_vocab()