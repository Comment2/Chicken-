import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot connecté en tant que {bot.user}")

@bot.command()
async def bonjour(ctx):
    await ctx.send("👋 Salut ! Je suis ton bot Discord.")

bot.run("7308647148:AAFPmURPxR4RbVBWvYZMd_3D_zxV4_ncZJc")
