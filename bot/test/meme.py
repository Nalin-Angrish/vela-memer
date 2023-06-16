"""
A Test to check if memes are being properly obtained by the library helper classes and functions.
"""
from ..lib import Meme


async def run_test() -> bool:
    """
    A Test to check if memes are being properly obtained by the library helper classes and functions

    :return: Test passed or not
    :rtype: bool
    """
    meme = (await Meme.get_memes(1))[0]
    return (meme.title != "") and (meme.image != "") and (meme.url != "")
