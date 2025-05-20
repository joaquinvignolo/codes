let pantalla = document.getElementById('pantalla');

function agregar(valor) {
  if (pantalla.value === 'Error' || pantalla.value === 'undefined') {
    pantalla.value = '';
  }
  const operadores = ['+', '-', '×', '÷'];
  const ultimo = pantalla.value.slice(-1);

  // Permitir "-" al inicio para negativos
  if (pantalla.value === '' && valor === '-') {
    pantalla.value = '-';
    return;
  }

  // Evitar otros operadores al inicio
  if (pantalla.value === '' && operadores.includes(valor) && valor !== '-') {
    return;
  }

  // Permitir una resta después de un operador (para negativos)
  if (
    operadores.includes(ultimo) &&
    valor === '-' &&
    ultimo !== '-'
  ) {
    pantalla.value += valor;
    return;
  }

  // Evitar dos operadores seguidos (excepto el caso anterior)
  if (
    operadores.includes(valor) &&
    operadores.includes(ultimo)
  ) {
    return;
  }

  // Evitar más de un punto en el mismo número
  if (valor === '.') {
    let partes = pantalla.value.split(/[\+\-\×\÷]/);
    let ultimaParte = partes[partes.length - 1];
    if (ultimaParte.includes('.')) {
      return;
    }
    if (pantalla.value === '') {
      pantalla.value = '0';
    }
  }

  // Cambia * por × y / por ÷ para mostrar en pantalla
  if (valor === '*') valor = '×';
  if (valor === '/') valor = '÷';

  pantalla.value += valor;
}

function limpiar() {
  pantalla.value = '';
}

function calcular() {
  try {
    // Reemplaza los símbolos visuales por los operadores reales
    let expresion = pantalla.value.replace(/÷/g, '/').replace(/×/g, '*');
    const operadores = ['+', '-', '*', '/'];
    if (
      expresion === '' ||
      operadores.includes(expresion.slice(-1))
    ) {
      return;
    }
    let resultado = eval(expresion);
    if (resultado === undefined || isNaN(resultado) || !isFinite(resultado)) {
      pantalla.value = 'Error';
    } else {
      // Limita a 8 decimales y elimina ceros innecesarios
      if (typeof resultado === 'number' && !Number.isInteger(resultado)) {
        pantalla.value = parseFloat(resultado.toFixed(8)).toString();
      } else {
        pantalla.value = resultado;
      }
    }
  } catch (e) {
    pantalla.value = 'Error';
  }
}

function retroceso() {
  if (pantalla.value === 'Error' || pantalla.value === 'undefined') {
    return;
  }
  pantalla.value = pantalla.value.slice(0, -1);
}
