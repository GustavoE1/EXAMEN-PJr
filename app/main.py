from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlmodel import SQLModel

from app.db.database import engine
from app.models import *
from app.routes.productos import router as productos_router
from app.routes.pages import router as pages_router
from app.routes.inventario import router as inventario_router
from app.routes.ventas import router as ventas_router
from app.routes.kardex import router as kardex_router
SQLModel.metadata.create_all(engine)

app = FastAPI(
    title="Sistema de ventas de Vinos",
    
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(productos_router)
app.include_router(pages_router)
app.include_router(inventario_router)
app.include_router(ventas_router)
app.include_router(kardex_router)