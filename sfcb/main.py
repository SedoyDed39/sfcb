from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentType
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import pymorphy2
import re
import random
import logging

import config 
morph = pymorphy2.MorphAnalyzer()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
sticker_chance = 0.2 


message_counter = 0

@dp.message_handler(content_types=ContentType.TEXT)
async def ht(message: types.Message):
    global message_counter
    message_counter += 1

    text = message.text.lower()
    words = re.findall(r'\b\w+\b', text)

    has_noun = False
    for word in words:
        parsed_word = morph.parse(word)
        if "NOUN" in parsed_word[0].tag:
            has_noun = True
            break

    if message_counter % 50 == 0:

        response = random.choice(config.STICKER_LIST)
        await message.reply_sticker(response)
    elif message_counter % 75 == 0 and has_noun:

        for word in words:
            parsed_word = morph.parse(word)
            if "NOUN" in parsed_word[0].tag:
                response, case = random.choice(config.responses)
                plural_form = parsed_word[0].inflect({case})
                if plural_form:
                    response = response.format(plural_form=plural_form.word)
                    await message.reply(response)
                    break

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp)