from fastapi import FastAPI
from containers import Container
import endpoints


def create_app() -> FastAPI:
    container = Container()
    db = container.db()
    db.create_database()

    fast_app = FastAPI()
    fast_app.container = container
    fast_app.include_router(endpoints.router)
    return fast_app


app = create_app()
