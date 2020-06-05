# Logger
Bot to log messages and server activity on a server.
This bot has only been tested on one server at a time.

## Logging Capabilities
 - [x] Messages
   - [x] Sent
   - [x] Edited
   - [x] Deleted 
   - [ ] Reactions
     - [ ] Added
     - [ ] Removed
 - [ ] Audit Log
 - [ ] Voice Activity
   - [ ] Joined Channel
   - [ ] Left Channel

## Requirements
 - python3
 - [discord.py](https://github.com/Rapptz/discord.py)

## Using the Bot
If you haven't already, clone this repo by running the following command.

```
git clone https://github.com/yemouu/logger
```

Before you can actually start using the bot, you will need to create your own `config.py`.
The sample config is `config.py.sample` and holds all possible configuration options aswell as a comment describing what each is for.

After configuration, just run `python logger.py`.
