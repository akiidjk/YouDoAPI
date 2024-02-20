from uuid import UUID
from sqlalchemy.sql import select

from config import db
from model.user import User


class UserRepository:
    """Repository class for the user entity."""

    @staticmethod
    async def create(user_data: User) -> int:
        """Method to insert a new user into the database.

        Args:
            user_data (User): The user data to be inserted.
        """
        session = db.get_new_session()
        async with session as async_session:
            stmt = select(User).where(User.email == user_data.email)
            existing_user = await async_session.execute(stmt)
            existing_user_data = existing_user.scalars().first()
            if not existing_user_data:
                async_session.add(user_data)
                async_session.commit()
                return user_data.id
            return existing_user_data.id

    @staticmethod
    async def get_by_id(user_id: UUID) -> User:
        """Method to retrieve a user by its id.

        Args:
            user_id (int): The id of the user to retrieve.

        Returns:
            User: _description_
        """
        session = db.get_new_session()
        async with session as async_session:
            stmt = select(User).where(User.id == user_id)
            result = await async_session.execute(stmt)
            user = result.scalars().first()
            return user

    @staticmethod
    async def get_by_email(user_email: str) -> User:
        """Method to retrieve a user by its id.

        Args:
            user_email (str): The email of the user to retrieve.

        Returns:
            User: _description_
        """
        session = db.get_new_session()
        async with session as async_session:
            stmt = select(User).where(User.email == user_email)
            result = await async_session.execute(stmt)
            user = result.scalars().first()
            return user

    @staticmethod
    async def update(user_id: UUID, user_data: User):
        """Method to update an existing user entry in the DB.

        Args:
            user_id (int): The user id
            user_data (User): The user data
        """
        session = db.get_new_session()
        async with session as async_session:
            stmt = select(User).where(User.id == user_id)
            result = await async_session.execute(stmt)
            user = result.scalars().first()
            if user:
                user.email = user_data.email
                await async_session.commit()

    @staticmethod
    async def delete(user_id: UUID):
        """Method to remove a specific user from the database.

        Args:
            user_id (int): _description_
        """
        session = db.get_new_session()
        async with session as async_session:
            stmt = select(User).where(User.id == user_id)
            result = await async_session.execute(stmt)
            user = result.scalars().first()
            if user:
                await async_session.delete(user)
                await async_session.commit()
