const PRODUCTOS_API = "/api/productos";
const INVENTARIO_API = "/api/inventario";

document.addEventListener("DOMContentLoaded", () => {
    cargarProductos();
});

async function cargarProductos() {
    const response = await fetch(PRODUCTOS_API);
    const productos = await response.json();

    const select = document.getElementById("producto_id");
    select.innerHTML = "";

    productos.forEach(producto => {
        select.innerHTML += `
            <option value="${producto.id}">
                ${producto.nombre} - Stock actual: ${producto.stock_actual}
            </option>
        `;
    });
}

async function registrarIngreso() {
    const productoId = document.getElementById("producto_id").value;
    const cantidad = document.getElementById("cantidad").value;

    const response = await fetch(
        `${INVENTARIO_API}/ingreso/${productoId}?cantidad=${cantidad}`,
        {
            method: "POST"
        }
    );

    const data = await response.json();

    if (!response.ok) {
        mostrarMensaje(data.detail || "Error al registrar ingreso", "danger");
        return;
    }

    mostrarMensaje("Ingreso registrado correctamente", "success");

    document.getElementById("cantidad").value = "";

    cargarProductos();
}

function mostrarMensaje(texto, tipo) {
    const mensaje = document.getElementById("mensaje");

    mensaje.className = `alert alert-${tipo}`;
    mensaje.textContent = texto;
}