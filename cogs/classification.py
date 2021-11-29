import discord
from discord.ext import commands
from PIL import Image, ImageFilter
from io import BytesIO
import os
import requests

class ImageManipulation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='classify')
    async def show(self, ctx,  image_url: str = None):
        # if user == None:
        #     user = ctx.author
        # if image_url == None:
        #     image_url = user.avatar_url
        url = os.environ['CLASSIFICATION_URL']
        data = {
            "image_url": str(image_url),
        }
        r = requests.post(url, json=data).json()
        res = []
        for i in r['data']:
            res.append(i['classification'])
        await ctx.send(res)


def setup(bot):
    bot.add_cog(ImageManipulation(bot))
