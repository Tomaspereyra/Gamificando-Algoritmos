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

var MAX_ITERATIONS = 1000;


var currentLock;
var currentLockpick = new Lockpick();
var currentIterations;

var animating = false;
var digitsAnimated = 0;

//Phaser Scene Functions

var lockpickTitle;
var lockpickText;
var lockpickUnderscores;
var lockTitle;
var lockText;
var lockUnderscores;

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
	
	lockTitle = this.add.text(256, 64, 'Cerrojo a Abrir:', { fontFamily: 'pixelartFont', fontSize: '32px', fill: '#FFFFFF' });
	lockTitle.setOrigin(0.5, 0.5);
	lockText = this.add.text(256, 128, '1 2 3 4 5 ', { fontFamily: 'pixelartFont', fontSize: '96px', fill: '#FFFFFF' });
	lockText.setOrigin(0.5,0.5);
	lockUnderscores = this.add.text(256, 128, '_ _ _ _ _', { fontFamily: 'pixelartFont', fontSize: '96px', fill: '#FFFFFF' });
	lockUnderscores.setOrigin(0.5,0.5);
	lockpickTitle = this.add.text(256, 128*3 - 96, 'Tu Ganzúa:', { fontFamily: 'pixelartFont', fontSize: '32px', fill: '#FFFFFF' });
	lockpickTitle.setOrigin(0.5, 0.5);
	lockpickText = this.add.text(256, 128 * 3, '1 _ _ _ _', { fontFamily: 'pixelartFont', fontSize: '96px', fill: '#FFFFFF' });
	lockpickText.setOrigin(0.5,0.5);
	lockpickUnderscores = this.add.text(256, 128 * 3, '_ _ _ _ _', { fontFamily: 'pixelartFont', fontSize: '96px', fill: '#FFFFFF' });
	lockpickUnderscores.setOrigin(0.5,0.5);
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
	PrintCurrentLock();
	Reset();
}

function Reset(){
	currentLockpick = new Lockpick();
	this.PrintCurrentLockpick();
}

//Action functions (Delegate to current player ones)

function PrintCurrentLock(){
	PrintLock(currentLock);
}

function PrintLock(lock){
	lockText.setText(lock.GetDigit(0) + " " + lock.GetDigit(1) + " " + lock.GetDigit(2) + " " + lock.GetDigit(3) + " " + lock.GetDigit(4));
}

function PrintCurrentLockpick(){
	PrintLockpick(currentLockpick);
}

function PrintLockpick(lockpick){
	var lockpickNewText = "";
	lockpickNewText += lockpick.GetDigit(0);
	for (var i = 1; i < lockpick.InputSize(); i++){
		 lockpickNewText += " " + lockpick.GetDigit(i);
	}
	lockpickText.setText(lockpickNewText);
}

function SetCurrentDigit(x){
	currentLockpick.SetCurrentValue(x);
}

function GetCurrentDigit(){
	return currentLockpick.GetCurrentValue();
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

function InputCurrentDigit(){
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
	currentIterations++;
	return (currentIterations >= MAX_ITERATIONS);
}

function PlayOrders(orderString){
	console.log("Orders : \n" + orderString);
	currentIterations = 0;
	eval(orderString);
	console.log("Lockpick : " + currentLockpick.input);
	if (HitIterationsCap()){
		alert("El algoritmo provoca un ciclo infinito.")
		Reset();
	} else {
		StartAnimating();
	}
}

function StartAnimating(){
	PrintCurrentLockpick();
	animating = true;
	digitsAnimated = 0;
	FinishAnimation();
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

	var lock = new Lock([1, 2, 3, 4, 5]);
	StartGame (lock);
}

