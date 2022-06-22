import random

from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentType
from aiogram.utils import executor
from aiogram.utils.emoji import emojize

from config import TOKEN
from dict import dictionary
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
words = [line.strip().split(';') for line in open('words.txt', encoding='UTF-8').readlines()]

@dp.message_handler(commands=['Start','Начать'])
async def startCommands(message: types.Message):
    await message.answer('Hello')

def findEmoji(text):
    str=''

    foundEmoji={}
    #Позиция и код эмоджи
    for i in range(len(words)):
        for y in range(len(words[i])):
            x= text.find(words[i][y])
            if x!=-1:

                foundEmoji[x]=[random.choice(dictionary[i]),len(words[i][y])]
    keys=list(foundEmoji.keys())
    print(keys)
    str+=text[0:keys[0]]
    pre=keys[0]
    for i in range(len(keys)):
        str+=text[keys[i]:foundEmoji[keys[i]][1]+keys[i]]
        str+=foundEmoji[keys[i]][0]
        if i<len(keys)-1:
            str+=text[pre:keys[i+1]]
        pre=keys[i]+1
    str+=text[pre:len(text)]
    return str






@dp.message_handler()
async def getMessage(message: types.Message):
    print(message)
    '''###if message.text=='Привет':
        await message.answer(emojize('Привет :grinning:'))

    if 'как дела' in message.text.lower():
        await message.answer('Нормально')
        await bot.send_sticker(message.chat.id,'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
        await message.reply('А твои?')'''
    await message.answer(emojize(findEmoji(message.text.lower())))
@dp.message_handler(content_types=ContentType.ANY)
async def getSticker(message: types.Message):
    print(message)





if __name__ == '__main__':
    executor.start_polling(dp)