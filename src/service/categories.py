from uuid import UUID
from model.categories import Categories
from repository.categories import CategoriesRepository
from schema import CategoriesInput, CategoriesType


class CategoryService:
    """Service class for the categories' entity. This class is responsible to manage all operations related to categories in.

    Returns:
        _type_: _description_
    """

    @staticmethod
    async def get_all(user_id: UUID) -> CategoriesType:
        """Get all categories from the database.

        Returns:
            _type_: _description_
        """
        category = await CategoriesRepository.get_all(user_id=user_id)
        return CategoriesType(id=category.id,
                              categories=category.categories,
                              user_id=category.user_id)

    @staticmethod
    async def create(category_data: CategoriesInput) -> CategoriesType:
        """Create a new category in the database.

        Args:
            category_data (CategoriesInput): _description_

        Returns:
            _type_: _description_
        """
        category = Categories()
        category.categories = category_data.categories
        category.user_id = category_data.user_id
        await CategoriesRepository.create(category)
        return CategoriesType(id=category.id,
                              categories=category.categories,
                              user_id=category.user_id)

    @staticmethod
    async def update(category_id: UUID, category_data: CategoriesInput) -> str:
        """Update a category on the database with new information.

        Args:
            category_id (UUID): _description_
            category_data (CategoriesInput): _description_

        Returns:
            _type_: _description_
        """
        category = Categories()
        category.categories = category_data.categories
        category.user_id = category_data.user_id
        await CategoriesRepository.update(category_id, category)
        return f'Successfully updated data by id {category_id}'

    @staticmethod
    async def delete(category_id: UUID) -> UUID:
        """Delete a category by its ID.

        Args:
            category_id (UUID): _description_

        Returns:
            _type_: _description_
        """
        await CategoriesRepository.delete(category_id)
        return category_id

    @staticmethod
    async def add_category(user_id: UUID, category: str) -> UUID:
        """Add a categories in the array of categories of the user.
        Args:
            user_id:
            category:

        Returns:

        """
        return await CategoriesRepository.add_category(user_id, category)

    @staticmethod
    async def remove_category(user_id: UUID, category: str) -> UUID:
        """Add a categories in the array of categories of the user.
        Args:
            user_id:
            category:

        Returns:

        """
        return await CategoriesRepository.remove_category(user_id, category)
