import discord
import const

from utils.clean_channel import clean_all


class Introduce(discord.ui.Modal, title='등록하기'):
    name = discord.ui.TextInput(
        label='닉네임',
        style=discord.TextStyle.short,
        placeholder='닉네임을 입력해주세요',
    )
 
    answer = discord.ui.TextInput(
        label='한줄소개',
        style=discord.TextStyle.long,
        placeholder='아무말이나 입력해주세요',
        required=False,
        max_length=300,
    )
 
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'{self.name.value} 님이 추가되었습니다! \n{self.name.value} : {self.answer.value}')

class ModalButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=1000000)
 
    @discord.ui.button(label='등록하기', style=discord.ButtonStyle.primary)
    async def button1(self, interaction: discord.Interaction, button: discord.ui.Button):
        print(dir(interaction))
        print(interaction.user)
        await interaction.response.send_modal(Introduce())
    
    
async def registration(bot):
    channel = bot.get_channel(const.REGISTRATION_CHANNEL_ID)
    
    if channel:
        await clean_all(channel)
        
        embed = discord.Embed(title=":hand_splayed: 안녕하세요!", color=0xFF9900)
        await channel.send(embed=embed)
        
        await channel.send(view=ModalButton())