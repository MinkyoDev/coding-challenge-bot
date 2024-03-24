import discord

class EmbedCreator:
    def __init__(self):
        pass
    
    async def embed_hello(message):
        embed = discord.Embed(title=":hand_splayed: 안녕하세요!", color=0xFF9900)
        return embed
        
    async def embed_test(message):
        embed = discord.Embed(title=message.author.global_name, description="설명 1", color=0x3498DB)

        embed.set_author(name="MinkyoDev", url="https://github.com/MinkyoDev", icon_url="https://avatars.githubusercontent.com/MinkyoDev")
        embed.set_thumbnail(url="https://avatars.githubusercontent.com/MinkyoDev")
        embed.set_image(url="https://avatars.githubusercontent.com/MinkyoDev")

        embed.add_field(name="필드 1", value="내용 1", inline=True)
        embed.add_field(name="필드 2", value="내용 2", inline=True)

        embed.set_footer(text="푸터 내용", icon_url="https://avatars.githubusercontent.com/MinkyoDev")

        await message.channel.send(embed=embed)
    
    async def registration_embed(message):
        
        embed = discord.Embed(title=":hand_splayed: 안녕하세요!", color=0xFF9900)
        await message.channel.send(embed=embed)