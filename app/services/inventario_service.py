from typing import Optional

from sqlmodel import Session

from app.models.producto import Producto
from app.models.kardex import Kardex, TipoMovimiento


def registrar_ingreso_stock(
    session: Session,
    producto_id: int,
    cantidad: int
) -> Optional[Producto]:

    if cantidad <= 0:
        return None

    producto = session.get(Producto, producto_id)

    if not producto:
        return None

    stock_anterior = producto.stock_actual
    stock_nuevo = stock_anterior + cantidad

    producto.stock_actual = stock_nuevo

    movimiento = Kardex(
        producto_id=producto.id,
        tipo_movimiento=TipoMovimiento.INGRESO,
        cantidad=cantidad,
        stock_anterior=stock_anterior,
        stock_nuevo=stock_nuevo,
        referencia="Ingreso de stock"
    )

    session.add(producto)
    session.add(movimiento)
    session.commit()
    session.refresh(producto)

    return producto