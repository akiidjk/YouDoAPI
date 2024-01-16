
#######################################################
#! The file declare the two type for the GraphQL quey #
#######################################################

import strawberry


# * When get a row
@strawberry.type
class TestType:
    """This class represent the data of one row in the database, it's used to parse the result from the query."""
    id:int
    name:str
    description:str

# * When put a element
@strawberry.input
class TestInput:
    """This class is used to send data to create or update an object in the database."""
    name:str
    description:str
