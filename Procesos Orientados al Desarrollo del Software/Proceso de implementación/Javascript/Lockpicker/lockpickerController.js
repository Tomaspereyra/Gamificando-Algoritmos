//Event handlers
//http://boards.4chan.org/soc/thread/27485406/did-you-ever-meet-irl-with-someone-you-met-on
$( document ).ready(function() {
	$("#play-button" ).click(function() {
		if (animating == false){
			Blockly.JavaScript.addReservedWords('code');
			var code = Blockly.JavaScript.workspaceToCode(workspace);
			PlayOrders(code);
		}
	});   
	$("#reset-button" ).click(function() {
		Reset();
	});  
	$("#set-map-string-button" ).click(function() {
		var mapString = prompt("Por favor, ingrese el codigo del mapa", "");
		if (mapString != null)
			SetNewMap(mapString);
		
	});
	CreateTestLock();
});
///*** INIT DATA ***///
	
var gameScene = new Phaser.Scene('MazeScene');

var config = {
	type: Phaser.AUTO,
	width: 512,
	height: 512,
	parent: 'phaser-div',
	scene: gameScene
};

var game = new Phaser.Game(config);

///*** FIN INIT  DATA ***///

var currentLock;
var currentLockpick = new Lockpick();
var currentIterations;

var animating = false;
var digitsAnimated = 0;

//Phaser Scene Functions

gameScene.preload = function () {
	console.log("Preload()...");
	//Cargamos los sprites (Imagenes)
	/*this.load.image ('Floor', 'Assets/Floor.png');
	this.load.image ('Wall', 'Assets/Wall.png');
	this.load.image ('Start', 'Assets/Start.png');
	this.load.image ('Exit', 'Assets/Exit.png');
	this.load.image ('Player', 'Assets/Beholder.png');
	this.load.spritesheet('explosion', 'Assets/FireExplosion.png', {frameWidth: 32, frameHeight: 32});*/
	
}

gameScene.create = function () {    
	console.log("gameScene.create()...");
	CreateTestLock();
	//StartMap(CreateTestMap());
	//StartMap(CreateTestMap2());
}


gameScene.update = function() {
	if (animating){
		if (!FinishedAnimating()){
			currentPlayerActions.Update();
		} else {
			FinishAnimation();
			if (TryToOpen()){
				alert("Felicidades! Resolviste el acertijo!")
			} else {
				alert("Lo siento, no lograste resolver el laberinto!")
			}
			Reset();
		}
	}
}

function StartGame(lock){
	currentLock = lock;
	console.log("Lock : " + lock);
	this.Reset();
	
}

function Reset(){
	currentLockpick = new Lockpick();
}

//Action functions (Delegate to current player ones)

function SetCurrentDigit(x){
	currentLockpick.SetCurrentValue(x);
}

function GetCurrentDigit(){
	return currentLockpick.GetCurrentValue(x);
}

function MultiplyCurrentDigit(x){
	SetCurrentDigit(GetCurrentDigit() * x);
}

function AddToCurrentDigit(x){
	SetCurrentDigit(GetCurrentDigit() + x);
}

function SubtractFromCurrentDigit(x){
	SetCurrentDigit(GetCurrentDigit() - x);
}

function DivideCurrentDigit(x){
	SetCurrentDigit(GetCurrentDigit() / x);
}

function GetInputCount(){
	return currentLockpick.InputSize();
}

function InputCurrentValue(){
	currentLockpick.InputCurrentValue();
}

function Reset(){
	currentLockpick.Reset();
}

function TryToOpen(){
	return currentLockpick.TryToOpen(currentLock);
}

function LockpickIsFull(){
	return (currentLockpick.InputSize() == currentLock.PasswordSize());
}

function FinishedInputting(){
	return (LockpickIsFull() || HitIterationsCap());
}

function HitIterationsCap() {
	return (currentIterations > MAX_ITERATIONS);
}

function PlayOrders(orderString){
	console.log("Orders : \n" + orderString);
	
	eval(orderString);
	
	if (HitIterationsCap()){
		alert("El algoritmo provoca un ciclo infinito.")
		Reset();
	} else {
		StartAnimating();
	}
}

function StartAnimating(){
	animating = true;
	digitsAnimated = 0;
}

function FinishedAnimating(){
	return (digitsAnimated == currentLock.PasswordSize());
}

function FinishAnimation(){
	animating = false;
	digitsAnimated = 0;
}

//Testing

function CreateTestLock(){

	var lock = new Lock([1, 2, 3, 4]);
	StartGame (lock);
}

