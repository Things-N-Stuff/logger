from discord.ext import commands
from send_log import send_to_log
from settings import message_log_id, color_deleted, color_sent

import discord


class Reactions(commands.Cog):
    """Log reactions sent and deleted"""
    def __init__(self, bot):
        self.bot = bot

    async def log_reaction(self, reaction, user, type):
        """Gather information about the reaction before sending it to
        the message log channel
        """
        # Prevent logger from logging itself
        if user.id == self.bot.user.id:
            return 0

        # Prevent logger from logging Direct Messages
        if reaction.message.guild is None:
            return 0

        # Action dependent
        if type == 'Deleted':
            color = color_deleted
        elif type == 'Sent':
            color = color_sent

        # Create embed
        embed = discord.Embed(title=f"{user}",
                              description=f"{reaction.emoji}\n"
                              f"[jump to message]({reaction.message.jump_url})",
                              color=color)
        embed.set_footer(text=f"Author ID: {user.id}\nMessage ID: {reaction.message.id}")
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_author(name=f"Reaction {type} in #{reaction.message.channel}",
                         icon_url=self.bot.user.avatar_url)

        # Unicode Emoji's won't have an attached url so we should grab
        # the url from https://twemoji.maxcdn.com
        try:
            embed.set_image(url=reaction.emoji.url)
        except AttributeError:
            # Get the unicode of the emoji
            # Some emojis are actually multiple emojis combined
            unicodes = []
            for emoji in reaction.emoji:
                unicodes.append(f"{ord(emoji):x}")

            filename = '-'.join(unicodes)
            embed.set_image(url=f"https://twemoji.maxcdn.com/v/latest/72x72/{filename}.png")

        # Send message to log channel
        await send_to_log(self.bot, embed, channel_id=message_log_id)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        """Detect Reactions Sent"""
        await self.log_reaction(reaction, user, type='Sent')

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        """Detect Reactions Deleted"""
        await self.log_reaction(reaction, user, type='Deleted')


def setup(bot):
    bot.add_cog(Reactions(bot))
