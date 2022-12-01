import os

class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    PLAYLIST_NAME = os.environ.get("PLAYLIST_NAME")
    GROUP = os.environ.get("GROUP") 
    PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID"))
    BOT_OWNER = os.environ.get("BOT_OWNER")
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
