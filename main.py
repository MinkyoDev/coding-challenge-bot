import discord
from discord.ext import commands

from utils.const import BOT_TOKEN, ADMIN_CHANNEL_ID
from utils.logger_config import setup_logger

from channels.user.user_channel import registration_channel
from channels.challenge.challenge_channel import challenge_channel

from cogs.message import MessageCog


setup_logger()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await registration_channel(bot)
    await challenge_channel(bot)
    await bot.add_cog(MessageCog(bot))

    channel = bot.get_channel(ADMIN_CHANNEL_ID)
    if channel:
        await channel.send(f'{bot.user}가 준비되었습니다!', silent=True)
        
    print(f'{bot.user}가 준비되었습니다!')

@bot.event
async def on_resumed():
    print("세션이 성공적으로 재개되었습니다.")
    
bot.run(BOT_TOKEN)