from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlmodel import SQLModel

from app.db.database import engine
from app.models import *
from app.routes.productos import router as productos_router
from app.routes.pages import router as pages_router

SQLModel.metadata.create_all(engine)

app = FastAPI(
    title="Sistema Kardex de Vinos",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(productos_router)
app.include_router(pages_router)

