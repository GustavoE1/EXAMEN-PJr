from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.db.database import get_session
from app.services import inventario_service

router = APIRouter(prefix="/api/inventario", tags=["Inventario"])


@router.post("/ingreso/{producto_id}")
def registrar_ingreso_stock(
    producto_id: int,
    cantidad: int,
    session: Session = Depends(get_session)
):
    producto = inventario_service.registrar_ingreso_stock(
        session=session,
        producto_id=producto_id,
        cantidad=cantidad
    )

    if not producto:
        raise HTTPException(
            status_code=400,
            detail="Producto no encontrado o cantidad inválida"
        )

    return {
        "message": "Ingreso de stock registrado correctamente",
        "producto_id": producto.id,
        "stock_actual": producto.stock_actual
    }