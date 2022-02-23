import os

import uvicorn
from fastapi import FastAPI

from app.routers import healthcheck


app = FastAPI(
    title="{{ cookiecutter.name }}",
    version="{{ cookiecutter.version }}",
    description="{{ cookiecutter.description }}"
)

app.include_router(healthcheck.router)

@app.get("/")
async def root():
    """
        Load the project name as a message on the API root route.
    """
    return {"message": "{{ cookiecutter.name }}"}


if __name__ == "__main__":
    uvicorn.run(app, log_level="info")
