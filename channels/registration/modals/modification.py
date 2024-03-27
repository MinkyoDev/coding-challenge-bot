import discord
import asyncio

from db import models
from db.db_connection import get_db
from channels.registration.user_crud import update_user, get_user

        
class Modification(discord.ui.Modal, title='수정하기'):
    
    def __init__(self, interaction: discord.Interaction):
        super().__init__()
        user = get_user(db_session=get_db(), user_id=interaction.user.id)

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
    
    async def embed_registration(self, user: models.User):
        embed = discord.Embed(title="수정 완료!", 
                            description=f"{user.global_name} 님의 정보가 성공적으로 수정되었습니다.",
                            color=discord.Color.green())
        embed.set_thumbnail(url=f"https://avatars.githubusercontent.com/{user.git_username}")
        embed.add_field(name="Github username", value=user.git_username, inline=False)
        embed.add_field(name="Repository name", value=user.repository_name, inline=False)
        return embed
    
    async def on_submit(self, interaction: discord.Interaction):
        pass
        user = update_user(db_session=get_db(), 
                          user_id=interaction.user.id,
                          name=interaction.user.name,
                          global_name=interaction.user.global_name,
                          git_username= self.children[0].value,
                          repository_name=self.children[1].value,
                          )
        
        await interaction.response.defer()
        embed = await self.embed_registration(user)
        message = await interaction.followup.send(embed=embed, wait=True)
    
        await asyncio.sleep(5)

        await message.delete()