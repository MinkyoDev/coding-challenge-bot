from discord.ext import commands, tasks
from utils.const import REMIND_CHANNEL_ID, CHECK_IN_TIMES, CHECK_OUT_TIMES


class MyCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.check_in_alarm.start()
        self.check_out_alarm.start()

    @tasks.loop(time=CHECK_IN_TIMES)
    async def check_in_alarm(self):
        channel = self.bot.get_channel(REMIND_CHANNEL_ID)
        await channel.send(f"checkin")
        
    @tasks.loop(time=CHECK_OUT_TIMES)
    async def check_out_alarm(self):
        channel = self.bot.get_channel(REMIND_CHANNEL_ID)
        await channel.send(f"checkout")

    @check_in_alarm.before_loop
    async def before_check_in_alarm(self):
        await self.bot.wait_until_ready()

    @check_out_alarm.before_loop
    async def before_my_task(self):
        await self.bot.wait_until_ready()

    @check_in_alarm.error
    async def check_in_alarm_error(self, error):
        channel = self.bot.get_channel(REMIND_CHANNEL_ID)
        await channel.send(f"An error occurred in my_task: {error}")

    @check_out_alarm.error
    async def my_task_error(self, error):
        channel = self.bot.get_channel(REMIND_CHANNEL_ID)
        await channel.send(f"An error occurred in my_task: {error}")


async def setup(bot: commands.Bot):
    await bot.add_cog(MyCog(bot))