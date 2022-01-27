import discord
import os
import imgurpython
import requests
from discord.ext import commands
import random
import praw
from textblob import TextBlob
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv('../.env'))
CLIENT_ID = os.environ['REDDIT_CLIENT_ID']
CLIENT_SECRET = os.environ['REDDIT_CLIENT_SECRET']
USER_AGENT = os.environ['REDDIT_USER_AGENT']
IMGUR_ID = os.environ['IMGUR_CLIENT_ID']
IMGUR_SECRET = os.environ['IMGUR_CLIENT_SECRET']

class Fun(commands.Cog):
    """Stuff that's fun"""
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        """Magic 8ball"""
        responses = ["It is certain.",
                     "It is decidedly so.",
                     "Without a doubt.",
                     "Yes - definitely.",
                     "You may rely on it.",
                     "As I see it, yes.",
                     "Most likely.",
                     "Outlook good.",
                     "Yes.",
                     "Signs point to yes.",
                     "Reply hazy, try again.",
                     "Ask again later.",
                     "Better not tell you now.",
                     "Cannot predict now.",
                     "Concentrate and ask again.",
                     "Don't count on it.",
                     "My reply is no.",
                     "My sources say no.",
                     "Outlook not so good.",
                     "Very doubtful."]
        res = discord.Embed(title=f'Question : **{question}**',description=f'Answer: **{random.choice(responses)}**')
        await ctx.send(embed=res)

    @commands.command()
    async def meme(self, ctx):
        """Gets memes from Reddit"""
        reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_CLIENT_SECRET,
                             user_agent=REDDIT_USER_AGENT, check_for_async=False)
        post = reddit.subreddit(
            'memes+dankmemes+me_irl+MadeMeSmile+cursedcomments').hot(limit=20)
        post = [i for i in post]
        post = random.choice(post)
        res = discord.Embed(
            title=f'**{post.title}**', url=f'https://reddit.com{post.permalink}', colour=discord.Colour(0x000000))
        res.set_footer(text=f'{post.score} 👍')
        res.set_image(url=post.url)
        await ctx.send(embed=res)

    @commands.command()
    async def joke(self, ctx):
        """Returns a joke from r/Jokes and r/darkjokes"""
        reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_CLIENT_SECRET,
                             user_agent=REDDIT_USER_AGENT, check_for_async=False)

        post = reddit.subreddit('Jokes+darkjokes').hot(limit=30)
        post = [i for i in post]
        post = random.choice(post)

        res = discord.Embed(
            title=f'**{post.title}**', url=f'https://reddit.com{post.permalink}', description=post.selftext, colour=discord.Colour(0x000000))
        await ctx.send(embed=res)

    @commands.command(aliases=["senti"])
    async def sentiment(self, ctx, *, sentence):
        """Returns sentiment of a sentence"""
        if sentence:
            words = TextBlob(sentence)
            res = discord.Embed(title=f'{sentence}', description= f'Calculated sentiment {words.sentiment.polarity}')
            res.set_footer(text="If value>0 then positive, <0 then negative and =0 then neutral sentiment")
            await ctx.send(embed=res)
    @commands.command()
    async def imgur(self, ctx, *, query):
        """Returns an image from imgur"""
        if query:
            client = imgurpython.ImgurClient(IMGUR_ID,IMGUR_SECRET)
            items = client.gallery_search(query)[:]
            post = random.choice(items)
            res = discord.Embed(title=post.title)
            res.set_image(url=post.link)
            await ctx.send(post.link)

def setup(client):
    client.add_cog(Fun(client))
