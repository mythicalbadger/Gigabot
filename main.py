import discord
import os
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
from pathlib import Path

intents = discord.Intents.default()
intents.members = True
intents.reactions = True
intents.message_content = True
# Initialize a new client (i.e. our bot)
bot = commands.Bot(command_prefix="$", intents=intents)

# Load the environment variables
load_dotenv(find_dotenv())

# These load and unload functions may or may not do something but cogs are working so yay
@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")

@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f"cogs.{extension}")

@bot.event
async def on_ready():
    # Once the bot is ready, load all the cogs from the cogs folder
    print("We have logged in as %s" % (bot.user))
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # Each cog is imported like {foldername}.{filename (without extension)}
            await bot.load_extension(f"cogs.{filename[:-3]}")

# Run our Discord bot
bot.run(os.getenv("DISCORD_TOKEN"))
