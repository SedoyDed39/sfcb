# import logging
# from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.middlewares.logging import LoggingMiddleware
# from aiogram.types import ParseMode
# import openai

# BOT_TOKEN = '6363744739:AAFhF3XK6nHcudCjOI9me_2mz3raE2FWktU'
# openai.api_key = '8Dsh90rKvpWZEiQ2VxEoReb_OjQ_A9g3cwg_FcLhhIE'
# openai.api_base = "https://chimeragpt.adventblocks.cc/api/v1"

# MODEL_NAME = 'gpt-4'
# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher(bot)
# dp.middleware.setup(LoggingMiddleware())
# message_count = 0


# @dp.message_handler(commands=['start'])
# async def on_start(message: types.Message):
#     await message.reply("Прив, я чат бот короче на базе гпт")


# @dp.message_handler(content_types=types.ContentTypes.TEXT)
# async def generate_response(message: types.Message):
#     global message_count
    
#     ans_style1 = ""
#     user_input = message.text
#     is_reply = message.reply_to_message is not None

#     message_count += 1

#     if message_count % 100 == 0 or is_reply:

#         response = openai.ChatCompletion.create(
#             model=MODEL_NAME,
#             messages=[
#                 {'role': 'user', 'content':ans_style1 + user_input},
#             ],
#         )

#         bot_response = response['choices'][0]['message']['content']

#         await message.reply(bot_response, parse_mode=ParseMode.HTML)

# if __name__ == '__main__':
#     logging.basicConfig(level=logging.INFO)

#     from aiogram import executor
#     executor.start_polling(dp, skip_updates=True)
