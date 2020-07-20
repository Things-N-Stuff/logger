from discord.ext import commands
from send_log import send_to_log
from settings import message_log_id, color_changed, color_deleted, color_sent

import discord


class Messages(commands.Cog):
    """Log messages sent, edited and deleted"""
    def __init__(self, bot):
        self.bot = bot

    async def log_message(self, message, type, before=None, attachments_old=None):
        """Gather information from the message and format it before
        sending it to message log channel
        """
        # Prevent logger from logging itself
        if message.author.id == self.bot.user.id:
            return 0

        # Prevent logger from logging Direct Messages
        if message.guild is None:
            return 0

        # Check for attachments in the message
        # Discord for desktop and web do not have the ability to send
        # multiple images within the same message. However, this is
        # possible on the mobile versions of discord and through bots.
        try:
            attachments = ""
            count = 1
            for a in message.attachments:
                attachments += f"[attachment{count}]({a.url})\n"
                count += 1
        except Exception:
            attachments = ""

        # Action dependent
        description = ""
        if type == 'Edited':
            color = color_changed
            description = f"Before:\n{before.content} {attachments_old}\n\nAfter:\n"
        elif type == 'Deleted':
            color = color_deleted
        elif type == 'Sent':
            color = color_sent

        # Create embed
        embed = discord.Embed(title=f"{message.author}",
                              description=f"{description}{message.content} {attachments}\n"
                              f"[jump to message]({message.jump_url})",
                              color=color)
        embed.set_footer(text=f"Author ID: {message.author.id}\nMessage ID: {message.id}")
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_author(name=f"Message {type} in #{message.channel}",
                         icon_url=self.bot.user.avatar_url)

        await send_to_log(self.bot, embed, channel_id=message_log_id)

    @commands.Cog.listener()
    async def on_message(self, message):
        """Detect Messages Sent"""
        await self.log_message(message, type='Sent')

    @commands.Cog.listener()
    async def on_message_edit(self, before, message):
        """Detect Messages Edited"""
        # This event is triggered when an embed is added or removed
        # from a messaged
        if before.content == message.content:
            return 0

        # Check for any attachments in the old message. The new message
        # will be checked in log_message()
        try:
            attachments_old = ""
            count = 1
            for a in before.attachments:
                attachments_old += f"[attachment{count}](a.url)\n"
                count += 1
        except Exception:
            attachments_old = ""

        await self.log_message(message, type='Edited', before=before,
                               attachments_old=attachments_old)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        """Detect Messages Deleted"""
        await self.log_message(message, type='Deleted')


def setup(bot):
    bot.add_cog(Messages(bot))
