import discord
import const

from utils.clean_channel import clean_all
from db.database_connection import get_db
from db.user_crud import create_user


class Introduce(discord.ui.Modal, title='등록하기'):
    username = discord.ui.TextInput(
        label='Github username',
        style=discord.TextStyle.short,
        placeholder='Github username을 입력해주세요',
    )
    
    repo_name = discord.ui.TextInput(
        label='Repository name',
        style=discord.TextStyle.short,
        placeholder='Repository 이름을 입력해주세요',
    )
 
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'{interaction.user.global_name} 님이 추가되었습니다! \nGithub username : {self.username.value}\nRepository name : {self.repo_name.value}')
        db = get_db()
        user = create_user(db, "new_user", "new_user@example.com")
        print(user.id, user.username, user.email)
        print(interaction.user.id)
        print(interaction.user.name)
        print(interaction.user.global_name)


class ModalButton(discord.ui.View):
    def __init__(self):
        super().__init__()
 
    @discord.ui.button(label='등록하기', style=discord.ButtonStyle.primary)
    async def button1(self, interaction: discord.Interaction, button: discord.ui.Button):
        print(dir(interaction))
        print(dir(interaction.user))
        print(interaction.user)
        print(interaction.user.id)
        print(interaction.user.name)
        print(interaction.user.global_name)
        print(interaction.user.discriminator)
        await interaction.response.send_modal(Introduce())


async def registration(bot):
    channel = bot.get_channel(const.REGISTRATION_CHANNEL_ID)
    
    if channel:
        await clean_all(channel)
        
        embed = discord.Embed(title=":hand_splayed: 안녕하세요!", color=0xFF9900)
        await channel.send(embed=embed, view=ModalButton())
        
        # await channel.send(view=ModalButton())