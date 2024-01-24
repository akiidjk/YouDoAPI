import strawberry

from schema import TodoInput, TodoType
from service.dailyTodo import TodoService

@strawberry.type
class Mutation:
    """The mutations available in the GraphQL API for testing purposes.

    Returns:
        _type_: _description_
    """

    @strawberry.mutation
    async def create_todo(self,todo_data:TodoInput) -> TodoType:
        """Create a new test case with given data.

        Args:
            todo_data (DailyTodoInput): _description_

        Returns:
            TestType: _description_
        """
        return await TodoService.create(todo_data=todo_data)

    @strawberry.mutation
    async def delete_todo(self,id:int) -> int:
        """Delete an existing test case by its id.

        Args:
            id (int): _description_

        Returns:
            str: _description_
        """
        return await TodoService.delete(id)

    @strawberry.mutation
    async def update_todo(self,id:int,todo_data:TodoInput) -> str:
        """Update an existing test case's information.

        Args:
            id (int): _description_
            todo_data (TestInput): _description_

        Returns:
            str: _description_
        """
        return await TodoService.update(id,todo_data)

