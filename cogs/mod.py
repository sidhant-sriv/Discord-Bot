import discord
from discord.ext import commands


class Mod(commands.Cog):
    """Moderation commands"""
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=10):
        """Delete stuff"""
        await ctx.channel.purge(limit=amount+1)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx,member: discord.Member,*,reason="lol bye"):
        """Kick people"""
        await member.kick(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx,member: discord.Member,*,reason="lol bye"):
        """Ban people"""
        await member.ban(reason=reason)
def setup(client):
    client.add_cog(Mod(client))
