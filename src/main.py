"""Main file for the API."""
from contextlib import asynccontextmanager
from fastapi import FastAPI
import strawberry
import uvicorn

from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from starlette.requests import Request
from starlette.responses import JSONResponse

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

    limiter = Limiter(key_func=get_remote_address)
    app = FastAPI(
        title='YouDoAPI',
        description='API for the communication with YouDo app',
        version='0.0.1',
        lifespan=lifespan
    )

    @app.exception_handler(RateLimitExceeded)
    async def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded):
        return JSONResponse(
            status_code=429,
            content={"detail": "Rate limit exceeded"},
        )

    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)

    @app.get('/')
    @limiter.limit("100/minute")
    def home(request: Request):
        return {'message': 'The api is online'}

    schema = strawberry.Schema(query=Query, mutation=Mutation)
    graphql_app = GraphQLRouter(schema)

    app.include_router(graphql_app, prefix="/graphql")

    return app


app = init_app()

if __name__ == '__main__':
    uvicorn.run(app='main:app', host="localhost", port=8081, reload=False)
