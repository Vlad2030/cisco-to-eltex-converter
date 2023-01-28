from backend.api import convert_commands
from frontend import site
from fastapi import FastAPI
from pydantic import BaseModel
from loguru import logger


app = FastAPI()


class Syntax(BaseModel):
    syntax_code: str


@app.on_event("startup")
async def startup():
    return logger.info("WebApp Started")


@app.on_event("shutdown")
async def shutdown():
    return logger.warning("WebApp Shutdown")


@app.get("/api/transform/{syntax_code}")
async def transform(syntax_code: str):
    pass
