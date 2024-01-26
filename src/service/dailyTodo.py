from model.dailyTodo import Todo
from repository.dailyTodo import TodoRepository
from schema import TodoInput, TodoType


class TodoService:
    """Service class for the test entity. This class is responsible to manage all operations related with tests in.

    Returns:
        _type_: _description_
    """

    @staticmethod
    async def create(todo_data:TodoInput):
        """Create a new test in the database.

        Args:
            todo_data (DailyTodoInput): _description_

        Returns:
            _type_: _description_
        """
        todo = Todo()
        todo.title = todo_data.title
        todo.description = todo_data.description
        todo.date_created = todo_data.date_created
        todo.date_expire = todo_data.date_expire
        todo.status_done = todo_data.status_done
        todo.email_user = todo_data.email_user
        todo.priority = todo_data.priority
        todo.favorite = todo_data.favorite

        await TodoRepository.create(todo)
        return TodoType(id = todo.id,
                             title = todo.title,
                             description = todo.description,
                             date_expire= todo.date_expire,
                             date_created=todo.date_created,
                             status_done=todo.status_done,
                             email_user=todo.email_user,
                             priority=todo.priority,favorite=todo.favorite)

    @staticmethod
    async def get_all():
        """Get all tests from the database.

        Returns:
            _type_: _description_
        """
        list_daily_todo = await TodoRepository.get_all()
        return [TodoType(id = todo.id,
                             title = todo.title,
                             description = todo.description,
                             date_expire= todo.date_expire,
                             date_created=todo.date_created,
                             status_done=todo.status_done,
                             email_user=todo.email_user,
                             priority=todo.priority,
                             favorite=todo.favorite) for todo in list_daily_todo]

    @staticmethod
    async def get_by_id(todo_id:int) -> TodoType:
        """Get an specific test by its id.

        Args:
            todo_id (int): _description_

        Returns:
            _type_: _description_
        """
        todo = await TodoRepository.get_by_id(todo_id)
        return TodoType(id = todo.id,
                             title = todo.title,
                             description = todo.description,
                             date_expire= todo.date_expire,
                             date_created=todo.date_created,
                             status_done=todo.status_done,
                             email_user=todo.email_user,
                             priority=todo.priority,
                             favorite=todo.favorite)

    @staticmethod
    async def get_by_email(todo_email:str) -> list[TodoType]:
        """Get an specific test by its id.

        Args:
            todo_email (str): _description_

        Returns:
            _type_: _description_
        """
        list_daily_todo = await TodoRepository.get_by_email(todo_email)
        return [TodoType(id = todo.id,
                             title = todo.title,
                             description = todo.description,
                             date_expire= todo.date_expire,
                             date_created=todo.date_created,
                             status_done=todo.status_done,
                             email_user=todo.email_user,
                             priority=todo.priority,
                             favorite=todo.favorite) for todo in list_daily_todo]

    @staticmethod
    async def delete(todo_id: int) -> int:
        """Delete a test by its ID.

        Args:
            todo_id (int): _description_

        Returns:
            _type_: _description_
        """
        await TodoRepository.delete(todo_id)
        return todo_id

    @staticmethod
    async def update(todo_id:int, todo_data: TodoInput) -> str:
        """Update a test on the database with new information.

        Args:
            todo_id (int): _description_
            todo_data (DailyTodoInput): _description_

        Returns:
            _type_: _description_
        """
        todo = Todo()
        todo.title = todo_data.title
        todo.description = todo_data.description
        todo.date_created = todo_data.date_created
        todo.date_expire = todo_data.date_expire
        todo.status_done = todo_data.status_done
        todo.email_user = todo_data.email_user
        todo.priority = todo_data.priority
        todo.favorite = todo_data.favorite

        await TodoRepository.update(todo_id,todo)
        return f'Successfully updated data by id {todo_id}'
