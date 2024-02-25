#######################################################
# ! The file declare the two types for the GraphQL query #
#######################################################

from datetime import datetime

from uuid import UUID
import strawberry


# * When get a row
@strawberry.type
class TodoType:
    """Class to represent the data of todoDaily in the graphql query."""
    id: UUID
    title: str
    description: str | None
    datetime_created: datetime
    datetime_expire: datetime
    status_done: bool
    user_id: UUID
    priority: int
    favorite: bool
    category: str | None
    remember: bool



@strawberry.type
class UserType:
    """Class to represent the data of User in the graphql query."""
    id: UUID
    email: str


@strawberry.type
class PomodoroType:
    """Class to represent the data of User in the graphql query."""
    id: UUID
    date_time: datetime
    duration: int
    user_id: UUID


@strawberry.type
class CategoriesType:
    """Class to represent the data of User in the graphql query."""
    id: UUID
    categories: list[str]
    user_id: UUID


# * When put an element
@strawberry.input
class TodoInput:
    """Class to represent the data in the mutation query."""
    title: str
    description: str | None
    datetime_created: datetime
    datetime_expire: datetime
    status_done: bool
    user_id: UUID
    priority: int
    favorite: bool
    category: str | None
    remember: bool


@strawberry.input
class UserInput:
    """Class to represent the data in the mutation query."""
    email: str


@strawberry.input
class PomodoroInput:
    """Class to represent the data in the mutation query."""
    date_time: datetime
    duration: int
    user_id: UUID


@strawberry.input
class CategoriesInput:
    """Class to represent the data in the mutation query."""
    categories: list[str]
    user_id: UUID
