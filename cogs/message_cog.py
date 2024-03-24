from discord.ext import commands
import asyncio

from utils.download_images import download_image
from utils.embeds import EmbedCreator
import const


class MessageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.SAVE_PATH = 'downloaded_images'
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        if message.channel.id in const.CHANNEL_LIST:
            print(message)
            print(message.author.global_name)

            print(f'메시지 받음: {message.content} (채널: {message.channel}, 사용자: {message.author})')

            # Say hello
            if "안녕" in message.content:
                embed = await EmbedCreator.embed_hello(message)
                await message.channel.send(embed=embed)
            
            # Image download
            if message.attachments:
                file_path = await download_image(message)
                if file_path:
                    await message.channel.send("이미지 저장 완료")
                    
            # Create embed
            if message.content == "임베드":
                await EmbedCreator.embed_test(message)
            
            # Delete message
            if "싫어" in message.content:
                await message.delete()
                await message.channel.send(f"{message.author.mention} 님이 비속어를 사용하였습니다.")
                
            # Clean channel
            if message.content.startswith("!청소 "):
                purge_number = message.content.replace("!청소 ", "")
                check_purge_number = purge_number.isdigit()
                
                if check_purge_number == True:
                    await message.channel.purge(limit=int(purge_number) + 1)
                    msg = await message.channel.send(f"**{purge_number}개**의 메시지를 삭제했습니다.")
                    await asyncio.sleep(5)
                    await msg.delete()

                else:
                    await message.channel.send("올바른 값을 입력해주세요.")