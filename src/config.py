"""Config file."""
import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

load_dotenv()

DB_CONFIG = os.getenv('DB_CONFIG')


class DatabaseSession:
    """A class that manages the connection to the database and provides a context for working with it."""

    def __init__(self, url: str = DB_CONFIG) -> None:
        """The URL of the database server as passed in by the user or read from the env.

        Args:
            url (str, optional): _description_. Default to DB_CONFIG.
        """
        self.engine = create_async_engine(url=url, echo=True)
        self.localSession = sessionmaker(bind=self.engine, class_=AsyncSession, expire_on_commit=False)

    async def create_all(self):
        """Create all tables in the database specified in the MetaData of SQLModel classes."""
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

    async def drop_all(self):
        """Drop all tables in the database specified in the MetaData of SQLModel classes."""
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.drop_all)

    async def close(self):
        """Close the engine and terminate the connection pool. This method should be called when you are done with."""
        await self.engine.dispose()

    async def __aenter__(self) -> AsyncSession:
        """A method that is called when entering the context manager block. It returns an instance of SessionLocal.

        Returns:
            AsyncSession: _description_
        """
        self.session = self.localSession()
        return self.session

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> AsyncSession:
        """Commit if there were no exceptions, rollback if there was an exception.

        Returns:
            AsyncSession: _description_
        """
        if exc_type is None:
            try:
                await self.session.commit()
            except Exception as commit_exc:
                await self.session.rollback()
                raise commit_exc
        else:
            await self.session.rollback()
        await self.session.close()

    async def commit_rollback(self):
        """Commit or Rollback the current Session based on whether an Exception has been raised or not."""
        try:
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise

    def get_new_session(self) -> AsyncSession:
        """Create and return a new asynchronous session.

        Returns:
            AsyncSession: A new session instance.
        """
        return self.localSession()





db = DatabaseSession()
