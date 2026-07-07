from datetime import datetime
from enum import Enum
from typing import Optional

from sqlmodel import Field, SQLModel


class TipoMovimiento(str, Enum):
    INGRESO = "INGRESO"
    SALIDA_VENTA = "SALIDA_VENTA"


class KardexBase(SQLModel):
    producto_id: int
    tipo_movimiento: TipoMovimiento
    cantidad: int
    stock_anterior: int
    stock_nuevo: int
    referencia: str = Field(max_length=100)


class KardexRead(KardexBase):
    id: int
    fecha: datetime


class Kardex(KardexBase, table=True):
    __tablename__ = "kardex"

    id: Optional[int] = Field(default=None, primary_key=True)
    producto_id: int = Field(foreign_key="productos.id")
    fecha: datetime = Field(default_factory=datetime.now)