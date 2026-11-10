import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
from aiohttp import web

# .env faylidagi o'zgaruvchilarni yuklash
load_dotenv()

# Bot tokenini olish
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()

dp = Dispatcher()

# /start buyrug'i uchun handler
@dp.message(CommandStart())
async def handle_start(message: Message):
    if message.from_user and message.from_user.username:
        user_display = f"@{message.from_user.username}"
    else:
        user_display = "hurmatli mijoz"

    await message.answer(f"Assalomu alaykum, {user_display}!")

# Render uchun HTTP web server (Health check va doimiy tirik turish uchun)
async def handle_ping(request):
    return web.Response(text="Bot muvaffaqiyatli ishlab turibdi!", content_type="text/plain; charset=utf-8")

async def start_web_server():
    app = web.Application()
    app.router.add_get('/', handle_ping)
    app.router.add_get('/health', handle_ping)

    port = int(os.environ.get("PORT", 8080))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    logging.info(f"Web server {port}-portda tinglashni boshladi.")

async def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    logging.info("Dastur ishga tushmoqda...")

    # 1. Render talab qiladigan web serverni fonda ishga tushiramiz
    await start_web_server()

    # 2. Telegram botni ishga tushirish
    if BOT_TOKEN:
        bot = Bot(token=BOT_TOKEN)
        logging.info("Telegram Bot polling rejimida ishga tushdi...")
        await dp.start_polling(bot)
    else:
        logging.error("DIQQAT: BOT_TOKEN muhit o'zgaruvchisi topilmadi! Iltimos, Render'da BOT_TOKEN ni kiriting.")
        # Web server ishlab turishi uchun cheksiz kutish
        while True:
            await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
