"""
Slash commands for the bot - The `config` command
"""


class ConfigCommand:
    """
    The `config` command
    """

    name = "config"
    description = "Lol config"

    @staticmethod
    async def main(interaction, *args):
        """
        The `config` command
        TODO To be implemented
        """
        await interaction.response.send_message("Hello!")
