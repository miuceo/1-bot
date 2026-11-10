import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

# .env faylidagi o'zgaruvchilarni yuklash
load_dotenv()

# Bot tokenini olish (TOKEN ni .env fayliga yoki quyidagi qatorga yozishingiz mumkin)
BOT_TOKEN = os.getenv("BOT_TOKEN", "BU_YERGA_TOKENINGIZNI_QO'YING")

# Bot va Dispatcher obyektlarini yaratamiz
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# /start buyrug'i uchun handler
@dp.message(CommandStart())
async def handle_start(message: Message):
    # Foydalanuvchining username'i bor-yo'qligini tekshiramiz
    if message.from_user and message.from_user.username:
        user_display = f"@{message.from_user.username}"
    else:
        user_display = "hurmatli mijoz"

    # Foydalanuvchiga javob qaytaramiz
    await message.answer(f"Assalomu alaykum, {user_display}")


async def main():
    # Konsolga ma'lumotlarni chiqarib borish uchun logging
    logging.basicConfig(level=logging.INFO)
    print("Bot ishga tushdi...")
    # Yangi xabarlarni tinglashni boshlaymiz
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
