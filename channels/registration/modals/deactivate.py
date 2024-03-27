import discord
import asyncio

from db import models
from db.db_connection import get_db
from channels.registration.user_crud import deactivate_user


class Deactivate(discord.ui.Modal, title='비활성화하기'):
    
    def __init__(self):
        super().__init__()
        self.add_item(discord.ui.TextInput(
            label='비활성화를 원하신다면 아래에 "비활성화"라고 입력해 주세요.',
            style=discord.TextStyle.short,
            placeholder="비활성화"
        ))

    async def embed_registration(self, user: models.User):
        embed = discord.Embed(title="비활성화 완료!", 
                            description=f"{user.global_name} 님이 성공적으로 비활성화되었습니다.",
                            color=discord.Color.red())
        return embed
    
    async def on_submit(self, interaction: discord.Interaction):
        if self.children[0].value =="비활성화":
            user = deactivate_user(db_session=get_db(), 
                            user_id=interaction.user.id,
                            )
        
        await interaction.response.defer()
        embed = await self.embed_registration(user)
        message = await interaction.followup.send(embed=embed, wait=True)
    
        await asyncio.sleep(5)

        await message.delete()