import discord
from discord.utils import MISSING

import asyncio
from typing import Union, List
import utils.const as const

async def send_message_auto_delete(interaction: discord.Interaction, embeds: Union[discord.Embed, List[discord.Embed]], view: discord.ui.View=MISSING, ephemeral: bool=True):
    await interaction.response.defer()

    if not isinstance(embeds, list):
        embeds = [embeds]

    message = await interaction.followup.send(embeds=embeds, view=view, wait=True, ephemeral=ephemeral)
    
    await asyncio.sleep(const.MAINTIME)

    try:
        await message.delete()
    except discord.NotFound:
        pass
