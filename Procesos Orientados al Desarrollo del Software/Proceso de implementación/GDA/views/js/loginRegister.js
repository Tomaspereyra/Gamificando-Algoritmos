$(document).ready(function(){
	//INIT
	init();
	//EVENTOS
	$("#login" ).click(function() {
        tryLogin();
    });   
    $("#registrarse" ).click(function() {
        tryRegister();
    });
});   

function tryLogin(){
	if (validateLoginInfo()){
		var username_ = $("#usernameLogin").val();
		var password_ = $("#passwordLogin").val();
		var data = {
			username : username_,
			password : password_
		};
		console.log("tryLogin() : " + JSON.stringify(data));
		$.ajax({
			url: "http://localhost:5000/auth/login",
			context: document.body,
			data : data
		}).done(doneLogin);
	}
}

function validateLoginInfo(){
	var username_ = $("#usernameLogin").val();
	var password_ = $("#passwordLogin").val();
	if (username_ == null || username_ == ""){
		showError({errorText : "Ingrese su nombre de usuario"});
		return false;
	}
	if (username_ == null || password_ == ""){
		showError({errorText : "Ingrese su contraseña"});
		return false;
	}
	
	return true;
}

function showError(data){
	alert("Se encontro un error al enviar la solicitud :\n" + data.errorText);
}

function doneLogin(data){
	if (data.error != null){
		showError(data);
	} else {
		alert("Usted se ha registrado con exito!");
	}
}

function tryRegister(){
	var username_ = $("#usernameLogin").val();
	var password_ = $("#passwordLogin").val();
	var email_ = $("#email").val();
	var nombre_ = $("#nombre").val();
	var apellido_ = $("#apellido").val();
	var fechaNacimiento_ = $("#fechaNacimiento").val();
	
	var data = {
			username : username_,
			password : password_,
			email : email_,
			nombre : nombre_,
			apellido : apellido_,
			fechaNacimiento : fechaNacimiento_
		};
	console.log("tryRegister() : " + JSON.stringify(data));
	$.ajax({
		url: "http://localhost:5000/auth/register",
		context: document.body,
		data : data
	}).done(doneLogin);
	
}

function init(){
	
	//$('.tabs').tabs({ 'swipeable': true });
	$('.tabs').tabs();
	document.addEventListener('DOMContentLoaded', function() {
	var elems = document.querySelectorAll('.datepicker');
	var instances = M.Datepicker.init(elems, {format : "dd-mm-yyyy"});
	
	// TAB Color
	$(".tabs" ).css("background-color", "white");

	// TAB Indicator/Underline Color
	$(".tabs>.indicator").css("background-color", 'blue');

	// TAB Text Color
	$(".tabs>li>a").css("color", 'black');
	});

	// Or with jQuery

	$(document).ready(function(){
		$('.datepicker').datepicker({format : "dd-mm-yyyy"});
	});
	
}