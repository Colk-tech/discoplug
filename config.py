import os

import discord

DISCORD_TOKEN: str = os.environ["DISCOPLUG_TOKEN"]

DISCORD_INTENTS = discord.Intents.all()
DISCORD_INTENTS.members = True

COMMAND_PREFIX: str = "!gce"

MY_NAME: str = "GCE Controller"
