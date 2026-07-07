from typing import Optional

from sqlmodel import Field, SQLModel


class DetalleVentaBase(SQLModel):
    venta_id: int
    producto_id: int
    cantidad: int
    precio_unitario: float
    subtotal: float


class DetalleVentaRead(DetalleVentaBase):
    id: int


class DetalleVenta(DetalleVentaBase, table=True):
    __tablename__ = "detalle_ventas"

    id: Optional[int] = Field(default=None, primary_key=True)
    venta_id: int = Field(foreign_key="ventas.id")
    producto_id: int = Field(foreign_key="productos.id")