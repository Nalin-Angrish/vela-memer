"""
Helper functions for getting meme data and sending them to specified channels
"""
from requests import get
from discord import Embed
from discord.abc import Messageable


class Meme:
    """
    A Class to manage meme data
    """

    title: str = ""
    """ Title/Caption of the meme """
    image: str = ""
    """ Image URL of the meme """
    url: str = ""
    """ Reddit URL of the meme """

    def __init__(self, title, image, url) -> None:
        """
        An initializer to set up properties of the meme

        :return: None
        """
        self.title = title
        self.image = image
        self.url = url

    @staticmethod
    def get_memes(amount: int = 1) -> list["Meme"]:
        """
        Helper function to obtain meme data from the meme api

        :param int amount: Number of memes to get the data of
        :return: List of memes
        :rtype: list[Meme]
        """
        data = get(f"https://meme-api.com/gimme/{amount}", timeout=10).json()
        if data.get("memes") is None:
            if data.get("code") == 403:  # Subreddit/Post is locked/hidden
                return Meme.get_memes(amount)  # Send some other memes
            else:
                data["memes"] = [
                    {
                        "title": "Some unexpected error occured!",
                        "postLink": "https://youtu.be/dQw4w9WgXcQ",
                        "url": "https://cataas.com/cat/says/Sorry%20friend%20:(",
                    }
                ]

        memes = []
        for meme in data["memes"]:
            memes.append(Meme(meme["title"], meme["url"], meme["postLink"]))
        return memes

    async def send_to(self, channel: Messageable) -> None:
        """
        Helper function to send the meme instance to the specified discord channel

        :param Messageable channel: The channel in which the meme is to be sent.
        """
        meme = Embed(title=self.title, url=self.url)
        meme.set_image(url=self.image)
        await channel.send(embed=meme)
