<?php

$nombre= $_POST['name'];
$email = $_POST['email'];
$pais_origen = $_POST['pais_origen'];

$mensaje = "Este mensaje fue enviado por: " . $nombre . ",/r/n";
$mensaje = "Su email es: " . $email . ",/r/n";
$mensaje = "Su país de origen es: " . $pais_origen . ",/r/n";
$mensaje = "Enviado el " . date('d/m/Y', time());

$para = "cosasdelfutbol.09@gmail.com"

mail($para, utf8_decode($mensaje), $header);

header('Location:exito.html');

?>