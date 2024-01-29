from sqlalchemy.sql import select
from config import db
from model.dailyTodo import Todo


class TodoRepository:
    """This class represents the repository for test objects. It provides methods to perform CRUD operations on test.

    Returns:
        _type_: _description_
    """
    @staticmethod
    async def create(todo_data:Todo):
        """Method to insert a new test into the database.

        Args:
            todo_data (DailyTodo): _description_
        """
        async with db as session, session.begin():
            session.add(todo_data)

    @staticmethod
    async def get_by_id(todo_id:int) -> Todo:
        """Method to retrieve a test by its id.

        Args:
            todo_id (Test): _description_

        Returns:
            _type_: _description_
        """
        async with db as session:
            stmt = select(Todo).where(Todo.id == todo_id)
            result = await session.execute(stmt)
            todo = result.scalars().first()
            return todo

    @staticmethod
    async def get_by_user(todo_user:str) -> list[Todo]:
        """Method to retrieve a test by its id.

        Args:
            todo_user (Test): _description_

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
    async def update(todo_id: int, todo_data: Todo):
        """Method to update an existing todo entry in the DB.

        Args:
            todo_id (int): _description_
            todo_data (Test): _description_
        """
        async with db as session, session.begin():
            stmt = select(Todo).where(Todo.id == todo_id)
            result = await session.execute(stmt)
            todo = result.scalars().first()
            if todo:
                todo.title = todo_data.title
                todo.description = todo_data.description
                todo.date_created = todo_data.date_created
                todo.date_expire = todo_data.date_expire
                todo.status_done = todo_data.status_done
                todo.user_id = todo_data.user_id
                todo.priority = todo_data.priority
                todo.favorite = todo_data.favorite


    @staticmethod
    async def delete(todo_id: int):
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
