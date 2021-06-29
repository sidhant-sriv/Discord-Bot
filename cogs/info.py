import discord as discord
from discord.ext import commands
from googlesearch import search
import wikipedia


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(description="Gives the first google result")
    async def google(self, ctx, *, query):
        for j in search(query, tld="co.in", num=2, stop=2, pause=1):
            await ctx.send(j)

    @commands.command(description="Wikipedia")
    async def wiki(self, ctx, *, query):
        try:
            res = discord.Embed(title=str(query).title(),
                                description=wikipedia.summary(query, sentences=3))
            await ctx.send(embed=res)
        except Exception:
            await ctx.send(f"Here is a page with all the links that contain {query} <https://en.wikipedia.org/wiki/"+query.title()+">")


def setup(client):
    client.add_cog(Info(client))
