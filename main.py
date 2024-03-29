import discord
from discord.ext import commands
from pathlib import Path
import os, dotenv

from utils.logger_config import setup_logger

from channels.user.user_channel import registration_channel
from channels.challenge.challenge_channel import challenge_channel

from cogs.message import MessageCog

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
    await challenge_channel(bot)
    await bot.add_cog(MessageCog(bot))

    print(f'{bot.user}가 준비되었습니다!')

@bot.event
async def on_resumed():
    print("세션이 성공적으로 재개되었습니다.")
    # 필요한 초기화나 상태 복원 로직 추가
    
bot.run(BOT_TOKEN)