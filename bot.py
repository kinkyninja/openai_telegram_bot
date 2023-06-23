from aiogram import Bot, Dispatcher, executor, types
import openai

tg_bot_token = " " # put your telegram token from @botfather
openai.api_key = " " # put your openai token here
bot = Bot(token=tg_token) 
dp = Dispatcher(bot)

@dp.message_handler()
async def get_openai_reply(message: types.Message):
    instruction = message.text
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": instruction}])
    await message.answer(completion.choices[0].message["content"])

executor.start_polling(dp, skip_updates=True)