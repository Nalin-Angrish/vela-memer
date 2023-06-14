"""
Vela Memer - Python rewrite
"""
import os
from discord import Client, Intents, Guild, Embed
from sqlalchemy import create_engine
from . import test, commands
from .lib import Base, Guild as DBGuild


def run_main() -> None:
    """
    Run the bot

    :return: None
    """
    bot = Client(intents=Intents.default())
    engine = create_engine(os.environ["DB_URI"])
    Base.metadata.create_all(engine)
    Base.engine = engine

    @bot.event
    async def on_ready():
        """
        When the client is ready, register handlers for all
        application commands and inform the standard output
        """
        await commands.register_handlers(bot)
        print("Ready!")

    @bot.event
    async def on_guild_join(guild: Guild):
        """
        When the bot joins a new guild, add the guild to the
        database and send a greeting message
        """
        main_channel = None
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                main_channel = channel
                break
        if main_channel is not None:
            await main_channel.send(
                embed=Embed(
                    title="Hello World!",
                    description="Thanks for inviting me to this server.\n\
                        To start getting memes from my awesome meme collection, you'll need to run some commands.\n\
                        To know more about those commands and me, run `/help`",
                )
            )
        DBGuild.new(guild.id, main_channel)
        print(guild.id, "Added")

    @bot.event
    async def on_guild_remove(guild: Guild):
        DBGuild.remove(guild.id)
        print(guild.id, "Removed")

    token = os.getenv("BOT_TOKEN")
    if token is not None:
        bot.run(token)  # type: ignore


def run_tests() -> None:
    """
    Run tests to ensure everything works properly

    :return: None
    """
    test.run_all_tests()
