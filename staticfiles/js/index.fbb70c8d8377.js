const textElement = document.getElementById("text");
const texts = ["¡LEARNING ENGLISH!", "¡APRENDE INGLES!"];
let textIndex = 0;
let charIndex = 0;

function type() {
  if (charIndex < texts[textIndex].length) {
    textElement.textContent += texts[textIndex].charAt(charIndex);
    charIndex++;
    setTimeout(type, 100); // Velocidad de escritura de teypiado
  } else {
    setTimeout(erase, 1500); // Tiempo antes de borrar lo teypiado
  }
}

function erase() {
  if (charIndex > 0) {
    textElement.textContent = texts[textIndex].substring(0, charIndex - 1);
    charIndex--;
    setTimeout(erase, 50); // Velocidad de borrado
  } else {
    textIndex = (textIndex + 1) % texts.length;
    setTimeout(type, 500); // Tiempo antes de comenzar la siguiente escritura
  }
}

type();







