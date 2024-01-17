from model.dailyTodo import DailyTodo
from repository.dailyTodo import DailyTodoRepository
from schema import DailyTodoInput, DailyTodoType


class DailyTodoService:
    """Service class for the test entity. This class is responsible to manage all operations related with tests in.

    Returns:
        _type_: _description_
    """

    @staticmethod
    async def create(daily_todo_data:DailyTodoInput):
        """Create a new test in the database.

        Args:
            daily_todo_data (DailyTodoInput): _description_

        Returns:
            _type_: _description_
        """
        daily_todo = DailyTodo()
        daily_todo.title = daily_todo_data.title
        daily_todo.description = daily_todo_data.description
        daily_todo.date_created = daily_todo_data.date_created
        daily_todo.date_expire = daily_todo_data.date_expire
        daily_todo.status_done = daily_todo_data.status_done
        daily_todo.email_user = daily_todo_data.email_user

        await DailyTodoRepository.create(daily_todo)

        return DailyTodoType(id = daily_todo.id,
                             title = daily_todo.title,
                             description = daily_todo.description,
                             date_expire= daily_todo.date_expire,
                             date_created=daily_todo.date_created,
                             status_done=daily_todo.status_done,
                             email_user=daily_todo.email_user)

    @staticmethod
    async def get_all():
        """Get all tests from the database.

        Returns:
            _type_: _description_
        """
        list_daily_todo = await DailyTodoRepository.get_all()
        return [DailyTodoType(id = daily_todo.id,
                             title = daily_todo.title,
                             description = daily_todo.description,
                             date_expire= daily_todo.date_expire,
                             date_created=daily_todo.date_created,
                             status_done=daily_todo.status_done,
                             email_user=daily_todo.email_user) for daily_todo in list_daily_todo]

    @staticmethod
    async def get_by_id(daily_todo_id:int) -> DailyTodoType:
        """Get an specific test by its id.

        Args:
            daily_todo_id (int): _description_

        Returns:
            _type_: _description_
        """
        daily_todo = await DailyTodoRepository.get_by_id(daily_todo_id)
        return DailyTodoType(id = daily_todo.id,
                             title = daily_todo.title,
                             description = daily_todo.description,
                             date_expire= daily_todo.date_expire,
                             date_created=daily_todo.date_created,
                             status_done=daily_todo.status_done,
                             email_user=daily_todo.email_user)

    @staticmethod
    async def get_by_email(daily_todo_email:str) -> list[DailyTodoType]:
        """Get an specific test by its id.

        Args:
            daily_todo_email (str): _description_

        Returns:
            _type_: _description_
        """
        list_daily_todo = await DailyTodoRepository.get_by_email(daily_todo_email)
        return [DailyTodoType(id = daily_todo.id,
                             title = daily_todo.title,
                             description = daily_todo.description,
                             date_expire= daily_todo.date_expire,
                             date_created=daily_todo.date_created,
                             status_done=daily_todo.status_done,
                             email_user=daily_todo.email_user) for daily_todo in list_daily_todo]

    @staticmethod
    async def delete(daily_todo_id: int) -> int:
        """Delete a test by its ID.

        Args:
            daily_todo_id (int): _description_

        Returns:
            _type_: _description_
        """
        await DailyTodoRepository.delete(daily_todo_id)
        return daily_todo_id

    @staticmethod
    async def update(daily_todo_id:int, daily_todo_data: DailyTodoInput) -> str:
        """Update a test on the database with new information.

        Args:
            daily_todo_id (int): _description_
            daily_todo_data (DailyTodoInput): _description_

        Returns:
            _type_: _description_
        """
        daily_todo = DailyTodo()
        daily_todo.title = daily_todo_data.title
        daily_todo.description = daily_todo_data.description
        daily_todo.date_created = daily_todo_data.date_created
        daily_todo.date_expire = daily_todo_data.date_expire
        daily_todo.status_done = daily_todo_data.status_done
        daily_todo.email_user = daily_todo_data.email_user
        await DailyTodoRepository.update(daily_todo_id,daily_todo)
        return f'Successfully updated data by id {daily_todo_id}'
