import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

bot = Bot(token="#")

dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
        await message.answer('Это была команда СТАРТ')


@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)


async def main():
    await dp.start_polling(bot)

asyncio.run(main())
