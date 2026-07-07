from typing import List

from sqlmodel import Session, select

from app.models.kardex import Kardex
from app.models.producto import Producto
from sqlmodel import select


def listar_movimientos(session: Session):
    statement = (
        select(Kardex, Producto)
        .join(Producto, Kardex.producto_id == Producto.id)
        .order_by(Kardex.fecha.desc())
    )

    resultados = session.exec(statement).all()

    return [
        {
            "fecha": kardex.fecha,
            "producto": producto.nombre,
            "tipo_movimiento": kardex.tipo_movimiento,
            "cantidad": kardex.cantidad,
            "stock_anterior": kardex.stock_anterior,
            "stock_nuevo": kardex.stock_nuevo,
            "referencia": kardex.referencia
        }
        for kardex, producto in resultados
    ]

def listar_movimientos_por_producto(session: Session, producto_id: int):
    statement = (
        select(Kardex, Producto)
        .join(Producto, Kardex.producto_id == Producto.id)
        .where(Kardex.producto_id == producto_id)
        .order_by(Kardex.fecha.desc())
    )

    resultados = session.exec(statement).all()

    return [
        {
            "fecha": kardex.fecha,
            "producto": producto.nombre,
            "tipo_movimiento": kardex.tipo_movimiento,
            "cantidad": kardex.cantidad,
            "stock_anterior": kardex.stock_anterior,
            "stock_nuevo": kardex.stock_nuevo,
            "referencia": kardex.referencia
        }
        for kardex, producto in resultados
    ]