import strawberry

from schema import DailyTodoInput, DailyTodoType
from service.dailyTodo import DailyTodoService

@strawberry.type
class Mutation:
    """The mutations available in the GraphQL API for testing purposes.

    Returns:
        _type_: _description_
    """

    @strawberry.mutation
    async def create_daily_todo(self,daily_todo_data:DailyTodoInput) -> DailyTodoType:
        """Create a new test case with given data.

        Args:
            daily_todo_data (DailyTodoInput): _description_

        Returns:
            TestType: _description_
        """
        return await DailyTodoService.create(daily_todo_data=daily_todo_data)

    @strawberry.mutation
    async def delete_daily_todo(self,id:int) -> int:
        """Delete an existing test case by its id.

        Args:
            id (int): _description_

        Returns:
            str: _description_
        """
        return await DailyTodoService.delete(id)

    @strawberry.mutation
    async def update_daily_todo(self,id:int,daily_todo_data:DailyTodoInput) -> str:
        """Update an existing test case's information.

        Args:
            id (int): _description_
            daily_todo_data (TestInput): _description_

        Returns:
            str: _description_
        """
        return await DailyTodoService.update(id,daily_todo_data)

