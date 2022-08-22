import discord
import asyncio
from discord.ext import commands

class Hello(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='hello', help='Says hello')
    async def hello(self, ctx):
        await ctx.send('Hello there!')

async def setup(bot):
    await bot.add_cog(Hello(bot))
