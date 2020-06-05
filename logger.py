#!/usr/bin/env python3

# Import discord.py Library
from discord.ext import commands
import discord

# Import Config
from config import auditlog_id
from config import bot_admins
from config import bot_prefix
from config import bot_token
from config import msglog_id
from config import vclog_id


# Setup commands.Bot with some base variables
bot = commands.Bot(command_prefix=bot_prefix,
                   help_command=None,
                   status=discord.Status.idle,
                   activity=discord.Game(name='Starting...'))

# When the bot is ready, print a message to stdout and change discord status
@bot.event
async def on_ready():
    print(f"{bot.user.name}: {bot.user.id}")
    print("Ready!")
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Game(name='Watchful Eye'))

# Send a Message to a Log Channel
async def send_to_log(channel_id, embed, *args, **kwargs):
    channel = bot.get_channel(channel_id)
    await channel.send(embed=embed)

# Log Messages Sent
@bot.event
async def on_message(message):
    # Don't Log our own messages
    if message.author.id == bot.user.id:
        return 0

    # Don't Log Direct Messages
    if message.guild == None:
        return 0

    # Check for attachments within the message
    try: a = f"[attachment]({message.attachments[0].url})"
    except: a = ""

    # Create Embed
    em = discord.Embed(title=f"{message.author}",
                       description=f"{message.content} {a}\n" \
                       f"[jump to message]({message.jump_url})",
                       colour=0xE3E5E8)
    em.set_footer(text=f"Author ID: {message.author.id}\n" \
                  f"Message ID: {message.id}")
    em.set_thumbnail(url=message.author.avatar_url)
    em.set_author(name=f"Message Sent in #{message.channel}",
                  icon_url=bot.user.avatar_url)

    # Send Embed Message to Log Channel
    await send_to_log(channel_id=msglog_id, embed=em)

# Log Edited Messages
@bot.event
async def on_message_edit(before, after):
    # Don't detect our own messages
    if after.author.id == bot.user.id:
        return 0

    # Don't Log Direct Messages
    if after.guild == None:
        return 0

    # This event is triggered when a link gets an embed added or removed.
    # The before and after messages should equal eachother, so check for this
    # before continuing.
    if before.content == after.content:
        return 0

    # Check for attachments in the old message
    try: a_old = f"[attachment]({before.attachments[0].url})"
    except: a_old = ""

    # Check for attachments in the new message
    try: a = f"[attachment]({after.attachments[0].url})"
    except: a = ""

    # Create Embed
    em = discord.Embed(title=f"{after.author}",
                       description=f"Before:\n{before.content} {a_old}\n\n" \
                       f"After:\n{after.content} {a}\n" \
                       f"[jump to message]({after.jump_url})",
                       color=0xFAA61A)
    em.set_footer(text=f"Author ID: {after.author.id}\n" \
                  f"Message ID: {after.id}")
    em.set_thumbnail(url=after.author.avatar_url)
    em.set_author(name=f"Message Edited in #{after.channel}",
                  icon_url=bot.user.avatar_url)

    # Send Message to Log Channel
    await send_to_log(channel_id=msglog_id, embed=em)

# Log Deleted Messages
@bot.event
async def on_message_delete(message):
    # Don't Log Ourselves
    if message.author.id == bot.user.id:
        return 0

    # Don't Log Direct Messages
    if message.guild == None:
        return 0

    # Check for attachments
    try: a = f"[attachment]({message.attachments[0].url})"
    except: a = ""

    # Create Embed
    em = discord.Embed(title=f"{message.author}",
                       description=f"{message.content} {a}\n" \
                       f"[jump to message]({message.jump_url})",
                       color=0xF04747)
    em.set_footer(text=f"Author ID: {message.author.id}\n" \
                  f"Message ID: {message.id}")
    em.set_thumbnail(url=message.author.avatar_url)
    em.set_author(name=f"Message Deleted in #{message.channel}",
                  icon_url=bot.user.avatar_url)

    # Send Message to Log Channel
    await send_to_log(channel_id=msglog_id, embed=em)

# Log Reactions Added
@bot.event
async def on_reaction_add(reaction, user):
    return 0

# Log Reactions Removed
@bot.event
async def on_reaction_remove(reaction, user):
    return 0

bot.run(bot_token)
