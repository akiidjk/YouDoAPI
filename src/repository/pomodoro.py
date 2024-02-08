from datetime import datetime
from uuid import UUID

from sqlalchemy import func
from sqlalchemy.sql import select

from config import db
from model.pomodoro import Pomodoro

class PomodoroRepository:
    """This class represents the repository for pomodoro objects. It provides methods to perform CRUD operations on test.

    Returns:
        _type_: _description_
    """
    @staticmethod
    async def create(pomodoro_data:Pomodoro):
        """Method to insert a new pomodoro into the database.

        Args:
            pomodoro_data (Pomodoro): _description_
        """
        async with db as session, session.begin():
            session.add(pomodoro_data)

    @staticmethod
    async def update(pomodoro_id: UUID, pomodoro_data: Pomodoro):
        """Method to update an existing pomodoro entry in the DB.

        Args:
            pomodoro_id (int): _description_
            pomodoro_data (pomodoro): _description_
        """
        async with db as session, session.begin():
            stmt = select(Pomodoro).where(Pomodoro.id == pomodoro_id)
            result = await session.execute(stmt)
            pomodoro = result.scalars().first()
            if pomodoro:
                pomodoro.date = pomodoro_data.date
                pomodoro.duration = pomodoro_data.duration
                pomodoro.user_id = pomodoro_data.user_id

    @staticmethod
    async def delete(pomodoro_id: UUID):
        """Method to remove a specific pomodoro from the database.

        Args:
            pomodoro_id (UUID): _description_
        """
        async with db as session, session.begin():
            stmt = select(Pomodoro).where(Pomodoro.id == pomodoro_id)
            result = await session.execute(stmt)
            pomodoro = result.scalars().first()
            if pomodoro:
                await session.delete(pomodoro)

    @staticmethod
    async def get_all() -> list[Pomodoro]:
        """Method to retrieve all pomodoro in the database.

        Returns:
            list[Pomodoro]: _description_
        """
        async with db as session:
            query = select(Pomodoro)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def get_by_id(pomodoro_id: UUID) -> Pomodoro:
        """Method to retrieve a pomodoro by its id.

        Args:
            pomodoro_id (pomodoro): _description_

        Returns:
            _type_: _description_
        """
        async with db as session:
            stmt = select(Pomodoro).where(Pomodoro.id == pomodoro_id)
            result = await session.execute(stmt)
            pomodoro = result.scalars().first()
            return pomodoro

    @staticmethod
    async def get_by_user(pomodoro_user:UUID) -> list[Pomodoro]:
        """Method to retrieve a pomodoro by its id.

        Args:
            pomodoro_user (pomodoro): _description_

        Returns:
            _type_: _description_
        """
        async with db as session:
            stmt = select(Pomodoro).where(Pomodoro.user_id == pomodoro_user)
            result = await session.execute(stmt)
            return result.scalars().all()

    @staticmethod
    async def get_by_month(pomodoro_user:UUID,pomodoro_date:datetime) -> list[Pomodoro]:
        """Method to retrieve a pomodoro by its month.

        Args:
            pomodoro_user (UUID): _description_
            pomodoro_date (datetime): _description_
        """
        async with db as session:
            stmt = select(Pomodoro).where(
                Pomodoro.user_id == pomodoro_user,func.extract('month', Pomodoro.date_time) == pomodoro_date.month)
            result = await session.execute(stmt)
            return result.scalars().all()
