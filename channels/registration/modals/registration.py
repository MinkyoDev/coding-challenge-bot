import discord

from db.db_connection import get_db
from channels.registration.user_crud import create_user, get_user, delete_user
from channels.registration.user_embed import embed_complite, embed_invalid_info, embed_duplicate_git_username

from utils.git_API import check_repository_exists


class Registration(discord.ui.Modal, title='등록하기'):
    def __init__(self):
        super().__init__()

        self.add_item(discord.ui.TextInput(
            label = 'Github username',
            style = discord.TextStyle.short,
            placeholder = 'Github username을 입력해주세요',
        ))
        self.add_item(discord.ui.TextInput(
            label = 'Repository name',
            style = discord.TextStyle.short,
            placeholder = 'Repository 이름을 입력해주세요',
        ))
        
    async def on_submit(self, interaction: discord.Interaction):
        username = self.children[0].value
        repository = self.children[1].value
        if check_repository_exists(username, repository):
            user = get_user(db_session=get_db(), user_id=interaction.user.id)
            if user:
                delete_user(db_session = get_db(), user_id=user.id)
            user = create_user(db_session = get_db(),
                               user_id = interaction.user.id,
                               name = interaction.user.name,
                               global_name = interaction.user.global_name,
                               git_username = username,
                               repository_name = repository,
                               )
            if user is None:
                await embed_duplicate_git_username(interaction, username)
                return
            
            await embed_complite(interaction, user, self.__class__.__name__)
        else:
            await embed_invalid_info(interaction)
        