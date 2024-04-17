from discord.ext import commands, tasks
from utils.const import REMIND_TIME, REMIND_CHANNEL_ID


class MyCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.my_task.start()

    # @tasks.loop(seconds=60)
    # async def my_task(self):
    #     channel = self.bot.get_channel(1230084679260966983)
    #     await channel.send("This message is sent every minute!")
        
    @tasks.loop(time=REMIND_TIME)
    async def my_task(self):
        channel = self.bot.get_channel(REMIND_CHANNEL_ID)
        await channel.send(f"This message is sent every {REMIND_TIME}")

    @my_task.before_loop
    async def before_my_task(self):
        print('waiting...')
        await self.bot.wait_until_ready()

    @my_task.error
    async def my_task_error(self, error):
        channel = self.bot.get_channel(REMIND_CHANNEL_ID)
        await channel.send(f"An error occurred in my_task: {error}")

async def setup(bot: commands.Bot):
    await bot.add_cog(MyCog(bot))