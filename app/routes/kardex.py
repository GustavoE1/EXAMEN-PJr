from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.db.database import get_session
from app.services import kardex_service

router = APIRouter(prefix="/api/kardex", tags=["Kardex"])


@router.get("/")
def listar_kardex(session: Session = Depends(get_session)):
    return kardex_service.listar_movimientos(session)


@router.get("/producto/{producto_id}")
def listar_kardex_por_producto(
    producto_id: int,
    session: Session = Depends(get_session)
):
    return kardex_service.listar_movimientos_por_producto(
        session=session,
        producto_id=producto_id
    )