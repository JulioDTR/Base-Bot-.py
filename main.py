import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re

bot = commands.Bot(command_prefix='!', description="Description")

@bot.command()
async def commande(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem Ipsum asdasd", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Serveur crée le", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Fondateur du serveur", value=f"{ctx.guild.owner}")
    embed.add_field(name="Région du serveur", value=f"{ctx.guild.region}")
    embed.add_field(name="ID du serveur", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="image")
