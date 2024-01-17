
#######################################################
#! The file declare the two type for the GraphQL quey #
#######################################################

import strawberry




# * When get a row
@strawberry.type
class DailyTodoType:
    """Class to represent the data of todoDaily in the graphql query."""
    id:int
    title:str
    description:str
    date_created:str
    date_expire:str
    status_done:bool

# * When put a element

@strawberry.input
class DailyTodoInput:
    """Class to represent the data in the mutation query."""
    title:str
    description:str
    date_created:str
    date_expire:str
    status_done:bool
