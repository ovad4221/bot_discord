import discord
from discord.ext import commands
import time
from requests import get
import datetime
import asyncio

TOKEN = "ODM3MzYxNzAzNjUyOTUwMDU4.YIrb2w.lUBFf41MluUhL9fxqjepIW6JCpw"


def wait_and_send(seconds, minutes, hours):
    time.sleep(int(seconds) + 60 * int(minutes) + 3600 * int(hours))
    return True


class CommandTime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='set_timer')
    async def timer(self, ctx, hours, minutes, seconds):
        ctx.send("Таймер поставлен")
        if wait_and_send(seconds, minutes, hours):
            await ctx.send("Время Х наступило!!!")


bot = commands.Bot(command_prefix='!#')
bot.add_cog(CommandTime(bot))
bot.run(TOKEN)
