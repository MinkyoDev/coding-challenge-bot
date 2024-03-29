import discord
import logging

from db.db_connection import get_db

from .modals import registration, modification, deactivate
from .user_crud import get_user
from .user_embed import embed_emty_user, embed_already_registered, embed_already_deactivated, embed_cannot_edit_while_deactivated

class UserButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
 
    @discord.ui.button(label='등록', style=discord.ButtonStyle.primary, row=1)
    async def registration(self, interaction: discord.Interaction, button: discord.ui.Button):
        logging.info(f"Register button pressed by: {interaction.user} (ID: {interaction.user.id})")

        user = get_user(db_session=get_db(), user_id=interaction.user.id)
        if not (user is None or not user.use):
            await embed_already_registered(interaction)
            return
            
        await interaction.response.send_modal(registration.Registration())
        
    @discord.ui.button(label='수정', style=discord.ButtonStyle.success, row=1)
    async def modification(self, interaction: discord.Interaction, button: discord.ui.Button):
        logging.info(f"Modify button pressed by: {interaction.user} (ID: {interaction.user.id})")

        user = get_user(db_session=get_db(), user_id=interaction.user.id)
        if user is None:
            await embed_emty_user(interaction)
            return
        if user.use is False:
            await embed_cannot_edit_while_deactivated(interaction)
            return

        await interaction.response.send_modal(modification.Modification(user))
        
    @discord.ui.button(label='비활성화', style=discord.ButtonStyle.danger, row=1)
    async def deactivate(self, interaction: discord.Interaction, button: discord.ui.Button):
        logging.info(f"Deactivate button pressed by: {interaction.user} (ID: {interaction.user.id})")

        user = get_user(db_session=get_db(), user_id=interaction.user.id)
        if user is None:
            await embed_emty_user(interaction)
            return
        if user.use is False:
            await embed_already_deactivated(interaction)
            return
        await interaction.response.send_modal(deactivate.Deactivate())