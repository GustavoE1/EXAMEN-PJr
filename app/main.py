from fastapi import FastAPI
from sqlmodel import SQLModel

from app.db.database import engine
from app.models import *

SQLModel.metadata.create_all(engine)

app = FastAPI(
    title="Sistema Kardex de Vinos",
    version="1.0.0"
)


@app.get("/")
def home():
    return {"message": "Sistema Kardex de Vinos"}