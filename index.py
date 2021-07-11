import discord 
import os
from dotenv import load_dotenv, find_dotenv
from pretty_help import PrettyHelp
from discord.ext import commands
client = commands.Bot(command_prefix="!!",help_command=PrettyHelp(no_category="none",sort_commands=True,show_index=True))
load_dotenv(find_dotenv())

TOKEN = os.environ['TOKEN']
COLOR = 0xB0B0BF

@client.command()
async def load(ctx,extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx,extension):
    client.unload_extension(f"cogs.{extension}")

for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        

@client.event
async def on_ready():
    print("Bot is ready")
client.run(TOKEN)
