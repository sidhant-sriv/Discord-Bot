import asyncio
import xkcd
from discord.ext import commands as c
import discord


class XKCD(c.Cog):
    """A plugin for those on the internet with good humor."""

    def __init__(self, bot):
        self.bot = bot

    async def get_comic(self, comic, number=None):
        case = {
            "latest": lambda: xkcd.getLatestComic(),
            "random": lambda: xkcd.getRandomComic(),
            "numbemysql-connector-pythonr": lambda: xkcd.getComic(number),
        }
        function = case.get(comic, None)
        comic = self.bot.loop.run_in_executor(None, function)
        while True:
            await asyncio.sleep(0.25)
            if comic.done():
                comic = comic.result()
                break
        try:
            link = comic.getImageLink()
            title = comic.getAsciiTitle().decode("ascii")
            alt_text = comic.getAsciiAltText().decode("ascii")
            number = comic.number
            return [number, link, title, alt_text]
        except AttributeError:
            return "\U00002754 Can't find that comic."

    @c.group(pass_context=True)
    async def xkcd(self, ctx):
        """
        Running the command without arguments will display a random comic.
        """
        if ctx.invoked_subcommand is None:
            comic = await self.get_comic("random")
            res = discord.Embed(
                title=comic[2], url=comic[1], description=f"**Comic number {comic[0]}**", colour=discord.Colour(0xB0B0BF))
            res.set_image(url=comic[1])
            res.set_footer(text=comic[-1])
            await ctx.send(embed=res)

    @xkcd.command(name="latest")
    async def xkcd_latest(self, ctx):
        """Get the latest xkcd comic."""
        comic = await self.get_comic("latest")
        res = discord.Embed(
            title=comic[2], url=comic[1], description=f"Comic number {comic[0]}", colour=discord.Colour(0xB0B0BF))
        res.set_image(url=comic[1])
        res.set_footer(text=comic[-1])
        await ctx.send(embed=res)

    @xkcd.command(name="number")
    async def xkcd_number(self, ctx, number: int):
        """Get an xkcd comic by number."""
        comic = await self.get_comic("number", number)
        res = discord.Embed(
            title=comic[2], url=comic[1], description=f"Comic number {comic[0]}", colour=discord.Colour(0xB0B0BF))
        res.set_image(url=comic[1])
        res.set_footer(text=comic[-1])
        await ctx.send(embed=res)


def setup(bot):
    bot.add_cog(XKCD(bot))
