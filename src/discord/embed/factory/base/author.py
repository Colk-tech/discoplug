from config import (
    MY_NAME
)
from src.discord.embed.factory.base.abs import AbstractEmbedFactory


class AuthorEmbedFactoryBase(AbstractEmbedFactory):
    _AUTHOR_NAME: str = MY_NAME
