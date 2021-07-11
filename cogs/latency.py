import discord as discord
from discord.ext import commands

class Latency(commands.Cog):
    """Latency commands"""
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def latency(self,ctx):
        """Returns latency"""
        await ctx.send(f'The latency is {round(self.client.latency *1000)} ms')

def setup(client):
    client.add_cog(Latency(client))
