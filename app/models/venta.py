from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class VentaBase(SQLModel):
    total: float


class VentaCreate(VentaBase):
    pass


class VentaRead(VentaBase):
    id: int
    fecha: datetime


class Venta(VentaBase, table=True):
    __tablename__ = "ventas"

    id: Optional[int] = Field(default=None, primary_key=True)
    fecha: datetime = Field(default_factory=datetime.now)