"""Import the user configuration file and setup variables for easier
use in other modules
"""

import os
import sys

# Determine where to place config files.
# Use LOGGER_CONFIG_DIR if it is set within the environment
if os.getenv("LOGGER_CONFIG_DIR") is not None:
    config_dir = os.getenv("LOGGER_CONFIG_DIR")

# Set config dir based on platform if LOGGER_CONFIG_DIR is not available
else:
    home_dir = os.path.expanduser("~")

    if os.name == 'posix':
        config_base = os.getenv("XDG_CONFIG_HOME", os.path.join(home_dir, ".config"))
    elif os.name == 'nt':
        config_base = os.path.join(home_dir, "AppData", "Local")
    else:
        print("Could not determine where to place config files", file=sys.stderr)
        sys.exit(1)

    config_dir = os.path.join(config_base, "logger")

# Add the configuration directory to python path
if config_dir not in sys.path:
    sys.path.insert(0, config_dir)

try:
    from config import bot_token, audit_log_channel_id, message_log_channel_id
    from config import voice_chat_log_channel_id, bot_admins, sent_color, changed_color
    from config import deleted_color, bot_command_prefix
except ImportError as error:
    print("Failed to import config.py. Check the README.md.", file=sys.stderr)
    print(error, file=sys.stderr)
    sys.exit(1)

token = bot_token

audit_log_id = audit_log_channel_id
message_log_id = message_log_channel_id
voice_log_id = voice_chat_log_channel_id

bot_host_id = bot_admins[0]
bot_admin_ids = bot_admins

color_sent = sent_color
color_changed = changed_color
color_deleted = deleted_color

command_prefix = bot_command_prefix

version = '0.1.0'
