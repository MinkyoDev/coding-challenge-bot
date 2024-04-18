from discord.ext import commands

from utils.const import CHALLENGE_CHANNEL_ID
from channels.setting.setting_buttons import SettingButton

from utils.clean_channel import clean_all


async def setting_channel(bot: commands.Bot):
    channel = bot.get_channel(CHALLENGE_CHANNEL_ID)
    if channel:
        await clean_all(channel)

        content = """
## Setting
        """
        
        await channel.send(content=content, view=SettingButton(), silent=True)