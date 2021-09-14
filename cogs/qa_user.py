# This will be the user creation cog using mysql connector
from os import name
import discord
from discord.ext import commands
import mysql.connector
import math
import os
database_password = os.environ.get('DATABASE_PASSWORD')
database_username = os.environ.get('DATABASE_USERNAME')
class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="create_user", aliases=["cu"])
    async def create_user(self, ctx):
        username = ctx.author.name
        info = "The name is " + username
        user_id = round(math.sqrt(ctx.author.id))
        # create the user
        db = mysql.connector.connect(
            host="localhost", user=database_username, passwd=database_password, database="discord_bot")
        cursor = db.cursor()
        print(user_id, username, info)
        cursor.execute(
            "INSERT INTO users (user_id, username,info) VALUES (%s,%s ,%s)", (user_id, username, info))
        db.commit()
        cursor.close()
        db.close()
        await ctx.send("User created!")
    #View the user
    @commands.command(name="view_user", aliases=["vu"])
    async def view_user(self, ctx):
        user_id = round(math.sqrt(ctx.author.id))
        db = mysql.connector.connect(
            host="localhost", user=database_username, passwd=database_password, database="discord_bot")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
        result = cursor.fetchall()
        for row in result:
            await ctx.send(row)
        cursor.close()
        db.close()
    #Delete the user
    @commands.command(name="delete_user", aliases=["du"])
    async def delete_user(self, ctx):
        user_id = round(math.sqrt(ctx.author.id))
        db = mysql.connector.connect(
            host="localhost", user=database_username, passwd=database_password, database="discord_bot")
        cursor = db.cursor()
        cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
        db.commit()
        cursor.close()
        db.close()
        await ctx.send("User deleted!")
    #Update info
    @commands.command(name="update_info", aliases=["ui"])
    async def update_info(self, ctx,*, info):
        user_id = round(math.sqrt(ctx.author.id))
        db = mysql.connector.connect(
            host="localhost", user=database_username, passwd=database_password, database="discord_bot")
        cursor = db.cursor()
        cursor.execute(
            "UPDATE users SET info = %s WHERE user_id = %s", (info, user_id))
        db.commit()
        cursor.close()
        db.close()
        await ctx.send("User updated!")
    #Add to the info
    @commands.command(name="add_info", aliases=["ai"])
    async def add_info(self, ctx,*, info):
        user_id = round(math.sqrt(ctx.author.id))
        db = mysql.connector.connect(
            host="localhost", user=database_username, passwd=database_password, database="discord_bot")
        cursor = db.cursor()
        cursor.execute(
            "UPDATE users SET info = CONCAT(info, %s) WHERE user_id = %s", (info, user_id))
        db.commit()
        cursor.close()
        db.close()
        await ctx.send("User updated!")
def setup(bot):
    bot.add_cog(User(bot))
