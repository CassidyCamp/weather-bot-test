## 🌦️ Telegram Ob-havo Bot

Bu loyiha — foydalanuvchi yozgan shahar nomiga qarab **hozirgi ob-havo ma’lumotini** (`WeatherAPI`) orqali olib, **Telegram**da yuboradigan oddiy bot dasturidir.

---

### 📋 Tarkib

* `main.py` — asosiy bot kodi
* `config.py` — maxfiy ma’lumotlar (tokenlar) saqlanadigan fayl

---

### ⚙️ Talablar

Quyidagi kutubxonalar o‘rnatilgan bo‘lishi kerak:

```bash
pip install requests
```

---

### 🔑 `config.py` fayli

`config.py` fayl ichida quyidagilar bo‘lishi kerak:

```python
TOKEN = "SIZNING_TELEGRAM_BOT_TOKENINGIZ"
WEATHER_API_KEY = "SIZNING_WEATHERAPI_KEYINGIZ"
```

* **TOKEN** — [@BotFather](https://t.me/BotFather) dan olingan Telegram bot token.
* **WEATHER_API_KEY** — [https://www.weatherapi.com/](https://www.weatherapi.com/) saytida ro‘yxatdan o‘tib olinadigan API kalit.

---

### 🚀 Ishga tushirish

1. `config.py` faylni to‘ldiring.
2. Keyin terminalda quyidagilarni yozing:

```bash
python main.py
```

3. Telegram’da botni toping va **/start** deb yozing.

---

### 💬 Foydalanish

Botga **shahar nomini** yozing — masalan:

```
Toshkent
```

Bot javob qaytaradi:

```
Hozirgi kunda Toshkentda ob-havo harorati 17°C, Qisman bulutli
```

---

### 🌍 Tarjima funksiyasi

`translate_condition()` funksiyasi ob-havo holatini ingliz tilidan o‘zbek tiliga tarjima qiladi, masalan:

| Inglizcha    | O‘zbekcha    |
| ------------ | ------------ |
| Sunny        | Quyoshli     |
| Cloudy       | Bulutli      |
| Rain         | Yomg‘ir      |
| Snow         | Qor          |
| Fog          | Tuman        |
| Thunderstorm | Momaqaldiroq |

---

### 🧠 Bot ishlash mantig‘i

1. Bot `getUpdates` orqali foydalanuvchi xabarini oladi.
2. Xabar yangi bo‘lsa (`update_id` yangilangan bo‘lsa):

   * Agar `/start` — salomlashuv xabari yuboriladi.
   * Aks holda — foydalanuvchi yozgan shahar nomi bo‘yicha ob-havo ma’lumoti olinadi.
3. Natija foydalanuvchiga yuboriladi.
4. Bot har 0.5 soniyada yangi xabarni tekshiradi.

---

### ⚠️ Xatoliklar bo‘lsa

Agar bot “Uzr, ob-havo ma’lumotini topa olmadim” deb yozsa:

* Shahar nomi xato yozilgan bo‘lishi mumkin.
* `WEATHER_API_KEY` noto‘g‘ri yoki muddati o‘tgan bo‘lishi mumkin.
* Internet aloqasi mavjudligini tekshiring.

---

### 📸 Namunaviy ishlash

```
👤 Siz: Samarkand  
🤖 Bot: Hozirgi kunda Samarkandda ob-havo harorati 19°C, Quyoshli
```

---

### 🧾 Muallif

* 👨‍💻 **Daler**
* 💡 Maqsad: Oddiy ob-havo tekshiruvchi Telegram bot yaratish

