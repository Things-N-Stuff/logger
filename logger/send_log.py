"""Very simple function to send logs to the correct channel"""


async def send_to_log(bot, embed, channel_id):
    """Send embed to channel corresponding with channel id"""
    channel = bot.get_channel(channel_id)
    await channel.send(embed=embed)
