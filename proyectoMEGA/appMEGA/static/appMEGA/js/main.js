
function agregarFila(boton) {
  console.log('Agregando nueva fila con botón:', boton);
  var contador = boton.dataset.contador;
  var tablaId = boton.dataset.tablaId;
  var tablaBody = document.getElementById('tabla-body-' + tablaId);

  var newRow = document.createElement('tr');
  newRow.innerHTML = `
    <td></td>
    <td class="concepto" data-objeto-id="${tablaId}"><input type="text" class="editable-input input-concepto" name="concepto"></td>
    <td class="monto-1"><input type="text" class="editable-input input-suma" oninput="calcularSuma(this)" name="monto-1"></td>
    <td class="monto-2"><input type="text" class="editable-input input-suma" oninput="calcularSuma(this)" name="monto-2"></td>
    <td class="monto-3"><input type="text" class="editable-input input-suma" oninput="calcularSuma(this)" name="monto-3"></td>
    <td class="suma-celda"></td>
  `;
}

// Event listener para los botones con clase ".boton-agregar"
var botonesAgregar = document.querySelectorAll('.boton-agregar');
botonesAgregar.forEach(function(boton) {
  boton.addEventListener('click', function() {
    agregarFila(this);
  });
});




