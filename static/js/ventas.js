const PRODUCTOS_API = "/api/productos";
const VENTAS_API = "/api/ventas";

let productos = [];
let itemsVenta = [];

document.addEventListener("DOMContentLoaded", () => {
    cargarProductos();
});

async function cargarProductos() {
    const response = await fetch(PRODUCTOS_API);
    productos = await response.json();

    const select = document.getElementById("producto_id");
    select.innerHTML = "";

    productos.forEach(producto => {
        select.innerHTML += `
            <option value="${producto.id}">
                ${producto.nombre} - Stock: ${producto.stock_actual} - S/. ${producto.precio_venta}
            </option>
        `;
    });
}

function agregarProductoVenta() {
    const productoId = parseInt(document.getElementById("producto_id").value);
    const cantidad = parseInt(document.getElementById("cantidad").value);

    if (!productoId || cantidad <= 0) {
        mostrarMensaje("Seleccione un producto y una cantidad válida", "danger");
        return;
    }

    const producto = productos.find(p => p.id === productoId);

    if (!producto) {
        mostrarMensaje("Producto no encontrado", "danger");
        return;
    }

    const cantidadYaAgregada = itemsVenta
        .filter(item => item.producto_id === productoId)
        .reduce((total, item) => total + item.cantidad, 0);

    const cantidadTotal = cantidadYaAgregada + cantidad;

    if (cantidadTotal > producto.stock_actual) {
        mostrarMensaje(
            `Stock insuficiente. Stock disponible: ${producto.stock_actual}. Ya agregaste: ${cantidadYaAgregada}.`,
            "danger"
        );
        return;
    }

    itemsVenta.push({
        producto_id: producto.id,
        nombre: producto.nombre,
        cantidad: cantidad,
        precio_unitario: producto.precio_venta,
        subtotal: producto.precio_venta * cantidad
    });

    document.getElementById("cantidad").value = "";

    renderizarTablaVenta();
}

function renderizarTablaVenta() {
    const tbody = document.getElementById("tabla-venta");
    tbody.innerHTML = "";

    let total = 0;

    itemsVenta.forEach(item => {
        total += item.subtotal;

        tbody.innerHTML += `
            <tr>
                <td>${item.nombre}</td>
                <td>${item.cantidad}</td>
                <td>S/. ${item.precio_unitario}</td>
                <td>S/. ${item.subtotal}</td>
            </tr>
        `;
    });

    document.getElementById("total").textContent = total.toFixed(2);
}

async function registrarVenta() {
    if (itemsVenta.length === 0) {
        mostrarMensaje("Debe agregar al menos un producto", "danger");
        return;
    }

    const payload = {
        items: itemsVenta.map(item => ({
            producto_id: item.producto_id,
            cantidad: item.cantidad
        }))
    };

    const response = await fetch(VENTAS_API, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    });

    const data = await response.json();

    if (!response.ok) {
        mostrarMensaje(data.detail || "Error al registrar venta", "danger");
        return;
    }

    mostrarMensaje(`Venta registrada correctamente. Total: S/. ${data.total}`, "success");

    itemsVenta = [];
    renderizarTablaVenta();
    cargarProductos();
}

function mostrarMensaje(texto, tipo) {
    const mensaje = document.getElementById("mensaje");

    mensaje.className = `alert alert-${tipo}`;
    mensaje.textContent = texto;
}