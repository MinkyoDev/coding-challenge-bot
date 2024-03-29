import discord
import asyncio
import utils.const as const

async def send_message_auto_delete(interaction: discord.Interaction, embed: discord.Embed, ephemeral:bool =True):
    await interaction.response.defer()
    
    message = await interaction.followup.send(embed=embed, wait=True, ephemeral=ephemeral)

    await asyncio.sleep(const.MAINTIME)

    await message.delete()