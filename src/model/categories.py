from sqlalchemy import Column, ARRAY, String
from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID, uuid4

from model.user import User


class Categories(SQLModel, table=True):
    """This is a model for the table in the DB.

    Args:
        SQLModel (_type_): _description_
        table (bool, optional): _description_. Defaults to True.
    """
    __tablename__ = "categories"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    categories: list[str] = Field(sa_column=Column(ARRAY(String)))
    user_id: UUID = Field(foreign_key="users.id")
    user: "User" = Relationship(back_populates="categories")
