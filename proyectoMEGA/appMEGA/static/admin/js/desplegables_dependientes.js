(function() {
  'use strict';

  document.addEventListener('DOMContentLoaded', function() {
    // Obtener la lista desplegable de tipo de contrato
    var tipoContratoDropdown = document.querySelector('select[name="fk_Liquidacionenc_Tipocontrato"]');
    
    // Obtener la referencia a los campos adicionales
    var propiedadContratoField = document.querySelector('select[name="fk_Liquidacionenc_Propiedadcontratoalquiler"]');
    var contratosField = document.querySelector('select[name="fk_Liquidacionenc_Contratos"]');

    // Obtener el valor seleccionado de la lista desplegable
    var tipoContratoSelectedText = tipoContratoDropdown.options[tipoContratoDropdown.selectedIndex].text;

    
    // Ocultar los campos adicionales al cargar la página
    propiedadContratoField.style.display = 'none';
    contratosField.style.display = 'none';

    // Controlador de eventos para el cambio de selección en la lista desplegable
    tipoContratoDropdown.addEventListener('change', function() {
      // Obtener el nuevo valor seleccionado
      var nuevoTipoContratoSelectedText = tipoContratoDropdown.options[tipoContratoDropdown.selectedIndex].text;

      // Mostrar u ocultar los campos adicionales según el nuevo valor seleccionado
      if (nuevoTipoContratoSelectedText === 'ALQUILER') {
        propiedadContratoField.style.display = 'block';
        contratosField.style.display = 'none';
      } else if (nuevoTipoContratoSelectedText === 'ADMINISTRACIÓN') {
        propiedadContratoField.style.display = 'none';
        contratosField.style.display = 'block';
      } else {
        propiedadContratoField.style.display = 'none';
        contratosField.style.display = 'none';
      }
    });

    // Mostrar u ocultar los campos adicionales según el valor seleccionado al cargar la página
    if (tipoContratoSelectedText === 'ALQUILER') {
      propiedadContratoField.style.display = 'block';
      contratosField.style.display = 'none';
    } else if (tipoContratoSelectedText === 'ADMINISTRACIÓN') {
      propiedadContratoField.style.display = 'none';
      contratosField.style.display = 'block';
    } else {
      propiedadContratoField.style.display = 'none';
      contratosField.style.display = 'none';
    }
  });
})();
