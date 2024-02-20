from uuid import UUID

from fastapi import Depends
from sqlalchemy import update, text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select

from config import db
from model.categories import Categories


class CategoriesRepository:
    """Asynchronously creates a new record in the database for the given categories' data.

    Returns:
        None
    """

    @staticmethod
    async def create(categories_data: Categories):
        session = db.get_new_session()
        async with session as async_session:
            async_session.add(categories_data)
            await async_session.commit()

    @staticmethod
    async def update(user_id: UUID, categories_data: Categories):
        session = db.get_new_session()
        async with session as async_session:
            stmt = select(Categories).where(Categories.user_id == user_id)
            result = await async_session.execute(stmt)
            categories = result.scalars().first()
            if categories:
                categories.categories = categories_data.categories
                await session.commit()

    @staticmethod
    async def delete(user_id: UUID):
        session = db.get_new_session()
        async with session as async_session:
            stmt = select(Categories).where(Categories.user_id == user_id)
            result = await async_session.execute(stmt)
            categories = result.scalars().first()
            if categories:
                await session.delete(categories)
                await async_session.commit()

    @staticmethod
    async def get_all(user_id: UUID) -> Categories:
        session = db.get_new_session()
        async with session as async_session:
            query = select(Categories).where(Categories.user_id == user_id)
            result = await async_session.execute(query)
            categories = result.scalars().first()
            return categories

    @staticmethod
    async def add_category(user_id: UUID, category: str) -> UUID:
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
