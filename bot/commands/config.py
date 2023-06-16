"""
Slash commands for the bot - The `config` command
"""
from typing import Union
from discord import Interaction, TextChannel
from ..lib import Guild


class ConfigCommand:
    """
    The `config` command
    """

    name = "config"
    description = "Configure Vela Memer"

    @staticmethod
    async def main(
        interaction: Interaction,
        *args,
        channel: Union[TextChannel, None] = None,
        frequency: Union[int, None] = None,
        num_memes: Union[int, None] = None
    ):
        """
        The `config` command

        :param TextChannel channel: Channel in which to send the memes
        :param int frequency: How frequently to send the memes (/help for more info)
        :param int num_memes: How many memes to send in one go
        """
        if interaction.guild_id is None:
            await interaction.response.send_message(
                "Cannot do this in DMs, try doing it in a Discord server"
            )
        elif not interaction.permissions.manage_guild:
            await interaction.response.send_message(
                "C'mon bruh how could you even think you were allowed to do this?"
            )
        else:
            Guild.update(interaction.guild_id, channel, frequency, num_memes)
            await interaction.response.send_message("The settings have been updated!")
