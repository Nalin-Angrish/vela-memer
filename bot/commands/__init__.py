"""
Slash commands for the bot
"""
from discord import Client
from discord.app_commands import CommandTree

from .help import HelpCommand
from .config import ConfigCommand
from .meme import MemeCommand


async def register_handlers(bot: Client):
    """
    Register slash command handlers for the bot

    :param Client bot: The bot to register all commands to
    """
    command_tree = CommandTree(bot)
    help_command = command_tree.command(
        name=HelpCommand.name, description=HelpCommand.description
    )
    help_command(HelpCommand.main)
    config_command = command_tree.command(
        name=ConfigCommand.name, description=ConfigCommand.description
    )
    config_command(ConfigCommand.main)
    meme_command = command_tree.command(
        name=MemeCommand.name, description=MemeCommand.description
    )
    meme_command(MemeCommand.main)
    await command_tree.sync()
