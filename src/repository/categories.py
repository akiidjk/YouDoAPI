from uuid import UUID

from sqlalchemy import text
from sqlalchemy.sql import select

from config import db
from model.categories import Categories


class CategoriesRepository:
    """Categories repository."""

    @staticmethod
    async def create(categories_data: Categories):
        """Asynchronously creates a new record in the database for the given categories' data.

        Args:
            categories_data (Categories): The category full model

        Returns:
            None
        """
        session = db.get_new_session()
        async with session as async_session:
            query = select(Categories).where(Categories.user_id == categories_data.user_id)
            result = await async_session.execute(query)
            category = result.scalars().first()
            if not category:
                async_session.add(categories_data)
                await async_session.commit()
            else:
                return category
    @staticmethod
    async def delete(user_id: UUID):
        """Asynchronously deletes the record in the database for the given categories' data

        Args:
            user_id (UUID): The user ID

        Returns:

        """
        session = db.get_new_session()
        async with session as async_session:
            stmt = select(Categories).where(Categories.user_id == user_id)
            result = await async_session.execute(stmt)
            categories = result.scalars().first()
            if categories:
                await session.delete(categories)
                await async_session.commit()

    @staticmethod
    async def get_by_user(user_id: UUID) -> Categories:
        """Asynchronously gets the record in the database for the given categories' data

        Args:
            user_id (UUID): The user ID

        Returns:

        """
        session = db.get_new_session()
        async with session as async_session:
            query = select(Categories).where(Categories.user_id == user_id)
            result = await async_session.execute(query)
            category = result.scalars().first()
            return category

    @staticmethod
    async def add_category(user_id: UUID, category: str) -> UUID:
        """Asynchronously adds a new category

        Args:
            user_id (UUID): The user ID
            category (str): The category

        Returns:

        """
        session = db.get_new_session()
        async with session as async_session:
            query = text("""
                UPDATE categories
                SET categories = CASE
                                    WHEN :new_element = ANY(categories) THEN categories
                                    ELSE array_append(categories, :new_element)
                                 END
                WHERE user_id = :user_id;
            """)
            await async_session.execute(query, {"new_element": category, "user_id": user_id})
            await async_session.commit()
            return user_id

    @staticmethod
    async def remove_category(user_id: UUID, category: str) -> UUID:
        """Asynchronously removes a category

        Args:
            user_id (UUID): The user ID
            category (str): The category

        Returns:

        """
        session = db.get_new_session()
        async with session as async_session:
            query = text("""
                UPDATE categories
                SET categories = array_remove(categories, :new_element)
                WHERE user_id = :user_id
            """)
            await async_session.execute(query, {"new_element": category, "user_id": user_id})
            await async_session.commit()
            return user_id
