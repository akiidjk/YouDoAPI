from sqlalchemy import update as sql_update, delete as sql_delete
from sqlalchemy.sql import select
from config import db
from model.dailyTodo import DailyTodo


class DailyTodoRepository:
    """This class represents the repository for test objects. It provides methods to perform CRUD operations on test.

    Returns:
        _type_: _description_
    """
    @staticmethod
    async def create(daily_todo_data:DailyTodo):
        """Method to insert a new test into the database.

        Args:
            daily_todo_data (DailyTodo): _description_
        """
        async with db as session:
            async with session.begin():
                session.add(daily_todo_data)
            await db.commit_rollback()

    @staticmethod
    async def get_by_id(daily_todo_id:int) -> DailyTodo:
        """Method to retrieve a test by its id.

        Args:
            daily_todo_id (Test): _description_

        Returns:
            _type_: _description_
        """
        async with db as session:
            stmt = select(DailyTodo).where(DailyTodo.id == daily_todo_id)
            result = await session.execute(stmt)
            daily_todo = result.scalars().first()
            return daily_todo

    @staticmethod
    async def get_all() -> list[DailyTodo]:
        """Method to retrieve all tests in the database.

        Returns:
            _type_: _description_
        """
        async with db as session:
            query = select(DailyTodo)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def update(daily_todo_id: int, daily_todo_data: DailyTodo):
        """Method to update an existing test entry in the DB.

        Args:
            daily_todo_id (int): _description_
            daily_todo_data (Test): _description_
        """
        async with db as session:
            stmt = select(DailyTodo).where(DailyTodo.id == daily_todo_id)
            result = await session.execute(stmt)

            daily_todo = result.scalars().first()

            session.add(daily_todo)

            daily_todo.title = daily_todo_data.title
            daily_todo.description = daily_todo_data.description
            daily_todo.date_created = daily_todo_data.date_created
            daily_todo.date_expire = daily_todo_data.date_expire
            daily_todo.status_done = daily_todo_data.status_done

            print(daily_todo.title)
            print(daily_todo.description)

            query = sql_update(DailyTodo).where(DailyTodo.id == daily_todo_id).values(
                **daily_todo.dict()).execution_options(synchronize_session="evaluate")


            await session.execute(query)
            await db.commit_rollback()


    @staticmethod
    async def delete(daily_todo_id: int):
        """Method to remove a specific test from the database.

        Args:
            daily_todo_id (int): _description_
        """
        async with db as session:
            query = sql_delete(DailyTodo).where(DailyTodo.id == daily_todo_id)
            await session.execute(query)
            await db.commit_rollback()
