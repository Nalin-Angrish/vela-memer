"""
Slash commands for the bot - The `meme` command
"""
from discord import Interaction
from discord.abc import Messageable
from ..lib.memes import Meme


class MemeCommand:
    """
    The `meme` command
    """

    name = "meme"
    description = "An endless supply of memes."

    @staticmethod
    async def main(interaction: Interaction, *, quantity: int = 1):
        """
        The `meme` command

        :param int quantity: The number of memes to send
        """
        if quantity < 1:
            await interaction.response.send_message(
                f"{quantity} memes? What exactly do you want me to do lol?"
            )
        elif quantity > 10:
            await interaction.response.send_message(
                f"{quantity} memes is just too much bruh."
            )
        elif isinstance(interaction.channel, Messageable):
            await interaction.response.send_message(
                f"Sending you {str(quantity)} memes now!"
            )
            memes = Meme.get_memes(quantity)
            for meme in memes:
                await meme.send_to(interaction.channel)
        else:
            await interaction.response.send_message(
                "I'm sorry but I cannot send the memes in this type of channel. Please ask me in DM or some public text channel."
            )
