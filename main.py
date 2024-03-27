import discord
from discord.ext import commands
from pathlib import Path
import os, dotenv

from channels.registration.user_channel import registration_channel
from cogs.message_cog import MessageCog

env_path = Path('.') / '.env'
if env_path.exists():
    dotenv.load_dotenv(dotenv_path=env_path)

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def load_extensions():
    # for filename in os.listdir("Cogs"):
    #     if filename.endswith(".py"):
    #         await app.load_extension(f"Cogs.{filename[:-3]}")
    # cog 하나씩 불러오기
    activate_list = ["registration_channel"]
    for name in activate_list:
        await bot.load_extension(f"channels.{name}")


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await registration_channel(bot)
    await bot.add_cog(MessageCog(bot))
    # await load_extensions()
    print(f'{bot.user}가 준비되었습니다!')

    # await bot.add_cog(Registration(bot))

bot.run(BOT_TOKEN)