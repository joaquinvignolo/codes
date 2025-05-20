let pantalla = document.getElementById('pantalla');

function agregar(valor) {
  pantalla.value += valor;
}

function limpiar() {
  pantalla.value = '';
}

function calcular() {
  try {
    pantalla.value = eval(pantalla.value);
  } catch (e) {
    pantalla.value = 'Error';
  }
}
