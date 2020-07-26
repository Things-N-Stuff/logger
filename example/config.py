"""
Move this file to the configuration directory. The configuration
directory can be specified with the environment variable
LOGGER_CONFIG_DIR if you want to change the location of configuration
files. Otherwise, logger will look for configuration files in these two
locations in this order if on a posix system (Linux, BSD, macOS).

    $XDG_CONFIG_HOME/logger
    ~/.config/logger

When on an nt system (Windows), logger will look for configuration
files in the following directory.

    %USERPROFILE%\\AppData\\Local\\logger
"""

# This is required for the bot to do anything. You can aquire a bot
# token from https://discord.com/developers/applications.
bot_token = 'insert bot token here'

# ID for channel where the bot will send audit logs
# Leave empty to not log the audit log 
audit_log_channel_id = 

# ID for channel where the bot will send message logs
# Leave empty to not log messages
message_log_channel_id = 

# ID for channel where the bot will send voice logs
# Leave empty to not log voice activity
voice_chat_log_channel_id = 

# Tuple of user ids that can issue special commands to the bot
# The first id should be the id of the person hosting the bot
bot_admins = (user_id1, user_id2, user_id3)

# Colors the bot will use for embeds
sent_color = 0xE3E5E8
changed_color = 0xFAA61A
deleted_color = 0xF04747

# Command prefix for the bot
bot_command_prefix = './l '
