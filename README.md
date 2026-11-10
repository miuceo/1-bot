# 1-bot

Telegram bot (Aiogram 3.x asosida).

## Server yoki kompyuterda o'rnatish va ishga tushirish

### 1. Repozitoriyani klonlash
```bash
git clone https://github.com/miuceo/1-bot.git
cd 1-bot
```

### 2. Virtual muhit (venv) yaratish va faollashtirish
**Linux (Ubuntu/Debian server):**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Kerakli paketlarni o'rnatish
```bash
pip install -r requirements.txt
```

### 4. Konfiguratsiya (.env)
`.env.example` dan nusxa olib `.env` faylini yarating:
```bash
cp .env.example .env
```
`.env` faylini ochib, `@BotFather` bergan tokenni yozing:
```env
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrSTUvwxYZ
```

### 5. Botni ishga tushirish
```bash
python bot.py
```

### Serverda doimiy (background / systemd) ishlatish (Linux)
Server o'chib-yonmaguncha yoki doim fonda ishlashi uchun `systemd` servisi orqali ishlatish tavsiya etiladi:
```ini
[Unit]
Description=Telegram 1-bot
After=network.target

[Service]
User=root
WorkingDirectory=/path/to/1-bot
ExecStart=/path/to/1-bot/venv/bin/python bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```
