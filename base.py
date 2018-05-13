import random
from os.path import dirname, abspath, join

from dinoralite import *


BASE_DIR = dirname(abspath(__file__))

bot = Bot("Дарина")
bot.learn_from_dir(join(BASE_DIR, 'dinoralite/models/'))


def bot_randint(start, end):
    return str(random.randint(int(start), int(end)))


bot.add_answer_fn("randint", bot_randint)
