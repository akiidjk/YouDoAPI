import strawberry

from schema import TodoType
from service.dailyTodo import TodoService


@strawberry.type
class Query:
    """The GraphQL query type for the test application. This class represents a single point of entry into the api.

    Returns:
        _type_: _description_
    """
    @strawberry.field
    async def get_all_todo(self) -> list[TodoType]:
        """Get all test data.

        Returns:
            list[TestType]: _description_
        """
        return await TodoService.get_all()

    @strawberry.field
    async def get_by_email_todo(self,email_user:str) -> list[TodoType]:
        """Get one test data by email.

        Args:
            email_user (int): The email of user

        Returns:
            DailyTodoType: _description_
        """
        return await TodoService.get_by_email(email_user)

    @strawberry.field
    async def get_by_id_todo(self,id:int) -> TodoType:
        """Get one test data by id.

        Args:
            id (int): _description_

        Returns:
            DailyTodoType: _description_
        """
        return await TodoService.get_by_id(id)
