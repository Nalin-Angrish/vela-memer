"""
Helper functions for interacting with the database
"""
from typing import Union
from discord import TextChannel
from sqlalchemy import Integer, String, Engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    """
    A Base class for database models
    """

    engine: Union[Engine, None] = None


class Guild(Base):
    """
    Helper class to interact with Guild data in the database
    """

    __tablename__ = "guilds"
    guild_id: Mapped[str] = mapped_column(String(), primary_key=True, nullable=False)
    meme_channel_id: Mapped[str] = mapped_column(String(), nullable=True)
    freqency: Mapped[int] = mapped_column(Integer(), nullable=True)
    meme_count: Mapped[int] = mapped_column(Integer(), nullable=True)

    @staticmethod
    def update(
        guild_id: int,
        meme_channel: Union[TextChannel, None] = None,
        frequency: Union[int, None] = None,
        num_memes: Union[int, None] = None,
    ) -> None:
        """
        Update Guild Configuration
        """
        with Session(Base.engine) as session:
            guild = session.get(Guild, str(guild_id))
            if guild is None:
                guild = Guild()
                guild.guild_id = str(guild_id)
            session.add(guild)
            if meme_channel is not None:
                guild.meme_channel_id = str(meme_channel.id)
            if frequency is not None:
                guild.freqency = frequency
            if num_memes is not None:
                guild.meme_count = num_memes
            session.commit()

    @staticmethod
    def new(guild_id: int, meme_channel: Union[TextChannel, None] = None) -> None:
        """
        Add new Guild to database
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
    def remove(guild_id: int) -> None:
        """
        Remove Guild from database
        """
        with Session(Base.engine) as session:
            guild = session.get(Guild, str(guild_id))
            if guild is not None:
                session.delete(guild)
            session.commit()
