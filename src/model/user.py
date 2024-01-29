from sqlmodel import Relationship, SQLModel, Field
class User(SQLModel, table=True):
    """This is a the model for the table in the DB.

    Args:
        SQLModel (_type_): _description_
        table (bool, optional): _description_. Defaults to True.
    """
    __tablename__ = "users"

    id: int | None = Field(None,primary_key=True,nullable=True)
    email:str
    todos: list["Todo"] = Relationship(back_populates="user")


