# 1-bot

Telegram bot (Aiogram 3.x va Render Web Service uchun to'liq moslashtirilgan).

## Render.com da 1 daqiqada ishga tushirish

1. **[render.com](https://render.com)** ga kiring va GitHub orqali kiring.
2. **`+ New`** -> **`Web Service`** ni bosing.
3. **`1-bot`** repozitoriyasini tanlang (`Connect`).
4. Repozitoriyadagi `render.yaml` tufayli barcha sozlamalar (Python, pip install, python bot.py) avtomatik to'ldiriladi!
5. Faqat **`BOT_TOKEN`** maydoniga `@BotFather` bergan tokenni kiriting.
6. **`Deploy Web Service`** ni bosing.

## Bot 24/7 o'chmasdan ishlashi uchun (Bepul)

Render bergan linkni (masalan: `https://telegram-1-bot.onrender.com`) **[uptimerobot.com](https://uptimerobot.com)** ga qo'shing:
- Monitor Type: `HTTP(s)`
- URL: Render havolangiz
- Interval: `10 minutes`
