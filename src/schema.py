
#######################################################
#! The file declare the two type for the GraphQL quey #
#######################################################

import strawberry

# * When get a row
@strawberry.type
class TodoType:
    """Class to represent the data of todoDaily in the graphql query."""
    id:int
    title:str
    description:str
    date_created:str
    date_expire:str
    status_done:bool
    user_id:int
    priority:int
    favorite:bool

@strawberry.type
class UserType:
    """Class to represent the data of User in the graphql query."""
    id:int
    email:str


# * When put a element
@strawberry.input
class TodoInput:
    """Class to represent the data in the mutation query."""
    title:str
    description:str
    date_created:str
    date_expire:str
    status_done:bool
    user_id:int
    priority:int
    favorite:bool

@strawberry.input
class UserInput:
    """Class to represent the data in the mutation query."""
    email:str


