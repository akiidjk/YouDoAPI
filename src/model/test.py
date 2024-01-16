from sqlmodel import SQLModel, Field
class Test(SQLModel, table=True):
    """This is a the model for the table in the DB.

    Args:
        SQLModel (_type_): _description_
        table (bool, optional): _description_. Defaults to True.
    """
    __tablename__ = "test"

    id: int | None = Field(None,primary_key=True,nullable=True)
    name:str
    description:str
