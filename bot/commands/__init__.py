"""
Slash commands for the bot
"""
from typing import Union
from discord import Client, TextChannel, Interaction
from discord.app_commands import CommandTree

from .help import HelpCommand
from .config import ConfigCommand
from .meme import MemeCommand


def register_handlers(bot: Client) -> CommandTree:
    """
    Generate a slash command tree for the bot

    :param Client bot: The bot to register all commands to
    :return: The command tree
    :rtype: CommandTree
    """
    command_tree = CommandTree(bot)

    @command_tree.command(name=HelpCommand.name, description=HelpCommand.description)
    async def help_command(interaction:Interaction):
        await interaction.response.defer()
        await HelpCommand.main(interaction)

    @command_tree.command(name=MemeCommand.name, description=MemeCommand.description)
    async def meme_command(interaction:Interaction, quantity: Union[int, None] = 1):
        await interaction.response.defer()
        await MemeCommand.main(interaction, quantity=quantity)

    @command_tree.command(
        name=ConfigCommand.name, description=ConfigCommand.description
    )
    async def config_command(
        interaction:Interaction,
        channel: Union[TextChannel, None] = None,
        frequency: Union[int, None] = None,
        num_memes: Union[int, None] = None
    ):
        await interaction.response.defer()
        await ConfigCommand.main(
            interaction,
            channel=channel,
            frequency=frequency,
            num_memes=num_memes
        )

    return command_tree
