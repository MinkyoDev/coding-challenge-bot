import discord
from discord.ext import commands

from utils.const import CHALLENGE_CHANNEL_ID

from utils.clean_channel import clean_all
from .buttons.challenge_button import ChallengeButton


async def challenge_channel(bot: commands.Bot):
    channel = bot.get_channel(CHALLENGE_CHANNEL_ID)
    if channel:
        await clean_all(channel)

        content = """
## 챌린지 인증

이 채널에는 여러분이 푼 문제들이 올라오게 됩니다.
        """
        
        await channel.send(content=content, view=ChallengeButton(), silent=True)