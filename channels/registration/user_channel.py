import discord
import const

from utils.clean_channel import clean_all
from channels.registration.modals import registration, modification, deactivate


class UserButton(discord.ui.View):
    def __init__(self):
        super().__init__()
 
    @discord.ui.button(label='등록', style=discord.ButtonStyle.primary, row=1)
    async def registration(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(registration.Registration())
        
    @discord.ui.button(label='수정', style=discord.ButtonStyle.success, row=1)
    async def modification(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(modification.Modification(interaction))
        
    @discord.ui.button(label='비활성화', style=discord.ButtonStyle.danger, row=1)
    async def deactivate(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(deactivate.Deactivate())


async def registration_channel(bot):
    channel = bot.get_channel(const.REGISTRATION_CHANNEL_ID)
    
    if channel:
        await clean_all(channel)
        
        embed = discord.Embed(title=":hand_splayed: 안녕하세요!", color=0xFF9900)
        
        # await channel.send(embed=embed, view=UserButton())
        await channel.send(content="여기에 일반 메시지를 입력하세요.", embed=embed, view=UserButton())