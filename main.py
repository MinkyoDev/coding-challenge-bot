import discord
from discord.ext import commands
from pathlib import Path
import os, dotenv

from channels.registration.user_channel import registration_channel
from utils.logger_config import setup_logger

env_path = Path('.') / '.env'
if env_path.exists():
    dotenv.load_dotenv(dotenv_path=env_path)

BOT_TOKEN = os.getenv("BOT_TOKEN")

setup_logger()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await registration_channel(bot)

    print(f'{bot.user}가 준비되었습니다!')

bot.run(BOT_TOKEN)