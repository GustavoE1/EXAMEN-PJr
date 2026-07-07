from typing import Optional

from sqlmodel import Field, SQLModel


class Producto(SQLModel, table=True):
    __tablename__ = "productos"

    id: Optional[int] = Field(default=None, primary_key=True)

    nombre: str = Field(max_length=100)
    marca: str = Field(max_length=100)
    tipo: str = Field(max_length=50)
    presentacion: str = Field(max_length=50)
    precio_venta: float
    stock_actual: int = Field(default=0)
