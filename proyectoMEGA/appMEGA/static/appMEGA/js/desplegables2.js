/*(function($) {
  'use strict';

  $(document).ready(function() {
    // Obtener referencias a los campos
    var tipoContratoField = $('#id_fk_Liquidacionenc_Tipocontrato');
    var propiedadContratoField = $('select[name="fk_Liquidacionenc_Propiedadcontratoalquiler"]');
    var contratosField = $('select[name="fk_Liquidacionenc_Contratos"]');

    // Ocultar los campos adicionales al cargar la página
    propiedadContratoField.hide();
    contratosField.hide();

    // Mostrar u ocultar los campos adicionales según el valor seleccionado en tipoContratoField
    tipoContratoField.change(function() {
      var selectedValue = tipoContratoField.find('option:selected').text();
      if (selectedValue === 'ALQUILER') {
        propiedadContratoField.show();
        contratosField.hide();
      } else if (selectedValue === 'ADMINISTRACIÓN') {
        propiedadContratoField.hide();
        contratosField.show();
      } else {
        propiedadContratoField.hide();
        contratosField.hide();
      }
    });
  });
})(django.jQuery);
;*/
