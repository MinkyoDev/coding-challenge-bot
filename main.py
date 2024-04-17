import discord
from discord.ext import commands, tasks
import os
from utils.const import BOT_TOKEN, ADMIN_CHANNEL_ID
from utils.logger_config import setup_logger

# from channels.user.user_channel import registration_channel
# from channels.challenge.challenge_channel import challenge_channel

setup_logger()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

async def load_extensions():
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


@bot.event
async def on_ready():
    # await registration_channel(bot)
    # await challenge_channel(bot)

    await load_extensions()

    channel = bot.get_channel(ADMIN_CHANNEL_ID)
    if channel:
        await channel.send(f'{bot.user}가 준비되었습니다!', silent=True)
        
    print(f'{bot.user}가 준비되었습니다!')

bot.run(BOT_TOKEN)