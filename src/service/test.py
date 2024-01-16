
from model.test import Test
from repository.test import TestRepository
from schema import TestInput, TestType


class TestService:
    """Service class for the test entity. This class is responsible to manage all operations related with tests in.

    Returns:
        _type_: _description_
    """
    @staticmethod
    async def create_test(test_data:TestInput):
        """Create a new test in the database.

        Args:
            test_data (TestInput): _description_

        Returns:
            _type_: _description_
        """
        test = Test()
        test.name = test_data.name
        test.description = test_data.description
        await TestRepository.create(test)

        return TestType(id = test.id,name = test.name, description = test.description)

    @staticmethod
    async def get_all_test():
        """Get all tests from the database.

        Returns:
            _type_: _description_
        """
        list_test = await TestRepository.get_all()
        return [TestType(id = test.id,name = test.name,description=test.description) for test in list_test]

    @staticmethod
    async def get_by_id_test(test_id:int):
        """Get an specific test by its id.

        Args:
            test_id (int): _description_

        Returns:
            _type_: _description_
        """
        test = await TestRepository.get_by_id(test_id)
        return TestType(id=test.id,name=test.name,description=test.description)

    @staticmethod
    async def delete_test(test_id: int):
        """Delete a test by its ID.

        Args:
            test_id (int): _description_

        Returns:
            _type_: _description_
        """
        await TestRepository.delete(test_id)
        return f'Successfully deleted data by id {test_id}'

    @staticmethod
    async def update_test(test_id:int, test_data: TestInput):
        """Update a test on the database with new information.

        Args:
            test_id (int): _description_
            test_data (TestInput): _description_

        Returns:
            _type_: _description_
        """
        test = Test()
        test.name = test_data.name
        test.description = test_data.description
        await TestRepository.update(test_id,Test)
        return f'Successfully updated data by id {test_id}'
