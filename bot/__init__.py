"""
Vela Memer - Python rewrite
"""
import os
from discord import Client, Intents
from . import test, commands


def run_main() -> None:
    """
    Run the bot

    :return: None
    """
    bot = Client(intents=Intents.default())

    @bot.event
    async def on_ready():
        await commands.register_handlers(bot)
        print("Ready!")

    token = os.getenv("BOT_TOKEN")
    if token is not None:
        bot.run(token)  # type: ignore


def run_tests() -> None:
    """
    Run tests to ensure everything works properly

    :return: None
    """
    test.run_all_tests()
