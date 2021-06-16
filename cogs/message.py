#This is a feature file
import discord
from discord.ext import commands
class message(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def ping(self,ctx):
        await ctx.send("pong")
def setup(client):
    client.add_cog(message(client))
