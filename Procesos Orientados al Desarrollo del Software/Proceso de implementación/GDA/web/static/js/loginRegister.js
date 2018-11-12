var HOME_PATH = "http://localhost:5050//home";

$(document).ready(function(){
	//INIT
	init();
	//EVENTOS
	$("#login" ).click(function() {
        //tryLogin();
    });   
    $("#registrarse" ).click(function() {
        //tryRegister();
    });
    var form = $('#MyForm');
});   

function validateLoginForm(e){
    if (!validateLoginInfo())
        e.preventDefault();
}

function validateRegisterForm(e){
    if (!validateRegisterInfo())
        e.preventDefault();
}

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
			url: "http://localhost:5000/auth/login?username=" + username_ + "&password=" + password_,
			type : "POST",
			datatype: "json",
			success: function(data) {

            }
		})
		
	}
}

function IsJSON(str) {
    try {
        JSON.parse(str);
    } catch (e) {
        return false;
    }
    return true;
}

function getLoginUsername(){
    return $("#usernameLogin").val();
}

function getLoginPassword(){

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
        console.log("Redirecting...");
        //window.location.replace(HOME_PATH + "?username=" + );
    }
}

function tryRegister(){
	var username_ = $("#usernameRegister").val();
	var password_ = $("#passwordRegister").val();
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
		url: "http://localhost:5000/auth/register?username=" + username_ + "&password=" + password_ + "&email=" + email_ +
		"&nombre=" + nombre_ + "&apellido=" + apellido_ + "&fechaNacimiento=" + fechaNacimiento_,
		type : "POST",
		dataType : "json"
	}).always(function (data){
		console.log("Done Registering. Data Received : " + JSON.stringify(data));
		doneRegister(data);
	});
	
}

function doneRegister(data){
	if (data.error != null){
		showError(data);
	} else {
		alert("Usted se ha registrado con exito!");
	}
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