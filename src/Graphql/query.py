from datetime import datetime
from typing import List
from uuid import UUID
import strawberry

from schema import PomodoroType, TodoType, UserType, CategoriesType
from service.dailyTodo import TodoService
from service.pomodoro import PomodoroService
from service.user import UserService
from service.categories import CategoryService


@strawberry.type
class Query:
    """The GraphQL query type for the user application. This class represents a single point of entry into the api.

    Returns:
        _type_: _description_
    """

    # * Todo Query

    @strawberry.field
    async def get_by_user_todo(self, user_id: UUID) -> list[TodoType]:
        """Get one todo data by email.

        Args:
            user_id (int): The email of user

        Returns:
            DailyTodoType: _description_
        """
        return await TodoService.get_by_user(user_id)

    @strawberry.field
    async def get_by_id_todo(self, id: UUID) -> TodoType:
        """Get one todo data by id.

        Args:
            id (int): _description_

        Returns:
            DailyTodoType: _description_
        """
        return await TodoService.get_by_id(id)

    # * User Query

    @strawberry.field
    async def get_by_id_user(self, id: UUID) -> UserType:
        """Get one user data by id.

        Args:
            id (int): _description_

        Returns:
            DailyTodoType: _description_
        """
        return await UserService.get_by_id(id)

    @strawberry.field
    async def get_by_email_user(self, email: str) -> UserType:
        """Get one user data by id.

        Args:
            email (str): _description_

        Returns:
            DailyTodoType: _description_
        """
        return await UserService.get_by_email(email)

    # * Pomodoro Query

    @strawberry.field
    async def get_by_id_pomodoro(self, id: UUID) -> PomodoroType:
        """Get one user data by id.

        Args:
            id (int): _description_

        Returns:
            DailyTodoType: _description_
        """
        return await PomodoroService.get_by_id(id)

    @strawberry.field
    async def get_by_user_pomodoro(self, user_id: UUID) -> list[PomodoroType]:
        """Get one todo data by email.

        Args:
            user_id (int): The email of user

        Returns:
            DailyTodoType: _description_
        """
        return await PomodoroService.get_by_user(user_id)

    @strawberry.field
    async def get_by_month_pomodoro(self, user_id: UUID, date: datetime) -> list[PomodoroType]:
        """Get one todo data by email.

        Args:
            user_id (int): The email of user
            date (datetime): The date

        Returns:
            DailyTodoType: _description_
        """
        return await PomodoroService.get_by_month(user_id, date)

    # * Category query

    @strawberry.field
    async def get_all_categories(self, user_id: UUID) -> CategoriesType:
        """Get one category data by email.

        Args:
            user_id (int): The email of user

        Returns:
            DailyTodoType: _description_
        """
        return await CategoryService.get_all(user_id)
