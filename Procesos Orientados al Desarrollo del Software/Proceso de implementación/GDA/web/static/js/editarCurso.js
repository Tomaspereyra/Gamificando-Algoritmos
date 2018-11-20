$(document).ready(function(){
  	console.log("Doc Ready");
    $('.sidenav').sidenav();
	$(".dropdown-trigger").dropdown({ hover: false });

	$("#actualizarCurso").on("click", function() {

	    actualizarCurso();

	})

})

