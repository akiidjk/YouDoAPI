import strawberry

from schema import TodoType, UserType
from service.dailyTodo import TodoService
from service.user import UserService


@strawberry.type
class Query:
    """The GraphQL query type for the user application. This class represents a single point of entry into the api.

    Returns:
        _type_: _description_
    """
    @strawberry.field
    async def get_all_todo(self) -> list[TodoType]:
        """Get all todo data.

        Returns:
            list[userType]: _description_
        """
        return await TodoService.get_all()

    @strawberry.field
    async def get_by_user_todo(self,user_id:int) -> list[TodoType]:
        """Get one todo data by email.

        Args:
            user_id (int): The email of user

        Returns:
            DailyTodoType: _description_
        """
        return await TodoService.get_by_user(user_id)

    @strawberry.field
    async def get_by_id_todo(self,id:int) -> TodoType:
        """Get one todo data by id.

        Args:
            id (int): _description_

        Returns:
            DailyTodoType: _description_
        """
        return await TodoService.get_by_id(id)

    @strawberry.field
    async def get_all_user(self) -> list[UserType]:
        """Get all user data.

        Returns:
            list[userType]: _description_
        """
        return await UserService.get_all()

    @strawberry.field
    async def get_by_id_user(self,id:int) -> UserType:
        """Get one user data by id.

        Args:
            id (int): _description_

        Returns:
            DailyTodoType: _description_
        """
        return await UserService.get_by_id(id)

    @strawberry.field
    async def get_by_email_user(self,email:str) -> UserType:
        """Get one user data by id.

        Args:
            email (str): _description_

        Returns:
            DailyTodoType: _description_
        """
        return await UserService.get_by_email(email)
