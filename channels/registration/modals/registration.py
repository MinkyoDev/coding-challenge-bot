import discord
import asyncio

from db import models
from db.db_connection import get_db
from channels.registration.user_crud import create_user


class Registration(discord.ui.Modal, title='등록하기'):
    def __init__(self):
        super().__init__()

        self.add_item(discord.ui.TextInput(
            label='Github username',
            style=discord.TextStyle.short,
            placeholder='Github username을 입력해주세요',
        ))
        self.add_item(discord.ui.TextInput(
            label='Repository name',
            style=discord.TextStyle.short,
            placeholder='Repository 이름을 입력해주세요',
        ))
        
    async def embed_registration(self, user: models.User):
        embed = discord.Embed(title="등록 완료!", 
                            description=f"{user.global_name} 님이 성공적으로 추가되었습니다.",
                            color=discord.Color.blue())
        embed.set_thumbnail(url=f"https://avatars.githubusercontent.com/{user.git_username}")
        embed.add_field(name="Github username", value=user.git_username, inline=False)
        embed.add_field(name="Repository name", value=user.repository_name, inline=False)
        return embed
 
    async def on_submit(self, interaction: discord.Interaction):
        user = create_user(db_session=get_db(), 
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
 
 