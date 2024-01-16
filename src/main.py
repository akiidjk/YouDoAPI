"""Main file for the API."""
from contextlib import asynccontextmanager
from fastapi import FastAPI
import strawberry
import uvicorn

from strawberry.fastapi import GraphQLRouter

from config import db
from Graphql.mutation import Mutation
from Graphql.query import Query

def init_app():
    """Initialize the FastAPI application."""

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        await db.create_all()
        yield
        await db.close()

    app = FastAPI(
        title='YouDoAPI',
        description='API for the communication with YouDo app',
        version='0.0.1',
        lifespan=lifespan
    )

    @app.get('/')
    def home():
        return {'message':'The api is online'}

    schema = strawberry.Schema(query=Query,mutation=Mutation)
    graphql_app = GraphQLRouter(schema)

    app.include_router(graphql_app,prefix="/graphql")

    return app


app = init_app()

if __name__ == '__main__':
    uvicorn.run(app='main:app',host="localhost",port=1000,reload=True)
