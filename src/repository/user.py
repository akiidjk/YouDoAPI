from sqlalchemy.sql import select
from config import db
from model.user import User


class UserRepository:
    """Repository class for the user entity."""

    @staticmethod
    async def create(user_data:User) -> int:
        """Method to insert a new user into the database.

        Args:
            user_data (User): The user data to be inserted.
        """
        async with db as session, session.begin():
            stmt = select(User).where(User.email == user_data.email)
            existing_user = await session.execute(stmt)
            existing_user_data = existing_user.scalars().first()
            if not existing_user_data:
                session.add(user_data)
                return user_data.id
            print("User already exists!")
            return existing_user_data.id

    @staticmethod
    async def get_by_id(user_id:int) -> User:
        """Method to retrieve a user by its id.

        Args:
            user_id (int): The id of the user to retrieve.

        Returns:
            User: _description_
        """
        async with db as session:
            stmt = select(User).where(User.id == user_id)
            result = await session.execute(stmt)
            user = result.scalars().first()
            return user

    @staticmethod
    async def get_by_email(user_email:str) -> User:
        """Method to retrieve a user by its id.

        Args:
            user_email (str): The email of the user to retrieve.

        Returns:
            User: _description_
        """
        async with db as session:
            stmt = select(User).where(User.email == user_email)
            result = await session.execute(stmt)
            user = result.scalars().first()
            return user

    @staticmethod
    async def get_all() -> list[User]:
        """Method to retrieve all user in the database.

        Returns:
            list[User]: _description_
        """
        async with db as session:
            query = select(User)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def update(user_id: int, user_data: User):
        """Method to update an existing user entry in the DB.

        Args:
            user_id (int): The user id
            user_data (User): The user data
        """
        async with db as session, session.begin():
            stmt = select(User).where(User.id == user_id)
            result = await session.execute(stmt)
            user = result.scalars().first()
            if user:
                user.email = user_data.email

    @staticmethod
    async def delete(user_id: int):
        """Method to remove a specific user from the database.

        Args:
            user_id (int): _description_
        """
        async with db as session, session.begin():
            stmt = select(User).where(User.id == user_id)
            result = await session.execute(stmt)
            user = result.scalars().first()
            if user:
                await session.delete(user)
