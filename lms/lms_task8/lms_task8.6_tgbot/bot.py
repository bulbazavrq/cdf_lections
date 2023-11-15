from aiogram import Bot, Dispatcher, executor, types

#
from config import calc1
# print(calc1())
#

API_TOKEN = '6444948282:AAFEjZuIskPEQuvy-d0sM7lm9ut49Wf0szY'
 
 
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
 
 
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hello world!")
 
 
@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Чем я могу помочь?")
 
 


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)
############################################
# a = []
# @dp.message_handler() #1+1
# async def send_welcome(message: types.Message):
    
#     # a = int(message.text)
#     # b = int(message.text)
#     # c = [a, b]
#     # await message.answer(c)    
#     await message.answer()
    # await message.reply(calc1(a))


# @dp.message_handler(commands=['calc'])
# async def send_welcome(message: types.Message):
#     await message.reply("a, b; +, -")

# @dp.message_handler()
# # async def a_value(msg: types.Message):
# #     await msg.answer(f'{msg} - a')

# # @dp.message_handler()
# # async def a_value(msg: types.Message):
# #     await msg.answer(f'{msg} - b')
# @dp.message_handler()
# async def test3(a: types.Message):
#     await bot.send_message(a)
# Этот декоратор будет реагировать на
# сообщения что вы присылали боту.
# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     a = msg.text
#     # b = input()
    
#     # В переменной msg.text
#     # содержится текст сообщения
#     # a = int(msg)
#     await bot.send_message(msg.from_user.id, a)



# bot.send_message(id,'123')
# Этот декоратор будет реагировать на
# сообщения что вы присылали боту.
# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     # В переменной msg.text
#     # содержится текст сообщения
#     await bot.send_message(msg.answer('asd'))

# print(a+1)


# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)

# @dp.message_handler()
# async def test1(message: types.Message):
#     await message.answer(message.text)
#     await message.answer(calc1())
 
 
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
