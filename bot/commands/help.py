"""
Slash commands for the bot - The `help` command
"""
from discord import Embed, Interaction


class HelpCommand:
    """
    The `help` command
    """

    name = "help"
    description = "A help menu for you noobs."

    @staticmethod
    async def main(interaction: Interaction, *args):
        """
        The `help` command
        """
        help_message = Embed(
            title="Vela Memer's help menu",
            description="The slash commands that can be used with this bot are described below:",
        )
        help_message.add_field(name="`/help`", value="Shows this message.")
        help_message.add_field(name="`/meme`", value="Sends you a meme.")
        help_message.add_field(
            name="`/meme <n>`",
            value="Sends you `n` memes. `n` should be a number between 1 and 10.",
        )
        help_message.add_field(
            name="`/config <channel> <frequency> <num_memes>`",
            value="Helps you configure the options for this server. It's options are described in more detail below.",
        )

        config_help = Embed()
        config_help.add_field(
            name="`channel`", value="Sets the given channel as the meme dump."
        )
        config_help.add_field(
            name="`frequency`",
            value="Sets the frequency with which the bot sends the memes in the configured channel.\
          It should be a number between 1 and 10 (inclusive). The higher the frequency,\
          the faster the bot sends the memes. More details:\n\
          10: 1 min\n9: 5 min\n8: 10 min\n7: 30 min\n6: 1 hr\n\
            5: 3 hrs\n4: 6 hrs\n3: 12 hrs\n2: 1 day\n1: 2days",
        )
        config_help.add_field(
            name="`num_memes`",
            value="The number of memes you want the bot to send after every interval. \
          It should be a number between 1 and 10",
        )
        await interaction.followup.send(embeds=[help_message, config_help])
