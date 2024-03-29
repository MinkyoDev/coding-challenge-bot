import discord

from db.db_connection import get_db
from channels.registration.user_crud import deactivate_user
from channels.registration.user_embed import embed_deactivate_complite, embed_incorrect_keyword


class Deactivate(discord.ui.Modal, title='비활성화하기'):
    def __init__(self):
        super().__init__()
        self.add_item(discord.ui.TextInput(
            label='비활성화를 원하신다면 아래에 "비활성화"라고 입력해 주세요.',
            style=discord.TextStyle.short,
            placeholder="비활성화"
        ))
    
    async def on_submit(self, interaction: discord.Interaction):
        if self.children[0].value =="비활성화":
            user = deactivate_user(db_session=get_db(), 
                            user_id=interaction.user.id,
                            )
            await embed_deactivate_complite(interaction, user)
        else:
            await embed_incorrect_keyword(interaction)
            
