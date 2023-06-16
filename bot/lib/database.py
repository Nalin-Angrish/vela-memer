"""
Helper functions for interacting with the database
"""
from typing import Union
from discord import TextChannel
from sqlalchemy import Integer, String, Engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    """
    A Base class for database models
    """

    engine: Union[Engine, None] = None
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
    freqency: Mapped[int] = mapped_column(Integer(), nullable=True)
    """ The frequency with which memes are to be sent """
    meme_count: Mapped[int] = mapped_column(Integer(), nullable=True)
    """ The number of memes to be sent in one go """

    @staticmethod
    def update(
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
        with Session(Base.engine) as session:
            guild = session.get(Guild, str(guild_id))
            if guild is None:
                guild = Guild()
                guild.guild_id = str(guild_id)
            session.add(guild)
            if meme_channel is not None:
                guild.meme_channel_id = str(meme_channel.id)
            if frequency is not None and frequency <= 10 and frequency > 0:
                guild.freqency = frequency
            if num_memes is not None and num_memes <= 10 and num_memes > 0:
                guild.meme_count = num_memes
            session.commit()

    @staticmethod
    def new(guild_id: int, meme_channel: Union[TextChannel, None] = None):
        """
        Add new Guild to database

        :param int guild_id: The ID of the guild
        :param Optional[TextChannel] meme_channel: The ID of the channel to which memes are to be sent
        """
        with Session(Base.engine) as session:
            guild = Guild()
            guild.guild_id = str(guild_id)
            session.add(guild)
            if meme_channel is not None:
                guild.meme_channel_id = str(meme_channel.id)
            guild.freqency = 5
            guild.meme_count = 5
            session.commit()

    @staticmethod
    def remove(guild_id: int):
        """
        Remove Guild from database

        :param int guild_id: The ID of the guild
        """
        with Session(Base.engine) as session:
            guild = session.get(Guild, str(guild_id))
            if guild is not None:
                session.delete(guild)
            session.commit()

    @staticmethod
    def get_guilds_with_frequency(frequency: int) -> list["Guild"]:
        """
        Get guilds with the configured frequency

        :param Optional[int] frequency: The frequency of the guilds we need
        :return: Guilds with the given frequency
        :rtype: list[Guild]
        """
        with Session(Base.engine) as session:
            stmt = select(Guild).where(Guild.freqency == frequency)
            guilds: list[Guild] = session.scalars(stmt).all()
        return guilds
