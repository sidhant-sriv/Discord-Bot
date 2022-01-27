# TODO Base64

from email import utils
import discord
from discord.ext import commands
import hashlib


class CaeserCipher:

    def encrypt(self, text, key):
        result = ""
        for i in text:
            if i.isupper():
                result += chr((ord(i)+key-65) % 26+65)
            elif i.islower():
                result += chr((ord(i)+key-97) % 26+97)
            else:
                result += i
        return result

    def decrypt(self, text, key):
        result = ""
        for i in text:
            if i.isupper():
                result += chr((ord(i)-key-65) % 26+65)
            elif i.islower():
                result += chr((ord(i)-key-97) % 26+97)
            else:
                result += i
        return result


class SHA256:
    def __init__(self, text):
        self.text = text
        self.hash = hashlib.sha256(text.encode('utf-8')).hexdigest()

    def __str__(self):
        return self.hash


class MD5:
    def __init__(self, text):
        self.text = text
        self.hash = hashlib.md5(text.encode('utf-8')).hexdigest()

    def __str__(self):
        return self.hash


class Base64:
    def encode(self, text):
        return text.encode('utf-8').decode('base64')

    def decode(self, text):
        return text.decode('base64')


class Cryptography(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def caeser_e(self, ctx, *, text):
        await ctx.send(CaeserCipher.encrypt(text, 3))

    @commands.command()
    async def caeser_d(self, ctx, key, *, text):
        print(key)
        await ctx.send(CaeserCipher.decrypt(text, 3))

    @commands.command()
    async def sha256(self, ctx, *, text):
        await ctx.send(SHA256(text))

    @commands.command()
    async def md5(self, ctx, *, text):
        await ctx.send(MD5(text))

    @commands.command()
    async def base64_e(self, ctx, *, text):
        await ctx.send(Base64.encode(text))

    @commands.command()
    async def base64_d(self, ctx, *, text):
        await ctx.send(Base64.decode(text))


def setup(client):
    client.add_cog(Cryptography(client))
