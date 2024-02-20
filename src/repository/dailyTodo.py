from uuid import UUID

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select

from config import db
from model.dailyTodo import Todo


class TodoRepository:
    """This class represents the repository for todo objects. It provides methods to perform CRUD operations on todo.

    Returns:
        _type_: _description_
    """

    @staticmethod
    async def create(todo_data: Todo):
        """Method to insert a new todo into the database.

        Args:
            todo_data (DailyTodo): _description_
        """
        session = db.get_new_session()
        async with session as async_session:
            async_session.add(todo_data)
            await async_session.commit()

    @staticmethod
    async def get_by_id(todo_id: UUID) -> Todo:
        """Method to retrieve a todo by its id.

        Args:
            todo_id (todo): _description_

        Returns:
            _type_: _description_
        """
        session = db.get_new_session()
        async with session as async_session:
            stmt = select(Todo).where(Todo.id == todo_id)
            result = await async_session.execute(stmt)
            todo = result.scalars().first()
            return todo

    @staticmethod
    async def get_by_user(todo_user: UUID) -> list[Todo]:
        """Method to retrieve a todo by its id.

        Args:
            session (DBSession): the db session
            todo_user (todo): _description_

        Returns:
            _type_: _description_
        # """
        session = db.get_new_session()
        async with session as async_session:
            stmt = select(Todo).where(Todo.user_id == todo_user)
            result = await async_session.execute(stmt)
            return result.scalars().all()

    @staticmethod
    async def update(todo_id: UUID, todo_data: Todo):
        """Method to update an existing todo entry in the DB.

        Args:
            todo_id (int): _description_
            todo_data (todo): _description_
        """
        session = db.get_new_session()
        async with session as async_session:
            stmt = select(Todo).where(Todo.id == todo_id)
            result = await async_session.execute(stmt)
            todo = result.scalars().first()
            if todo:
                todo.title = todo_data.title
                todo.description = todo_data.description
                todo.datetime_created = todo_data.datetime_created
                todo.datetime_expire = todo_data.datetime_expire
                todo.status_done = todo_data.status_done
                todo.user_id = todo_data.user_id
                todo.priority = todo_data.priority
                todo.favorite = todo_data.favorite
                todo.category = todo_data.category
                await async_session.commit()


    @staticmethod
    async def delete(todo_id: UUID):
        """Method to remove a specific todo from the database.

        Args:
            todo_id (int): _description_
        """
        session = db.get_new_session()
        async with session as async_session:
            stmt = select(Todo).where(Todo.id == todo_id)
            result = await async_session.execute(stmt)
            todo = result.scalars().first()
            if todo:
                await async_session.delete(todo)
                await async_session.commit()
