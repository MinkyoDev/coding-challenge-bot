import discord

async def clean(message, num: int):
    if num < 1:
        await message.send("삭제할 메시지 수는 최소 1개 이상이어야 합니다.", delete_after=10)
        return

    deleted = await message.channel.purge(limit=num + 1)

    msg = await message.send(f"**{len(deleted)-1}개**의 메시지를 삭제했습니다.", delete_after=5)
    
async def clean_all(channel: discord.channel.TextChannel, message=False):
    count = 0
    async for _ in channel.history(limit=None):
        count += 1
        
    deleted = await channel.purge(limit=count + 1)

    if message:
        msg = await channel.send(f"**{len(deleted)-1}개**의 메시지를 삭제했습니다.", delete_after=5)