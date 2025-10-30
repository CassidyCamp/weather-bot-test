import time
import requests
from config import TOKEN, WEATHER_API_KEY

# ======= Telegram API========
TG_BO_BASE_URL = f'https://api.telegram.org/bot{TOKEN}'
WEATHER_URL = 'http://api.weatherapi.com/v1/current.json'
GETME_URL = f"{TG_BO_BASE_URL}/getMe"
SENDMASSAGE_URL = f"{TG_BO_BASE_URL}/sendMessage"
GETUPDATES_URL = f"{TG_BO_BASE_URL}/getUpdates"


def get_updates() -> list:
    return requests.get(GETUPDATES_URL).json()


def get_last_update() -> list:
    return requests.get(GETUPDATES_URL).json()['result'][-1]


def last_chat_id(last_user: dict) -> str:
    return last_user['message']['chat']['id']


def last_first_name(last_user: dict) -> str:
    return last_user['message']['from']['first_name']


def send_massage(id: str, text: str) -> None:
    requests.get(SENDMASSAGE_URL, params={"chat_id": id, "text":text})


def last_text(last_user: str) -> None:
    return last_user['message']['text']

def get_weather(city: str) -> float:
    res = requests.get(WEATHER_URL, params={'key':f"{WEATHER_API_KEY}", 'q':city}).json()

    loc = res['location']['name']
    temp = res['current']['temp_c']
    cond = res['current']['condition']['text']
    
    return [loc, temp, cond]

def translate_condition(condition: str) -> str:
    condition = condition.lower()
    
    translations = {
        "sunny": "Quyoshli",
        "clear": "Tiniq, musaffo",
        "partly cloudy": "Qisman bulutli",
        "cloudy": "Bulutli",
        "overcast": "Qorong‘i, quyosh ko‘rinmaydi",
        "rain": "Yomg‘ir",
        "light rain": "Yengil yomg‘ir",
        "heavy rain": "Kuchli yomg‘ir",
        "drizzle": "Mayda yomg‘ir",
        "snow": "Qor",
        "light snow": "Yengil qor",
        "heavy snow": "Qalin qor",
        "thunderstorm": "Momaqaldiroq",
        "fog": "Tuman",
        "mist": "Yengil tuman",
        "windy": "Shamolli",
        "freezing rain": "Muzlab tushgan yomg‘ir",
    }
    
    for eng, uz in translations.items():
        if eng in condition:
            return uz
        
    return condition.capitalize()

translate_condition(get_weather('samarkand')[2])


last_update_id = 0

while True:
    update = get_last_update()
    new_update_id = update['update_id']
    
    
    if not new_update_id:
        continue
        time.sleep(2)
    
    text = last_text(update)
    
    if last_update_id != new_update_id:    
        if text == "/start":
            send_massage(last_chat_id(get_last_update()),f"Salom {last_first_name(get_last_update())}!\n👋 Meni Ob-havo botimga xush kelibsiz!\n🌤️ Qaysi shahar ob-havosini bilmoqchisiz?")
        else:
            try:
                weather_info = get_weather(text)
                translate_cond = translate_condition(weather_info[-1])
                
                send_massage(last_chat_id(get_last_update()), f"Hozirgi kunda {weather_info[0]}da ob-havo harorati {weather_info[1]}C, {translate_cond}")
            except:
                send_massage(last_chat_id(get_last_update()), "Uzr, ob-havo ma'lumotini topa olmadim.")
    
    last_update_id = new_update_id
    time.sleep(0.5)
    