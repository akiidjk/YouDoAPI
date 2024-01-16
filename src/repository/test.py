from sqlalchemy import update as sql_update, delete as sql_delete
from sqlalchemy.sql import select
from config import db
from model.test import Test


class TestRepository:
    """This class represents the repository for test objects. It provides methods to perform CRUD operations on test.

    Returns:
        _type_: _description_
    """
    @staticmethod
    async def create(test_data:Test):
        """Method to insert a new test into the database.

        Args:
            test_data (Test): _description_
        """
        async with db as session:
            async with session.begin():
                session.add(test_data)
            await db.commit_rollback()

    @staticmethod
    async def get_by_id(test_id:Test):
        """Method to retrieve a test by its id.

        Args:
            test_id (Test): _description_

        Returns:
            _type_: _description_
        """
        async with db as session:
            stmt  = select(Test).where(Test.id == test_id)
            result = await session.execute(stmt)
            tests = result.scalars().first()
            return tests

    @staticmethod
    async def get_all():
        """Method to retrieve all tests in the database.

        Returns:
            _type_: _description_
        """
        async with db as session:
            query = select(Test)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def update(test_id: int, test_data: Test):
        """Method to update an existing test entry in the DB.

        Args:
            test_id (int): _description_
            test_data (Test): _description_
        """
        async with db as session:
            stmt = select(Test).where(Test.id == test_id)
            result = await session.execute(stmt)

            test = result.scalars().first()
            test.name = test_data.name
            test.description = test_data.description

            query = sql_update(test).where(test.id == test_id).values(
                **test.dict()).execution_options(synchronize_session="fetch")

            await session.execute(query)
            await db.commit_rollback()

    @staticmethod
    async def delete(test_id: int):
        """Method to remove a specific test from the database.

        Args:
            test_id (int): _description_
        """
        async with db as session:
            query = sql_delete(Test).where(Test.id == test_id)
            await session.execute(query)
            await db.commit_rollback()

