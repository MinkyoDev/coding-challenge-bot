import discord
import utils.const as const
import logging

from utils.clean_channel import clean_all
from channels.registration.modals import registration, modification, deactivate

from db.db_connection import get_db
from channels.registration.user_crud import get_user
from channels.registration.user_embed import embed_emty_user, embed_already_registered, embed_already_deactivated, embed_cannot_edit_while_deactivated

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s     %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class UserButton(discord.ui.View):
    def __init__(self):
        super().__init__()
 
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


async def registration_channel(bot):
    channel = bot.get_channel(const.REGISTRATION_CHANNEL_ID)
    
    if channel:
        await clean_all(channel)
        
        embed = discord.Embed(title=":hand_splayed: 안녕하세요!", color=0xFF9900)
        
        # await channel.send(embed=embed, view=UserButton())
        await channel.send(content="여기에 일반 메시지를 입력하세요.", embed=embed, view=UserButton())