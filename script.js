function VerificarClave() {
    if (document.getElementById("ingreso").value=="5678") {
        document.getElementById("caja1").style.backgroundImage="url ('../static/Blue.png')"
    }
    else {
        document.getElementById("mensaje1").innerHTML="Error en imágen JPG."
    }
}
function VerificarClave() {
    if (document.getElementById("ingreso").value=="5678") {
        document.getElementById("mensaje").innerHTML="Password correcta"
    }
    else {
        document.getElementById("mensaje").innerHTML="Password incorrecta"
    }
}
