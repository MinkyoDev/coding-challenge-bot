import discord
from discord.ext import commands

from utils.const import REGISTRATION_CHANNEL_ID

from utils.clean_channel import clean_all
from .user_buttons import UserButton


async def registration_channel(bot: commands.Bot):
    channel = bot.get_channel(REGISTRATION_CHANNEL_ID)
    if channel:
        await clean_all(channel)

        content = "여기에 일반 메시지를 입력하세요."
        embed = discord.Embed(title=":hand_splayed: 안녕하세요!", color=0xFF9900)
        
        await channel.send(content=content, embed=embed, view=UserButton())