from uuid import UUID
from model.dailyTodo import Todo
from repository.dailyTodo import TodoRepository
from schema import TodoInput, TodoType


class TodoService:
    """Service class for the todo entity. This class is responsible to manage all operations related with todos in.

    Returns:
        _type_: _description_
    """

    @staticmethod
    async def create(todo_data:TodoInput):
        """Create a new todo in the database.

        Args:
            todo_data (DailyTodoInput): _description_

        Returns:
            _type_: _description_
        """
        todo = Todo()
        todo.title = todo_data.title
        todo.description = todo_data.description
        todo.datetime_created = todo_data.datetime_created
        todo.datetime_expire = todo_data.datetime_expire
        todo.status_done = todo_data.status_done
        todo.user_id = todo_data.user_id
        todo.priority = todo_data.priority
        todo.favorite = todo_data.favorite
        todo.category = todo_data.category

        await TodoRepository.create(todo)
        return TodoType(id = todo.id,
                            title = todo.title,
                            description = todo.description,
                            datetime_expire= todo.datetime_expire,
                            datetime_created=todo.datetime_created,
                            status_done=todo.status_done,
                            user_id=todo.user_id,
                            priority=todo.priority,
                            favorite=todo.favorite,
                            category=todo.category)

    @staticmethod
    async def get_all():
        """Get all todo from the database.

        Returns:
            _type_: _description_
        """
        list_daily_todo = await TodoRepository.get_all()
        return [TodoType(id = todo.id,
                             title = todo.title,
                             description = todo.description,
                             datetime_expire = todo.datetime_expire,
                             datetime_created = todo.datetime_created,
                             status_done = todo.status_done,
                             user_id = todo.user_id,
                             priority = todo.priority,
                             favorite = todo.favorite,
                             category = todo.category) for todo in list_daily_todo]

    @staticmethod
    async def get_by_id(todo_id:UUID) -> TodoType:
        """Get an specific todo by its id.

        Args:
            todo_id (UUID): _description_

        Returns:
            _type_: _description_
        """
        todo = await TodoRepository.get_by_id(todo_id)
        return TodoType(id = todo.id,
                             title = todo.title,
                             description = todo.description,
                             datetime_expire = todo.datetime_expire,
                             datetime_created = todo.datetime_created,
                             status_done = todo.status_done,
                             user_id = todo.user_id,
                             priority = todo.priority,
                             favorite = todo.favorite,
                             category = todo.category)

    @staticmethod
    async def get_by_user(todo_user:UUID) -> list[TodoType]:
        """Get an specific todo by its id.

        Args:
            todo_user (int): _description_

        Returns:
            _type_: _description_
        """
        list_daily_todo = await TodoRepository.get_by_user(todo_user)
        return [TodoType(id = todo.id,
                             title = todo.title,
                             description = todo.description,
                             datetime_expire = todo.datetime_expire,
                             datetime_created = todo.datetime_created,
                             status_done = todo.status_done,
                             user_id = todo.user_id,
                             priority = todo.priority,
                             favorite = todo.favorite,
                             category = todo.category) for todo in list_daily_todo]

    @staticmethod
    async def delete(todo_id: UUID) -> int:
        """Delete a todo by its ID.

        Args:
            todo_id (int): _description_

        Returns:
            _type_: _description_
        """
        await TodoRepository.delete(todo_id)
        return todo_id

    @staticmethod
    async def update(todo_id:UUID, todo_data: TodoInput) -> str:
        """Update a todo on the database with new information.

        Args:
            todo_id (int): _description_
            todo_data (DailyTodoInput): _description_

        Returns:
            _type_: _description_
        """
        todo = Todo()
        todo.title = todo_data.title
        todo.description = todo_data.description
        todo.datetime_created = todo_data.datetime_created
        todo.datetime_expire = todo_data.datetime_expire
        todo.status_done = todo_data.status_done
        todo.user_id = todo_data.user_id
        todo.priority = todo_data.priority
        todo.favorite = todo_data.favorite
        todo.category = todo_data.category

        await TodoRepository.update(todo_id,todo)
        return f'Successfully updated data by id {todo_id}'
