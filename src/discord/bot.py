from typing import Optional

import discord

from src.util.singleton import Singleton

from src.discord.embed.factory.exception import ExceptionEmbedFactory
from src.discord.handler.rooter import MessageHandler

from config import (
    DISCORD_INTENTS,
    DISCORD_TOKEN
)


class DiscordBOT(Singleton, discord.Client):
    def __init__(self):
        super(DiscordBOT, self).__init__(
            presences=True,
            guild_subscriptions=True,
            intents=DISCORD_INTENTS)
        self.guild: Optional[discord.Guild] = None
        self.main_channel: Optional[discord.TextChannel] = None

    def launch(self):
        self.run(DISCORD_TOKEN)

    async def on_ready(self):
        self.guild = self.guilds[0]

    async def on_message(self, message):
        handler: MessageHandler = MessageHandler(
            message=message,
            context={
                "guild": self.guild,
                "main_channel": self.main_channel
            })

        try:
            await handler.execute()
        except Exception as e:
            embed: discord.Embed = ExceptionEmbedFactory(
                exception=e
            ).make()
            await self.main_channel.send(embed=embed)

            raise e
