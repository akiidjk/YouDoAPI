import strawberry

from schema import TestType
from service.test import TestService


@strawberry.type
class Query:
    """The GraphQL query type for the test application. This class represents a single point of entry into the api.

    Returns:
        _type_: _description_
    """
    @strawberry.field
    def hello(self) -> str:
        """Get a greeting message from the server.

        Returns:
            str: _description_
        """
        return "Hello World!"

    @strawberry.field
    async def get_all(self) -> list[TestType]:
        """Get all test data.

        Returns:
            list[TestType]: _description_
        """
        return await TestService.get_all_Test()

    @strawberry.field
    async def get_by_id(self,id:int) -> TestType:
        """Get one test data by id.

        Args:
            id (int): _description_

        Returns:
            TestType: _description_
        """
        return await TestService.get_by_id(id)
