const API_URL = "/api/productos";

document.addEventListener("DOMContentLoaded", () => {
    cargarProductos();
});

async function cargarProductos() {

    const response = await fetch(API_URL);
    const productos = await response.json();

    const tbody = document.getElementById("tabla-productos");

    tbody.innerHTML = "";

    productos.forEach(producto => {

        tbody.innerHTML += `
            <tr>
                <td>${producto.id}</td>
                <td>${producto.nombre}</td>
                <td>${producto.marca}</td>
                <td>${producto.tipo}</td>
                <td>${producto.presentacion}</td>
                <td>S/. ${producto.precio_venta}</td>
                <td>${producto.stock_actual}</td>
                <td>
                    <button
                    class="btn btn-warning btn-sm"
                    onclick="editarProducto(${producto.id})">
                    Editar
                </button>
                </td>
            </tr>
        `;

    });

}

async function guardarProducto() {

    const id = document.getElementById("producto_id").value;

    const producto = {

        nombre: document.getElementById("nombre").value,
        marca: document.getElementById("marca").value,
        tipo: document.getElementById("tipo").value,
        presentacion: document.getElementById("presentacion").value,
        precio_venta: parseFloat(document.getElementById("precio_venta").value),
        stock_actual: parseInt(document.getElementById("stock_actual").value)

    };

    if (id === "") {

        await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(producto)
        });

    } else {

        await fetch(`${API_URL}/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(producto)
        });

    }

    limpiarFormulario();

    cargarProductos();

}


function limpiarFormulario() {

    document.getElementById("producto_id").value = "";
    document.getElementById("nombre").value = "";
    document.getElementById("marca").value = "";
    document.getElementById("tipo").value = "";
    document.getElementById("presentacion").value = "";
    document.getElementById("precio_venta").value = "";
    document.getElementById("stock_actual").value = "";

}


async function editarProducto(id) {
    const response = await fetch(`${API_URL}/${id}`);

    if (!response.ok) {
        alert("No se pudo obtener el producto");
        return;
    }

    const producto = await response.json();

    document.getElementById("edit_producto_id").value = producto.id;
    document.getElementById("edit_nombre").value = producto.nombre;
    document.getElementById("edit_marca").value = producto.marca;
    document.getElementById("edit_tipo").value = producto.tipo;
    document.getElementById("edit_presentacion").value = producto.presentacion;
    document.getElementById("edit_precio_venta").value = producto.precio_venta;
    document.getElementById("edit_stock_actual").value = producto.stock_actual;

    const modal = new bootstrap.Modal(
        document.getElementById("modalEditarProducto")
    );

    modal.show();
}

async function actualizarProducto() {
    const id = document.getElementById("edit_producto_id").value;

    const producto = {
        nombre: document.getElementById("edit_nombre").value,
        marca: document.getElementById("edit_marca").value,
        tipo: document.getElementById("edit_tipo").value,
        presentacion: document.getElementById("edit_presentacion").value,
        precio_venta: parseFloat(document.getElementById("edit_precio_venta").value),
        stock_actual: parseInt(document.getElementById("edit_stock_actual").value)
    };

    await fetch(`${API_URL}/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(producto)
    });

    bootstrap.Modal.getInstance(
        document.getElementById("modalEditarProducto")
    ).hide();

    cargarProductos();
}