# Sistema de venta de Vinos

Sistema web desarrollado con FastAPI para la gestión de productos, inventario, ventas y registro de movimientos tipo Kardex.

## Tecnologías utilizadas

- Python 3.13
- FastAPI
- SQLModel
- PostgreSQL
- HTML
- Bootstrap 5
- JavaScript
- Jinja2

---

## Instalación

### 1. Clonar el repositorio o extraer archivo .rar

```bash
git clone https://github.com/GustavoE1/EXAMEN-PJr.git
cd EXAMEN-PJr
```

### 2. Crear entorno virtual

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Configuración

Crear un archivo `.env` en la raíz del proyecto (**EXAMEN-PJR/**) con el siguiente contenido:

```env
POSTGRES_SERVER=localhost
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=tu_password
POSTGRES_DB=kardex_db
```

Crear previamente la base de datos:

```sql
CREATE DATABASE kardex_db;
```

---

## Ejecución

Ejecutar:

```bash
uvicorn app.main:app --reload
```

La aplicación estará disponible en:

```
http://127.0.0.1:8000
```

Documentación Swagger:

```
http://127.0.0.1:8000/docs
```

---

## Funcionalidades

- Gestión de productos
  - Registrar productos
  - Editar productos

- Inventario
  - Registrar ingresos de stock

- Ventas
  - Registrar ventas
  - Validación de stock disponible

- Kardex
  - Registro automático de ingresos
  - Registro automático de salidas por venta
  - Consulta de movimientos

---

## Estructura del proyecto

```
app/
├── config/
├── db/
├── models/
├── routes/
├── services/
├── main.py

templates/
static/
```

---

## Notas

- El stock solo puede modificarse mediante el módulo de Inventario y las Ventas.
- No se permite registrar productos con stock inicial negativo.
- No se permite vender una cantidad superior al stock disponible.
- Todos los movimientos de inventario quedan registrados en la seccion Kardex.
- IMPORTANTE: Las tablas de la base de datos se crean automáticamente al iniciar la aplicación
  por primera vez, de igual manera se esta dejando un script de postgres en el entregable.
- Opcionalmente, para insertar datos de ejemplo ejecutar:

  python -m app.db.seed

---

## Autor

Gustavo Bocanegra