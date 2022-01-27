# TODO Caeser cipher, encrypt and decrypt
# TODO SHA256
# TODO MD5
# TODO Base64

from email import utils
import discord
from discord.ext import commands
from ..utils import CaeserCipher


class Crypto(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def caeser_e(self, ctx, *, text):
        await ctx.send(CaeserCipher.encrypt(text, 3))

    @commands.command()
    async def caeser_d(self, ctx, key, *, text):
        print(key)
        await ctx.send(CaeserCipher.decrypt(text, 3))


def setup(self, client):
    client.add_cog(Crypto(client))
