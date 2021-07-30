import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN") 
GLAV_ADMINS = os.getenv("GLAV_ADMINS")  
IP = os.getenv("ip")
BOT_START_URL='http://t.me/insomnia_zm_bot?start=start'

PG_USER=os.getenv('PG_USER')
PG_PASS=os.getenv('PG_PASS')
host=os.getenv('PG_HOST')
