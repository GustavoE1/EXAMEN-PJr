from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Venta(SQLModel, table=True):
    __tablename__ = "ventas"

    id: Optional[int] = Field(default=None, primary_key=True)

    fecha: datetime = Field(default_factory=datetime.now)

    total: float