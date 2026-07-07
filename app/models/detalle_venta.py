from typing import Optional

from sqlmodel import Field, SQLModel


class DetalleVenta(SQLModel, table=True):
    __tablename__ = "detalle_ventas"

    id: Optional[int] = Field(default=None, primary_key=True)

    venta_id: int = Field(foreign_key="ventas.id")

    producto_id: int = Field(foreign_key="productos.id")

    cantidad: int

    precio_unitario: float

    subtotal: float