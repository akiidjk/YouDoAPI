import strawberry

from schema import TestInput, TestType
from service.test import TestService


@strawberry.type
class Mutation:
    """The mutations available in the GraphQL API for testing purposes.

    Returns:
        _type_: _description_
    """

    @strawberry.mutation
    async def create_test(self,test_data:TestInput) -> TestType:
        """Create a new test case with given data.

        Args:
            test_data (TestInput): _description_

        Returns:
            TestType: _description_
        """
        return await TestService.create_test(test_data=test_data)

    @strawberry.mutation
    async def delete_test(self,id:int) -> str:
        """Delete an existing test case by its id.

        Args:
            id (int): _description_

        Returns:
            str: _description_
        """
        return await TestService.detete_test(id)

    @strawberry.mutation
    async def update_test(self,id:int,test_data:TestInput) -> str:
        """Update an existing test case's information.

        Args:
            id (int): _description_
            test_data (TestInput): _description_

        Returns:
            str: _description_
        """
        return await TestService.update(id,test_data)
