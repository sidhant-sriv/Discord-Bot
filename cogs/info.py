import discord as discord
from discord.ext import commands
from googlesearch import search
import wikipedia
import requests

class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(description="Gives the first google result")
    async def google(self, ctx, *, query):
        """Google search"""
        st=""
        for j in search(query, tld="co.in", num=8, stop=8, pause=1):
            html_content=requests.get(j).content.decode()
            title=html_content[html_content.find("<title>")+len("<title>"):html_content.find("</title>")]
            st=st+"\n"+title+":"+str(j)
        await ctx.send(embed=discord.Embed(title="Google Search", description=st))

    @commands.command(description="Wikipedia")
    async def wiki(self, ctx, *, query):
        """Wikipedia search"""
        try:
            t = str(wikipedia.search(query)[0].encode("utf-8"))
            res = discord.Embed(title=str(t).title()[
                                2:-1], description=wikipedia.summary(t, sentences=4))
            res.set_thumbnail(url=wikipedia.page(t).images[0])
            # res.set_image(url=wikipedia.page(t).images[1])
            await ctx.send(embed=res)
        except Exception:
            await ctx.send(f"Here is a page with all the links that contain {query} <https://en.wikipedia.org/wiki/"+query.title()+">")


def setup(client):
    client.add_cog(Info(client))
