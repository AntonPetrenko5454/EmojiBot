from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentType
from aiogram.utils import executor
from aiogram.utils.emoji import emojize

from config import TOKEN
from dict import dictionary
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
words=open('words.txt').readlines()

@dp.message_handler(commands=['Start','Начать'])
async def startCommands(message: types.Message):
    await message.answer('Hello')

def findEmoji(text):

    foundEmoji={}
    for i in range(len(words)):




@dp.message_handler()
async def getMessage(message: types.Message):
    print(message)
    if message.text=='Привет':
        await message.answer(emojize('Привет :grinning:'))

    if 'как дела' in message.text.lower():
        await message.answer('Нормально')
        await bot.send_sticker(message.chat.id,'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
        await message.reply('А твои?')
@dp.message_handler(content_types=ContentType.ANY)
async def getSticker(message: types.Message):
    print(message)





if __name__ == '__main__':
    executor.start_polling(dp)