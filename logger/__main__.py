"""Startup the bot with everything necessary"""

# Import Discord Library
from discord.ext import commands
import discord

# Import settings for starting up the bot
from settings import command_prefix, token

# Import bot admins
from settings import bot_admin_ids

# Import sys so we can send errors to stderr
import sys

# Base Bot
bot = commands.Bot(command_prefix=command_prefix,
                   status=discord.Status.idle,
                   activity=discord.Game(name='Starting...'))


@bot.event
async def on_ready():
    """Output to stdout when the bot is ready"""
    print(f"{bot.user.name}: {bot.user.id}")
    print("Ready!")
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game(name='Watchful Eye'))


@bot.command()
async def load(ctx, cog: str):
    """Load a cog. This will not re-evaluate the cog's code. Can only
    be used by bot admins
    """
    if ctx.message.author.id in bot_admin_ids:
        try:
            bot.load_extension(f"cogs.{cog}")
            await ctx.message.add_reaction('\N{THUMBS UP SIGN}')
        except Exception as error:
            print(error, file=sys.stderr)
            await ctx.send(f"```python\n{error}```")


@bot.command()
async def unload(ctx, cog: str):
    """Unload a cog. Useful if a cog is behaving badly. Can only be
    used by bot admins
    """
    if ctx.message.author.id in bot_admin_ids:
        try:
            bot.unload_extension(f"cogs.{cog}")
            await ctx.message.add_reaction('\N{THUMBS UP SIGN}')
        except Exception as error:
            print(error, file=sys.stderr)
            await ctx.send(f"```python\n{error}```")


@bot.command()
async def reload(ctx, cog: str):
    """Re-evaluate the cog's code. Useful if the cog's code has changed.
    Can only be used by bot admins
    """
    if ctx.message.author.id in bot_admin_ids:
        try:
            bot.reload_extension(f"cogs.{cog}")
            await ctx.message.add_reaction('\N{THUMBS UP SIGN}')
        except Exception as error:
            print(error, file=sys.stderr)
            await ctx.send(f"```python\n{error}```")


bot.load_extension('cogs.Messages')
bot.load_extension('cogs.Reactions')
bot.run(token)
