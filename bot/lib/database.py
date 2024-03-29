"""
Helper functions for interacting with the database
"""
from typing import Union
from discord import TextChannel
from sqlalchemy import Integer, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncAttrs, async_sessionmaker


class Base(AsyncAttrs, DeclarativeBase):
    """
    A Base class for database models
    """

    engine: Union[AsyncEngine, None] = None
    """ The database engine to use """


class Guild(Base):
    """
    Helper class to interact with Guild data in the database
    """

    __tablename__ = "guilds"
    guild_id: Mapped[str] = mapped_column(String(), primary_key=True, nullable=False)
    """ The ID of the guild """
    meme_channel_id: Mapped[str] = mapped_column(String(), nullable=True)
    """ The ID of the channel to which memes are to be sent """
    frequency: Mapped[int] = mapped_column(Integer(), nullable=True)
    """ The frequency with which memes are to be sent """
    meme_count: Mapped[int] = mapped_column(Integer(), nullable=True)
    """ The number of memes to be sent in one go """

    @staticmethod
    async def update(
        guild_id: int,
        meme_channel: Union[TextChannel, None] = None,
        frequency: Union[int, None] = None,
        num_memes: Union[int, None] = None,
    ):
        """
        Update Guild Configuration

        :param int guild_id: The ID of the guild
        :param Optional[TextChannel] meme_channel: The ID of the channel to which memes are to be sent
        :param Optional[int] frequency: The frequency with which memes are to be sent
        :param Optional[int] num_memes: The number of memes to be sent in one go
        """
        async with async_sessionmaker(Base.engine)() as session:
            guild = await session.get(Guild, str(guild_id))
            if guild is None:
                guild = Guild()
                guild.guild_id = str(guild_id)
            session.add(guild)
            if meme_channel is not None:
                guild.meme_channel_id = str(meme_channel.id)
            if frequency is not None and frequency <= 10 and frequency > 0:
                guild.frequency = frequency
            if num_memes is not None and num_memes <= 10 and num_memes > 0:
                guild.meme_count = num_memes
            await session.commit()

    @staticmethod
    async def new(guild_id: int, meme_channel: Union[TextChannel, None] = None):
        """
        Add new Guild to database

        :param int guild_id: The ID of the guild
        :param Optional[TextChannel] meme_channel: The ID of the channel to which memes are to be sent
        """
        async with async_sessionmaker(Base.engine)() as session:
            guild = Guild()
            guild.guild_id = str(guild_id)
            session.add(guild)
            if meme_channel is not None:
                guild.meme_channel_id = str(meme_channel.id)
            guild.frequency = 5
            guild.meme_count = 5
            await session.commit()

    @staticmethod
    async def remove(guild_id: int):
        """
        Remove Guild from database

        :param int guild_id: The ID of the guild
        """
        async with async_sessionmaker(Base.engine)() as session:
            guild = await session.get(Guild, str(guild_id))
            if guild is not None:
                await session.delete(guild)
            await session.commit()

    @staticmethod
    async def get_guilds_with_frequency(frequency: int):
        """
        Get guilds with the configured frequency

        :param Optional[int] frequency: The frequency of the guilds we need
        :return: Guilds with the given frequency
        :rtype: list[Guild]
        """
        async with async_sessionmaker(Base.engine)() as session:
            stmt = select(Guild).where(Guild.frequency == frequency)
            result = await session.execute(stmt)
            guilds: list[Guild] = result.scalars().all()
        return guilds
