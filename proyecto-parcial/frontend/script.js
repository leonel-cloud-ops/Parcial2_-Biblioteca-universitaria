/**
 * Muestra un mensaje en pantalla al seleccionar un material para préstamo.
 * @param {string} titulo - Nombre del recurso seleccionado.
 * @param {string} tipo - Tipo de recurso (Libro o Revista).
 * @param {number} dias - Días autorizados para el préstamo.
 */
function solicitarPrestamo(titulo, tipo, dias) {
    const contenedor = document.getElementById('mensaje-contenedor');

    contenedor.classList.remove('hidden');

    contenedor.innerHTML = `
        <strong>Solicitud procesada:</strong> Has seleccionado el recurso 
        <em>"${titulo}"</em> (${tipo}). <br> 
        <strong>Período máximo de préstamo autorizado:</strong> ${dias} días.
    `;

    contenedor.scrollIntoView({ behavior: 'smooth', block: 'end' });
}