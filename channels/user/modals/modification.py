import discord

from db.models import User
from db.db_connection import get_db
from utils.git_API import check_repository_exists

from ..user_crud import update_user
from ..user_embed import embed_complite, embed_invalid_info

        
class Modification(discord.ui.Modal, title='수정하기'):
    def __init__(self, user: User):
        super().__init__()
            
        self.add_item(discord.ui.TextInput(
            label='Github username',
            style=discord.TextStyle.short,
            default=user.git_username
        ))
        self.add_item(discord.ui.TextInput(
            label='Repository name',
            style=discord.TextStyle.short,
            default=user.repository_name
        ))

    async def on_submit(self, interaction: discord.Interaction):
        username = self.children[0].value
        repository = self.children[1].value
        if check_repository_exists(username, repository):
            user = update_user(db_session=get_db(), 
                               user_id=interaction.user.id,
                               name=interaction.user.name,
                               global_name=interaction.user.global_name,
                               git_username= self.children[0].value,
                               repository_name=self.children[1].value,
                               )
            await embed_complite(interaction, user, self.__class__.__name__)
        else:
            await embed_invalid_info(interaction)
        