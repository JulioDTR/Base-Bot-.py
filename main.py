import discord 
from discord.ext import commands

bot = commands.Bot(command_prefix='!', description="Description")
bot = commands.Bot(help_command=None) # supprime la commande de base help

bot.run('token')
