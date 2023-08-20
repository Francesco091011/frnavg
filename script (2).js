function VerificarClave() {
    if (document.getElementById("ingreso").value=="valery") {
        document.getElementById("mensaje").innerHTML="Password correcta.";
        // <img src="../static/Blue.jpg" alt="Easter Egg N.° 01" width="500">
    }
    else {
        document.getElementById("mensaje").innerHTML="Password incorrecta."
    }
}

// Easter Egg N.° 01