from model.user import User
from repository.user import UserRepository
from schema import UserInput, UserType


class UserService:
    """Service class for the user entity. This class is responsible to manage all operations related with user in.

    Returns:
        _type_: _description_
    """
    @staticmethod
    async def create(user_data:UserInput):
        """Create a new user in the database.

        Args:
            user_data (UserInput): The user data

        Returns:
            _type_: _description_
        """
        user = User()
        user.email = user_data.email
        id_user = await UserRepository.create(user)
        if(user.id is None):
            return UserType(id = id_user,
                            email = None)
        return UserType(id = id_user,
                            email = user.email)

    @staticmethod
    async def get_all():
        """Get all user from the database.

        Returns:
            _type_: _description_
        """
        list_user = await UserRepository.get_all()
        return [UserType(id = user.id,
                             email = user.email,
                            ) for user in list_user]

    @staticmethod
    async def get_by_id(user_id:int) -> UserType:
        """Get an specific test by its id.

        Args:
            user_id (int): The id of the user

        Returns:
            _type_: _description_
        """
        user = await UserRepository.get_by_id(user_id)
        return UserType(id = user.id,
                        email = user.email)
    @staticmethod
    async def get_by_email(user_email:str) -> UserType:
        """Get an specific test by its id.

        Args:
            user_email (int): The id of the user

        Returns:
            _type_: _description_
        """
        user = await UserRepository.get_by_email(user_email)
        return UserType(id = user.id,
                        email = user.email)

    @staticmethod
    async def delete(user_id: int) -> int:
        """Delete a test by its ID.

        Args:
            user_id (int): The id of the user

        Returns:
            _type_: _description_
        """
        await UserRepository.delete(user_id)
        return user_id

    @staticmethod
    async def update(user_id:int, user_data: UserInput) -> str:
        """Update a user on the database with new information.

        Args:
            user_id (int): _description_
            user_data (DailyTodoInput): _description_

        Returns:
            _type_: _description_
        """
        user = User()
        user.email = user_data.email

        await UserRepository.update(user_id,user)
        return f'Successfully updated data by id {user_id}'
