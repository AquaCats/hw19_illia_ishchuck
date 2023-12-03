import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.utils.markdown import hbold

logging.basicConfig(level=logging.INFO)

bot = Bot(token="6975984623:AAGPuUMlMBg2S7eWafvgyqGcJen2aZTr_ZM")

dp = Dispatcher()

@dp.message(Command("hello"))
async def cmd_start(message: types.Message) -> None:
    await message.answer(f"hi {hbold(message.from_user.full_name)}")

@dp.message(Command("time"))
async def data(message: types.Message):
    await message.answer(f"Теперішній час: {message.date}")

@dp.message()
async def data(message: types.Message):
    await message.answer("Я не розумію вас. Доступні команди: /hello, /time")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())