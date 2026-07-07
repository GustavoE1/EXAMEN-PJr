from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.db.database import get_session
from app.models.producto import ProductoCreate, ProductoRead, ProductoUpdate
from app.services import producto_service

router = APIRouter(prefix="/api/productos", tags=["Productos"])


@router.get("/", response_model=List[ProductoRead])
def listar_productos(session: Session = Depends(get_session)):
    return producto_service.listar_productos(session)


@router.get("/{producto_id}", response_model=ProductoRead)
def obtener_producto(
    producto_id: int,
    session: Session = Depends(get_session)
):
    producto = producto_service.obtener_producto_por_id(session, producto_id)

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return producto


@router.post("/", response_model=ProductoRead)
def crear_producto(
    producto_data: ProductoCreate,
    session: Session = Depends(get_session)
):
    return producto_service.crear_producto(session, producto_data)


@router.put("/{producto_id}", response_model=ProductoRead)
def actualizar_producto(
    producto_id: int,
    producto_data: ProductoUpdate,
    session: Session = Depends(get_session)
):
    producto = producto_service.actualizar_producto(
        session=session,
        producto_id=producto_id,
        producto_data=producto_data
    )

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return producto