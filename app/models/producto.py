from typing import Optional

from sqlmodel import Field, SQLModel


class ProductoBase(SQLModel):
    nombre: str = Field(max_length=100)
    marca: str = Field(max_length=100)
    tipo: str = Field(max_length=50)
    presentacion: str = Field(max_length=50)
    precio_venta: float
    stock_actual: int


class ProductoCreate(ProductoBase):
    pass


class ProductoUpdate(SQLModel):
    nombre: Optional[str] = Field(default=None, max_length=100)
    marca: Optional[str] = Field(default=None, max_length=100)
    tipo: Optional[str] = Field(default=None, max_length=50)
    presentacion: Optional[str] = Field(default=None, max_length=50)
    precio_venta: Optional[float] = None
    stock_actual: Optional[int] = None


class ProductoRead(ProductoBase):
    id: int


class Producto(ProductoBase, table=True):
    __tablename__ = "productos"

    id: Optional[int] = Field(default=None, primary_key=True)