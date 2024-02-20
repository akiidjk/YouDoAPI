from sqlmodel import Relationship, SQLModel, Field
from uuid import uuid4, UUID


class User(SQLModel, table=True):
    """This is a model for the table in the DB.

    Args:
        SQLModel (_type_): _description_
        table (bool, optional): _description_. Defaults to True.
    """
    __tablename__ = "users"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    email: str
    todos: list["Todo"] = Relationship(back_populates="user")
    pomodoros: list["Pomodoro"] = Relationship(back_populates="user")
    categories: list["Categories"] = Relationship(back_populates="user")
