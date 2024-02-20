from uuid import UUID
import strawberry

from schema import PomodoroInput, PomodoroType, TodoInput, TodoType, UserInput, UserType, CategoriesType, CategoriesInput
from service.dailyTodo import TodoService
from service.pomodoro import PomodoroService
from service.user import UserService
from service.categories import CategoryService


@strawberry.type
class Mutation:
    """The mutations available in the GraphQL API for usering purposes.

    Returns:
        _type_: _description_
    """

    # * Todo mutation

    @strawberry.mutation
    async def create_todo(self, todo_data: TodoInput) -> TodoType:
        """Create a new todo case with given data.

        Args:
            todo_data (DailyTodoInput): _description_

        Returns:
            userType: _description_
        """
        return await TodoService.create(todo_data=todo_data)

    @strawberry.mutation
    async def delete_todo(self, id_todo: UUID) -> UUID:
        """Delete an existing todo case by its id.

        Args:
            id_todo (UUID): _description_

        Returns:
            str: _description_
        """
        return await TodoService.delete(id_todo)

    @strawberry.mutation
    async def update_todo(self, id_todo: UUID, todo_data: TodoInput) -> str:
        """Update an existing todo case's information.

        Args:
            id_todo (UUID): _description_
            todo_data (userInput): _description_

        Returns:
            str: _description_
        """
        return await TodoService.update(id_todo, todo_data)

    # * User mutation

    @strawberry.mutation
    async def create_user(self, user_data: UserInput) -> UserType:
        """Create a new user case with given data.

        Args:
            user_data (DailyTodoInput): _description_

        Returns:
            userType: _description_
        """
        return await UserService.create(user_data=user_data)

    @strawberry.mutation
    async def delete_user(self, user_id: UUID) -> UUID:
        """Delete an existing user case by its id.

        Args:
            user_id (int): _description_

        Returns:
            str: _description_
        """
        return await UserService.delete(user_id)

    @strawberry.mutation
    async def update_user(self, user_id: UUID, user_data: UserInput) -> str:
        """Update an existing user case's information.

        Args:
            user_id (int): _description_
            user_data (userInput): _description_

        Returns:
            str: _description_
        """
        return await UserService.update(user_id, user_data)

    # * Pomodoro mutation

    @strawberry.mutation
    async def create_pomodoro(self, pomodoro_data: PomodoroInput) -> PomodoroType:
        """Create a new user case with given data.

        Args:
            pomodoro_data (PomodoroInput): _description_

        Returns:
            userType: _description_
        """
        return await PomodoroService.create(pomodoro_data=pomodoro_data)

    @strawberry.mutation
    async def delete_pomodoro(self, pomodoro_id: UUID) -> UUID:
        """Delete an existing user case by its id.

        Args:
            pomodoro_id (int): _description_

        Returns:
            str: _description_
        """
        return await PomodoroService.delete(pomodoro_id)

    @strawberry.mutation
    async def update_pomodoro(self, pomodoro_id: UUID, pomodoro_data: PomodoroInput) -> str:
        """Update an existing user case's information.

        Args:
            pomodoro_id (int): _description_
            pomodoro_data (PomodoroInput): _description_

        Returns:
            str: _description_
        """
        return await PomodoroService.update(pomodoro_id, pomodoro_data=pomodoro_data)

    @strawberry.mutation
    async def create_category(self, category_data: CategoriesInput) -> CategoriesType:
        """Create a new user case with given data.

        Args:
            category_data (CategoriesInput): _description_

        Returns:
            userType: _description_
        """
        return await CategoryService.create(category_data=category_data)

    @strawberry.mutation
    async def delete_category(self, id_category: UUID) -> UUID:
        """Delete an existing user case by its id.

        Args:
            id_category (int): _description_

        Returns:
            str: _description_
        """
        return await CategoryService.delete(id_category)

    @strawberry.mutation
    async def add_category_categories(self, user_id: UUID, category: str) -> UUID:
        """Add a categories in the array of categories of the user.
        Args:
            user_id:
            category:

        Returns:

        """
        return await CategoryService.add_category(user_id, category)

    @strawberry.mutation
    async def remove_category_categories(self, user_id: UUID, category: str) -> UUID:
        """Add a categories in the array of categories of the user.
        Args:
            user_id:
            category:

        Returns:

        """
        return await CategoryService.remove_category(user_id, category)
