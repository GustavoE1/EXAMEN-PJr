from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlmodel import Session

from app.db.database import get_session
from app.services import venta_service

router = APIRouter(prefix="/api/ventas", tags=["Ventas"])


class VentaItemRequest(BaseModel):
    producto_id: int
    cantidad: int


class VentaRequest(BaseModel):
    items: List[VentaItemRequest]


@router.post("/")
def crear_venta(
    venta_data: VentaRequest,
    session: Session = Depends(get_session)
):
    try:
        venta = venta_service.crear_venta(
            session=session,
            items=[item.model_dump() for item in venta_data.items]
        )

        return {
            "message": "Venta registrada correctamente",
            "venta_id": venta.id,
            "total": venta.total
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )