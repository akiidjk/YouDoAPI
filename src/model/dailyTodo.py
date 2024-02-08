from datetime import datetime

from sqlmodel import Relationship, SQLModel, Field
from uuid import UUID, uuid4
from model.user import User
class Todo(SQLModel, table=True):
    """This is a the model for the table in the DB.

    Args:
        SQLModel (_type_): _description_
        table (bool, optional): _description_. Defaults to True.
    """
    __tablename__ = "dailyTodo"

    id: UUID =Field(default_factory=uuid4, primary_key=True)
    title: str
    description:str | None
    datetime_created: datetime = Field(sa_column_kwargs={"nullable": False})
    datetime_expire: datetime = Field(sa_column_kwargs={"nullable": False})
    status_done:bool
    priority:int
    favorite:bool
    user_id: UUID = Field(foreign_key="users.id")
    user: "User" = Relationship(back_populates="todos")


