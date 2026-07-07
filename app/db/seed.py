from sqlmodel import Session

from app.db.database import engine
from app.models.producto import Producto


with Session(engine) as session:

    session.add_all([
        Producto(
            nombre="Cabernet Sauvignon",
            marca="Toro",
            tipo="Tinto",
            presentacion="750 ml",
            precio_venta=55,
            stock_actual=20
        ),
        Producto(
            nombre="Merlot",
            marca="Santa Rita",
            tipo="Tinto",
            presentacion="750 ml",
            precio_venta=48,
            stock_actual=15
        ),
        Producto(
            nombre="Sauvignon Blanc",
            marca="Casillero del Diablo",
            tipo="Blanco",
            presentacion="750 ml",
            precio_venta=42,
            stock_actual=10
        )
    ])

    session.commit()

print("Datos insertados correctamente.")