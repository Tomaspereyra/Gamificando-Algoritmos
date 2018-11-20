$(document).ready(function(){
  	console.log("Doc Ready");
    $('.sidenav').sidenav();
	$(".dropdown-trigger").dropdown({ hover: false });

	$("#actualizarCurso").on("click", function() {

	    actualizarCurso();

	})

})

function actualizarCurso(){

    var idCurso = $("#idCurso").val();
    var nombre = $("#nombre").val();
    var desc = $("#descripcion").val();
    //var hint = $("#hint").val();
    var sePuedeSaltear = $("#sePuedeSaltear").val();
    //var cantMaxBloques = $("#cantMaxBloques").val();

    //"&hint=" + hint +
    //console.log("actualizarCurso() : " + JSON.stringify(data));
    $.ajax({
        url: "http://localhost:5000/cursos/guardarInfoCurso?idCurso=" +
            idCurso + "&nombre=" + nombre + "&descripcion=" + desc  + "&sePuedeSaltear=" + sePuedeSaltear,
        type : "POST"

    }).always(function(data){
        afterActualizar(data);
    })

}

function afterActualizar(data){
    if (data.errorText != null){
        alert(errorText);
    } else {
        alert ("Datos guardados con exito!");
    }
}

