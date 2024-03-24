import discord
from discord.ext import commands

from utils.button import ButtonFunction
from utils.modal import ModalButton

class CommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='print_message')
    async def print_info(self, message):
        print("Context 객체의 정보:")
        print(f"채널: {message.channel}")
        print(f"채널: {message.channel.id}")
        print(f"길드(서버): {message.guild}")
        print(f"메시지: {message.message}")
        print(f"메시지 내용: {message.message.content}")
        print(f"사용자: {message.author}")
        print(f"명령어: {message.command}")
        print(f"명령어 이름: {message.command.name}")
        
    @commands.command(name='count_messages')
    async def count_messages(self, message):
        channel = self.bot.get_channel(message.channel.id)
        if channel is None:
            await message.send("채널을 찾을 수 없습니다.")
            return

        count = 0
        async for _ in channel.history(limit=None):
            count += 1

        await message.send(f"{channel.name} 채널의 메시지 개수: {count}")
        
    @commands.command(name='clean')
    async def clean(self, message, num: int):
        if num < 1:
            await message.send("삭제할 메시지 수는 최소 1개 이상이어야 합니다.", delete_after=10)
            return

        deleted = await message.channel.purge(limit=num + 1)

        # 삭제 완료 메시지 보내기 (5초 후 자동 삭제)
        msg = await message.send(f"**{len(deleted)-1}개**의 메시지를 삭제했습니다.", delete_after=5)
        
    @commands.command(name='clean_all')
    async def clean_all(self, message):
        channel = self.bot.get_channel(message.channel.id)
        if channel is None:
            await message.send("채널을 찾을 수 없습니다.")
            return
        
        count = 0
        async for _ in channel.history(limit=None):
            count += 1
            
        deleted = await message.channel.purge(limit=count + 1)

        # 삭제 완료 메시지 보내기 (5초 후 자동 삭제)
        msg = await message.send(f"**{len(deleted)-1}개**의 메시지를 삭제했습니다.", delete_after=5)
        
    @commands.command(name='cal')
    async def calculate(self, message):
        # names = message.split("!cal ",1)[1]
        # data = names.split("*")
        a = 3
        b = 4
        c=int(a)*int(b)
        r=str(c)
        em=discord.Embed(title=f"Calculator",description=f"Input\n```{a}*{b}```\n\nOutput\n```{r}```")
        await message.channel.send(embed=em)
        
    @commands.command(name='button')
    async def button(self, message):
        await message.send("버튼 명령어", view=ButtonFunction())
        
    @commands.command(name='modal')
    async def modal(self, message):
        await message.send(view=ModalButton())