from typing import List, Optional

from sqlmodel import Session, select

from app.models.producto import Producto, ProductoCreate, ProductoUpdate


def crear_producto(
    session: Session,
    producto_data: ProductoCreate
) -> Producto:
    producto = Producto.model_validate(producto_data)

    session.add(producto)
    session.commit()
    session.refresh(producto)

    return producto


def listar_productos(session: Session) -> List[Producto]:
    statement = select(Producto).order_by(Producto.id)
    return session.exec(statement).all()


def obtener_producto_por_id(
    session: Session,
    producto_id: int
) -> Optional[Producto]:
    return session.get(Producto, producto_id)


def actualizar_producto(
    session: Session,
    producto_id: int,
    producto_data: ProductoUpdate
) -> Optional[Producto]:
    producto = session.get(Producto, producto_id)

    if not producto:
        return None

    datos_actualizados = producto_data.model_dump(exclude_unset=True)

    for campo, valor in datos_actualizados.items():
        setattr(producto, campo, valor)

    session.add(producto)
    session.commit()
    session.refresh(producto)

    return producto