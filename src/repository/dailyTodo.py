from uuid import UUID
from sqlalchemy.sql import select

from config import db
from model.dailyTodo import Todo


class TodoRepository:
    """This class represents the repository for todo objects. It provides methods to perform CRUD operations on todo.

    Returns:
        _type_: _description_
    """
    @staticmethod
    async def create(todo_data:Todo):
        """Method to insert a new todo into the database.

        Args:
            todo_data (DailyTodo): _description_
        """
        async with db as session, session.begin():
            session.add(todo_data)

    @staticmethod
    async def get_by_id(todo_id: UUID) -> Todo:
        """Method to retrieve a todo by its id.

        Args:
            todo_id (todo): _description_

        Returns:
            _type_: _description_
        """
        async with db as session:
            stmt = select(Todo).where(Todo.id == todo_id)
            result = await session.execute(stmt)
            todo = result.scalars().first()
            return todo

    @staticmethod
    async def get_by_user(todo_user:UUID) -> list[Todo]:
        """Method to retrieve a todo by its id.

        Args:
            todo_user (todo): _description_

        Returns:
            _type_: _description_
        """
        async with db as session:
            stmt = select(Todo).where(Todo.user_id == todo_user)
            result = await session.execute(stmt)
            return result.scalars().all()

    @staticmethod
    async def get_all() -> list[Todo]:
        """Method to retrieve all todo in the database.

        Returns:
            list[Todo]: _description_
        """
        async with db as session:
            query = select(Todo)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def update(todo_id: UUID, todo_data: Todo):
        """Method to update an existing todo entry in the DB.

        Args:
            todo_id (int): _description_
            todo_data (todo): _description_
        """
        async with db as session, session.begin():
            stmt = select(Todo).where(Todo.id == todo_id)
            result = await session.execute(stmt)
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


    @staticmethod
    async def delete(todo_id: UUID):
        """Method to remove a specific todo from the database.

        Args:
            todo_id (int): _description_
        """
        async with db as session, session.begin():
            stmt = select(Todo).where(Todo.id == todo_id)
            result = await session.execute(stmt)
            todo = result.scalars().first()
            if todo:
                await session.delete(todo)
