"""
Helper functions for scheduling auto-memes
"""
import logging
from discord import Client
from discord.ext import tasks
from sqlalchemy import Engine
from ..lib import Guild, Meme

interval_data: list[int] = [
    60 * 60 * 24 * 2,  # 2 days
    60 * 60 * 24,  # 1 day
    60 * 60 * 12,  # 12 hrs
    60 * 60 * 6,  # 6 hrs
    60 * 60 * 3,  # 3 hrs
    60 * 60,  # 1 hr
    60 * 30,  # 30 mins
    60 * 10,  # 10 mins
    60 * 5,  # 5 mins
    60,  # 1 min
]
""" The interval (in seconds) corresponding to each frequency setting """


class MemeScheduler:
    """
    Helper class for scheduling auto-memes
    """

    _client: Client = None
    """ The Discord client using which all memes should be sent """
    _engine: Engine = None
    """ The Database engine to get the guild data from """
    _logger: logging.Logger = None

    @staticmethod
    def setup(client: Client, engine: Engine):
        """
        Setup meme sender using the given
        discord client and database engine

        :param Client client: The discord client to use to send memes
        :param Engine engine: The database engine to get the data from
        """
        MemeScheduler._client = client
        MemeScheduler._engine = engine
        MemeScheduler._logger = logging.getLogger("discord.client")

    @staticmethod
    async def send(frequency: int):
        """
        Send memes to all channels with configured frequency

        :param int frequency: The frequency of the channels to send the memes in
        """
        guilds: list[Guild] = Guild.get_guilds_with_frequency(frequency)
        if len(guilds) == 0:
            return
        memes: list[Meme] = Meme.get_memes(10)
        MemeScheduler._logger.info(f"Sending memes to {len(guilds)} channels with frequency {frequency}")

        for guild in guilds:
            channel = MemeScheduler._client.get_channel(int(guild.meme_channel_id))
            if channel is not None and channel.guild.me.guild_permissions.send_messages:
                for meme in memes[: guild.meme_count]:
                    await meme.send_to(channel)

    @staticmethod
    async def start():
        """
        Run the meme-sending schedule in a parallel thread
        """
        _loop_1.start()
        _loop_2.start()
        _loop_3.start()
        _loop_4.start()
        _loop_5.start()
        _loop_6.start()
        _loop_7.start()
        _loop_8.start()
        _loop_9.start()
        _loop_10.start()
        MemeScheduler._logger.info("Started meme scheduler")


# pylint: disable=pointless-string-statement
"""
Scheduling event loops.
This is not a very good way of writing all these 10 loops
individually but i could not figure out a shorter way to
do this, and until i find, i think i'll make do with this...
"""


@tasks.loop(seconds=interval_data[0])
async def _loop_1():
    await MemeScheduler.send(1)


@tasks.loop(seconds=interval_data[1])
async def _loop_2():
    await MemeScheduler.send(2)


@tasks.loop(seconds=interval_data[2])
async def _loop_3():
    await MemeScheduler.send(3)


@tasks.loop(seconds=interval_data[3])
async def _loop_4():
    await MemeScheduler.send(4)


@tasks.loop(seconds=interval_data[4])
async def _loop_5():
    await MemeScheduler.send(5)


@tasks.loop(seconds=interval_data[5])
async def _loop_6():
    await MemeScheduler.send(6)


@tasks.loop(seconds=interval_data[6])
async def _loop_7():
    await MemeScheduler.send(7)


@tasks.loop(seconds=interval_data[7])
async def _loop_8():
    await MemeScheduler.send(8)


@tasks.loop(seconds=interval_data[8])
async def _loop_9():
    await MemeScheduler.send(9)


@tasks.loop(seconds=interval_data[9])
async def _loop_10():
    await MemeScheduler.send(10)
