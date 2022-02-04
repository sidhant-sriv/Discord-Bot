from os import name
import requests
import discord
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument
import mysql.connector
import math
import os


database_name = os.getenv('DATABASE_NAME')
database_password = os.getenv('DATABASE_PASSWORD')
database_username = os.getenv('DATABASE_USERNAME')
database_host = os.getenv('DATABASE_HOST')
API_URL = os.getenv('HUGGINGFACE_URL')
API_KEY = os.getenv('HUGGINGFACE_KEY')
headers = {"Authorization": str(API_KEY)}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


class User(commands.Cog):
    """Do stuff with your profile"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="create_user", aliases=["cu"])
    async def create_user(self, ctx):
        """Create user"""
        username = ctx.author.name
        info = "The name is " + username
        user_id = round(math.sqrt(ctx.author.id))
        # create the user
        db = mysql.connector.connect(
            host=database_host, user=database_username, passwd=database_password, database=database_name)
        cursor = db.cursor()
        try:
                   # Create the table user with user_id , username, info
            cursor.execute(
                "CREATE TABLE users (user_id INT, username VARCHAR(255), info VARCHAR(255))")
        except:
            pass
        print(user_id, username, info)
        cursor.execute(
            "INSERT INTO users (user_id, username,info) VALUES (%s,%s ,%s)", (user_id, username, info))
        db.commit()
        cursor.close()
        db.close()
        await ctx.send("`User created!`")
    # View the user

    @commands.command(name="view_user", aliases=["vu"])
    async def view_user(self, ctx):
        """View user"""
        user_id = round(math.sqrt(ctx.author.id))
        db = mysql.connector.connect(
            host=database_host, user=database_username, passwd=database_password, database=database_name)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
        result = cursor.fetchall()[0]
        # await ctx.send(result)
        res = discord.Embed(title=result[1], description=result[2])
        await ctx.send(embed=res)
        cursor.close()
        db.close()
    
    # Delete the user

    @commands.command(name="delete_user", aliases=["du"])
    async def delete_user(self, ctx):
        """Delete user"""
        user_id = round(math.sqrt(ctx.author.id))
        db = mysql.connector.connect(
            host=database_host, user=database_username, passwd=database_password, database=database_name)
        cursor = db.cursor()
        cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
        db.commit()
        cursor.close()
        db.close()
        await ctx.send("`User deleted!`")
    # Update info

    @commands.command(name="update_info", aliases=["ui"])
    async def update_info(self, ctx, *, info):
        """Update user info"""
        user_id = round(math.sqrt(ctx.author.id))
        db = mysql.connector.connect(
            host=database_host, user=database_username, passwd=database_password, database=database_name)
        cursor = db.cursor()
        cursor.execute(
            "UPDATE users SET info = %s WHERE user_id = %s", (info, user_id))
        db.commit()
        cursor.close()
        db.close()
        await ctx.send("`Info updated!`")
    # Add to the info

    @commands.command(name="add_info", aliases=["ai"])
    async def add_info(self, ctx, *, info):
        """Add to user info"""
        user_id = round(math.sqrt(ctx.author.id))
        db = mysql.connector.connect(
            host=database_host, user=database_username, passwd=database_password, database=database_name)
        cursor = db.cursor()
        cursor.execute(
            "UPDATE users SET info = CONCAT(info, %s) WHERE user_id = %s", (info, user_id))
        db.commit()
        cursor.close()
        db.close()
        await ctx.send("`Info updated!`")
    # Get users info

    @commands.command(name="get_info", aliases=["gi"])
    async def get_info(self, ctx, user: discord.Member = None):
        """Get information of user"""
        if user == None:
            user_id = round(math.sqrt(ctx.author.id))
        else:
            user_id = round(math.sqrt(user.id))
        db = mysql.connector.connect(
            host=database_host, user=database_username, passwd=database_password, database=database_name)
        cursor = db.cursor()
        cursor.execute("SELECT info FROM users WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        await ctx.send(result[0])
        cursor.close()
        db.close()
    # Clear users info

    @commands.command(name="clear_info", aliases=["ci"])
    async def clear_info(self, ctx):
        """Clear the info"""
        user_id = round(math.sqrt(ctx.author.id))
        db = mysql.connector.connect(
            host=database_host, user=database_username, passwd=database_password, database=database_name)
        cursor = db.cursor()
        cursor.execute(
            "UPDATE users SET info = '' WHERE user_id = %s", (user_id,))
        db.commit()
        cursor.close()
        db.close()
        await ctx.send("Info cleared!")
    @commands.command(name="ask", aliases=["a"])
    async def ask(self, ctx, user: discord.Member = None, *, question):
        """Ask a question from the user info"""
        if user == None:
            user_id = round(math.sqrt(ctx.author.id))
        else:
            user_id = round(math.sqrt(user.id))
        db = mysql.connector.connect(
            host=database_host, user=database_username, passwd=database_password, database=database_name)
        cursor = db.cursor()
        cursor.execute("SELECT info FROM users WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        cursor.close()
        db.close()
        context = result[0]
        # Check if user exists
        if context == None:
            await ctx.send("User does not exist")
        output = query({
            "inputs": {
                "question": question,
                "context": context,
            },
        })
        print(output)
        await ctx.send("```{}```".format(output["answer"]))

def setup(bot):
    bot.add_cog(User(bot))