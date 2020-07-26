# Logger
Discord bot to log activity on a server. This bot is meant to work on one server at a time.

## Logging Capabilities
 - [x] Messages
   - [x] Sent
   - [x] Edited
   - [x] Deleted 
   - [X] Reactions
     - [X] Added
     - [X] Removed
 - [ ] Audit Log
 - [ ] Voice Activity
   - [ ] Joined Channel
   - [ ] Left Channel

## Requirements
 - python3 (tested on python 3.7)
 - [discord.py](https://github.com/Rapptz/discord.py) (tested on discord.py 1.3.4)

## Using the Bot
Clone the repository or grab the source code from the releases tab.

A configuration file will be necessary for the bot to run properly. An example configuration with
all options is available in the example directory. On posix systems (Linux, BSD, macOS), the
`config.py` will be expected in either `$XDG_CONFIG_HOME/logger` or `$HOME/.config/logger`
depending on if `$XDG_CONFIG_HOME` is set. On nt systems (Windows), the `config.py` will be
expected in `%USERPROFILE%\\AppData\\Local\\logger`. If the environment variable
`LOGGER_CONFIG_DIR` is set, the configuration file can be placed anywhere on the filesystem.

After configuration, simply run `python logger`. If `python -V` is python 2.x.x, use `python3`
instead of `python`.
