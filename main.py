import discord
import os
from main.config import prefix, token, status
from discord.ext import commands
from main.ascii import text

bot = commands.Bot(command_prefix = prefix)
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    try:
      bot.load_extension(f"cogs.{filename[:-3]}")
      print(f"Loaded Cog: {filename}")
    except Exception as e:
      print(e)

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
  print(random.choice(text))