from typing import List

from sqlmodel import Session, select

from app.models.kardex import Kardex


def listar_movimientos(session: Session) -> List[Kardex]:
    statement = select(Kardex).order_by(Kardex.fecha.desc())
    return session.exec(statement).all()


def listar_movimientos_por_producto(
    session: Session,
    producto_id: int
) -> List[Kardex]:
    statement = (
        select(Kardex)
        .where(Kardex.producto_id == producto_id)
        .order_by(Kardex.fecha.desc())
    )

    return session.exec(statement).all()