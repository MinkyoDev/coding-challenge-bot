import discord
import logging

from utils.message_auto_delete import send_message_auto_delete

from . import setting_embeds
from .detail_buttons import DetailButton


class SettingButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
 
    @discord.ui.button(label='등록', style=discord.ButtonStyle.primary, row=1)
    async def registration(self, interaction: discord.Interaction, button: discord.ui.Button):
        logging.info(f"Register button pressed by: {interaction.user} (ID: {interaction.user.id})")

        await setting_embeds.embed_emty_user(interaction)

    @discord.ui.button(label='설정', style=discord.ButtonStyle.secondary, row=2)
    async def settings(self, interaction: discord.Interaction, button: discord.ui.Button):
        logging.info(f"Register button pressed by: {interaction.user} (ID: {interaction.user.id})")

        content = "User Settings"
        await send_message_auto_delete(interaction, content=content, view=DetailButton())