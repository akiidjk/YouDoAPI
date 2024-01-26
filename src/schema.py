
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
    email_user:str
    priority:int
    favorite:bool


# * When put a element

@strawberry.input
class TodoInput:
    """Class to represent the data in the mutation query."""
    title:str
    description:str
    date_created:str
    date_expire:str
    status_done:bool
    email_user:str
    priority:int
    favorite:bool


