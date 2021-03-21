# discord_slash.py
Attempting to create a framework for Discord Slash commands... yes

# Disclaimer
This is heavily made to target 1 server only, whenever I get a good, modular slash command handler, I will start converting this in to a framework. Feel free to make pull requests if you have ideas on how this can be improved. ❤

# Quick understanding
There's a folder named **slashpy** where I attempt to create the modular slash manager. While the folder **commands** is where the magic happens with commands. Goal is to make a really good modular Discord Slash manager with webhooks only. Documentation is limited, as I haven't gotten that far, sorry for my shitcode, I'm just trying to get things working, then actually clean it up a bit.

# Why is it forced to a guild?
Because I hate having the 1 hour cache when testing the output of these shits, so while I test, it will be controlled by config.json on which guild_id it will make commands to.

# Webhook manager
The main file that manages webhook requests is **index.py**. Plan is to keep it public so anyone can change how their Slash webhook should be managed.

# Commands folder
- Class name = Command name
- Class doc = Command desc.
- async reply = The JSON sent back as reply to Discord's POST webhook