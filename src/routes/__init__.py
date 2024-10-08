from fastapi import FastAPI
from .file_routes import router as files


def init_routes(app: FastAPI):
    app.include_router(files)
