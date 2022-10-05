import os, youtube_dl, requests, time
from config import Config
from youtube_search import YoutubeSearch
from pyrogram.handlers import MessageHandler
from pyrogram import Client, filters
import yt_dlp
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message
)


#config#

bot = Client(
    'moonBot',
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)

#musik indirme#

@bot.on_message(filters.command("bul", "indir", "song") & ~filters.edited)
def bul(_, message):
    query = " ".join(message.command[1:])
    m = message.reply("<b>▶️ **şᴀʀᴋɪ ᴀʀᴀɴɪʏᴏʀ** ...</b>")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        m.edit("<b>⛔ **Üzgünüm şarkı bulunamadı.**</b>")
        print(str(e))
        return
    m.edit("<b>▶️ **ɪɴᴅɪʀᴍᴇ ʙᴀşʟᴀᴅɪ...**</b>")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"▶️ **Parça**: [{title[:35]}]({link})\n\n⌚ **Süre**: `{duration}`\n\n•> [𝖬𝗉3 𝖬𝗎𝗓𝗂𝗄 𝖡𝗈𝗍](https://t.me/Mp3MuzikBot) 𝖳𝖺𝗋𝖺𝖿𝗂𝗇𝖽𝖺𝗇 !"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("▶️ **ʏᴜ̈ᴋʟᴇɴɪʏᴏʀ**...")
        message.reply_audio(audio_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, thumb=thumb_name, performer="ᴍᴘ3 ᴍᴜ̈ᴢɪᴋ ʙᴏᴛ")
        m.delete()
        bot.send_audio(chat_id=Config.PLAYLIST_ID, audio=audio_file, caption=rep, performer="ᴍᴘ3 ᴍᴜ̈ᴢɪᴋ ʙᴏᴛ", parse_mode='md', title=title, duration=dur, thumb=thumb_name)
    except Exception as e:
        m.edit("<b>⛔ **Hatanın düzelmesini bekleyin** .</b>")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

bot.run()
