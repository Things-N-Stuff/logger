"""Main function of logger. Start logger aswell as define commands and
load cogs
"""

# Import Discord Library
from discord.ext import commands
import discord

# Import settings
from settings import bot_admin_ids, bot_host_id, command_prefix, token, version

# Import sys so we can send errors to stderr
import sys

# Base Bot
bot = commands.Bot(command_prefix=command_prefix, status=discord.Status.idle,
                   activity=discord.Game(name='Starting...'))


@bot.event
async def on_ready():
    """Output to stdout when the bot is ready"""
    print(f"logger version: {version}")
    print(f"{bot.user.name}: {bot.user.id}")
    print("---Ready!---")
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game(name='Watchful Eye'))


@bot.command()
async def load(ctx, cog: str):
    """Load a cog back into the bot if the cog was unloaded. Can only
    be used by bot admins
    """
    if ctx.message.author.id in bot_admin_ids:
        try:
            bot.load_extension(f"cogs.{cog}")
            await ctx.message.add_reaction('\U0001F44D')
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
            await ctx.message.add_reaction('\U0001F44D')
        except Exception as error:
            print(error, file=sys.stderr)
            await ctx.send(f"```python\n{error}```")


@bot.command()
async def reload(ctx, cog: str):
    """Re-evaluate the cog's code. Useful if working on the cog's code
    and you want to quickly test your changes. Can only be used by bot
    admins
    """
    if ctx.message.author.id in bot_admin_ids:
        try:
            bot.reload_extension(f"cogs.{cog}")
            await ctx.message.add_reaction('\U0001F44D')
        except Exception as error:
            print(error, file=sys.stderr)
            await ctx.send(f"```python\n{error}```")


@bot.command()
async def shutdown(ctx):
    """Allows the bot host to shutdown the bot. Useful if the host
    doesn't have access to the console
    """
    if ctx.message.author.id == bot_host_id:
        print(f"Shutdown issued by: {ctx.message.author}({ctx.message.author.id})")
        await ctx.message.add_reaction('\U0001F44B')

        # Ensure that the bot has exited
        try:
            await bot.close()
        except Exception as error:
            print(error)
            sys.exit(1)


bot.load_extension('cogs.Messages')
bot.load_extension('cogs.Reactions')
bot.run(token)
