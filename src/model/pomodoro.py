from datetime import datetime

from sqlmodel import Relationship, SQLModel, Field
from uuid import UUID, uuid4
from model.user import User


class Pomodoro(SQLModel, table=True):
    """This is a model for the table in the DB.

    Args:
        SQLModel (_type_): _description_
        table (bool, optional): _description_. Defaults to True.
    """
    __tablename__ = "pomodoro"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    date_time: datetime = Field(
        sa_column_kwargs={"nullable": False})  # Use date_time and not datetime for distinguish from datetime library
    duration: int
    user_id: UUID = Field(foreign_key="users.id")
    user: "User" = Relationship(back_populates="pomodoros")
