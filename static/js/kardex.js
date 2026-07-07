const PRODUCTOS_API = "/api/productos";
const KARDEX_API = "/api/kardex";

document.addEventListener("DOMContentLoaded", () => {
    cargarProductos();
    cargarKardex();
});

async function cargarProductos() {
    const response = await fetch(PRODUCTOS_API);
    const productos = await response.json();

    const select = document.getElementById("producto_id");

    productos.forEach(producto => {
        select.innerHTML += `
            <option value="${producto.id}">
                ${producto.nombre}
            </option>
        `;
    });
}

async function cargarKardex(url = KARDEX_API) {
    const response = await fetch(url);
    const movimientos = await response.json();

    const tbody = document.getElementById("tabla-kardex");
    tbody.innerHTML = "";

    movimientos.forEach(mov => {
        const fecha = new Date(mov.fecha).toLocaleString();

        tbody.innerHTML += `
            <tr>
                <td>${fecha}</td>
                <td>${mov.producto_id}</td>
                <td>${mov.tipo_movimiento}</td>
                <td>${mov.cantidad}</td>
                <td>${mov.stock_anterior}</td>
                <td>${mov.stock_nuevo}</td>
                <td>${mov.referencia}</td>
            </tr>
        `;
    });
}

function filtrarKardex() {
    const productoId = document.getElementById("producto_id").value;

    if (productoId === "") {
        cargarKardex();
        return;
    }

    cargarKardex(`${KARDEX_API}/producto/${productoId}`);
}