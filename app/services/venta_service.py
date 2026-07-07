from typing import List, Dict, Any

from sqlmodel import Session

from app.models.producto import Producto
from app.models.venta import Venta
from app.models.detalle_venta import DetalleVenta
from app.models.kardex import Kardex, TipoMovimiento


def crear_venta(
    session: Session,
    items: List[Dict[str, Any]]
) -> Venta:

    if not items:
        raise ValueError("La venta debe tener al menos un producto")

    total = 0
    productos_validos = []

    for item in items:
        producto_id = item["producto_id"]
        cantidad = item["cantidad"]

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero")

        producto = session.get(Producto, producto_id)

        if not producto:
            raise ValueError("Producto no encontrado")

        if producto.stock_actual < cantidad:
            raise ValueError(f"Stock insuficiente para {producto.nombre}")

        subtotal = producto.precio_venta * cantidad
        total += subtotal

        productos_validos.append({
            "producto": producto,
            "cantidad": cantidad,
            "precio_unitario": producto.precio_venta,
            "subtotal": subtotal
        })

    venta = Venta(total=total)
    session.add(venta)
    session.commit()
    session.refresh(venta)

    for item in productos_validos:
        producto = item["producto"]
        cantidad = item["cantidad"]

        stock_anterior = producto.stock_actual
        stock_nuevo = stock_anterior - cantidad

        producto.stock_actual = stock_nuevo

        detalle = DetalleVenta(
            venta_id=venta.id,
            producto_id=producto.id,
            cantidad=cantidad,
            precio_unitario=item["precio_unitario"],
            subtotal=item["subtotal"]
        )

        movimiento = Kardex(
            producto_id=producto.id,
            tipo_movimiento=TipoMovimiento.SALIDA_VENTA,
            cantidad=cantidad,
            stock_anterior=stock_anterior,
            stock_nuevo=stock_nuevo,
            referencia=f"Venta #{venta.id}"
        )

        session.add(producto)
        session.add(detalle)
        session.add(movimiento)

    session.commit()
    session.refresh(venta)

    return venta