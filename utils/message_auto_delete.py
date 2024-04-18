import discord
from discord.utils import MISSING

import asyncio
from typing import Sequence
import utils.const as const

async def send_message_auto_delete(
        interaction: discord.Interaction, 
        content: str = MISSING,
        embed: discord.Embed = MISSING,
        embeds: Sequence[discord.Embed] = MISSING, 
        view: discord.ui.View = MISSING, 
        holding_time: int = const.MAINTIME,
        ephemeral: bool = True
        ):
    await interaction.response.defer()

    message = await interaction.followup.send(content=content, embed=embed, embeds=embeds, view=view, wait=True, ephemeral=ephemeral)
    
    await asyncio.sleep(holding_time)

    try:
        await message.delete()
    except discord.NotFound:
        pass
