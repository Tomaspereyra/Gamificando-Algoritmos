//Event handlers
$( document ).ready(function() {
	$("#play-button" ).click(function() {
		if (currentPlayerActions == null){
			Blockly.JavaScript.addReservedWords('code');
			var code = Blockly.JavaScript.workspaceToCode(workspace);
			PlayOrders(code);
		}
	});   
	$("#reset-button" ).click(function() {
		RestartMap();
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

var currentPlayer;
var currentMap;
var currentPlayerActions;

//Phaser Scene Functions

gameScene.preload = function () {
	console.log("Preload()...");
	//Cargamos los sprites (Imagenes)
	/*
	this.load.image ('Floor', {{ url_for('static', filename='Assets/Floor.png') }});
	this.load.image ('Wall', {{ url_for('static', filename='Assets/Wall.png') }});
	this.load.image ('Start', {{ url_for('static', filename='Assets/Start.png') }});
	this.load.image ('Exit', {{ url_for('static', filename='Assets/Exit.png') }});
	this.load.image ('Player', {{ url_for('static', filename='Assets/Beholder.png') }});
	*/
    var resourcesPath = $("#resources_path").val();
    console.log("Resources Path : " + resourcesPath)
	this.load.image ('Floor', resourcesPath + 'Assets/Floor.png');
	this.load.image ('Wall', resourcesPath + 'Assets/Wall.png');
	this.load.image ('Start', resourcesPath + 'Assets/Start.png');
	this.load.image ('Exit', resourcesPath + 'Assets/Exit.png');
	this.load.image ('Player', resourcesPath + 'Assets/Beholder.png');

	//this.load.spritesheet('explosion', {{ url_for('static', filename='Assets/FireExplosion.png') }}, {frameWidth: 32, frameHeight: 32});
	this.load.spritesheet('explosion', resourcesPath + 'Assets/FireExplosion.png', {frameWidth: 32, frameHeight: 32});
	
}

gameScene.create = function () {    
	console.log("create()...");
	//StartMap(CreateTestMap());
	StartMap(CreateTestMap2());
	this.anims.create({
        key: 'explosion',
        frames: this.anims.generateFrameNumbers('explosion'),
        frameRate: 10,
        repeat: -1
    });
}


gameScene.update = function() {
	if (currentPlayerActions != null){
		if (!currentPlayerActions.finished){
			currentPlayerActions.Update();
			console.log("Updating Actions!");
		} else {
			console.log("Player Actions Finished Rendering!");
			if (currentPlayer.IsOnExit()){
				alert("Felicidades! Resolviste el laberinto!")
			} else {
				alert("Lo siento, no lograste resolver el laberinto!")
			}
			RestartMap();
		}
	}
}

function SetNewMap (mapString){
	
	var map = new MazeMap(16, 16, 0);
	map.FromString(mapString);
	if (map.valid){
		StartMap(map);
		RestartMap();
	} else {
		alert("Mapa ingresado invalido!")
	}
	
}

function RestartMap(){
	currentPlayerActions = null;
	currentPlayer.Reset();
	currentPlayer.Draw();
	
}

function StartMap(map){
	currentMap = map;
	currentPlayer = new Player(map, gameScene)
	currentMap.Draw(gameScene);
	currentPlayer.Draw();
	
	console.log(game);
}

//Action functions (Delegate to current player ones)

function SpinLeft(){
	currentPlayer.SpinLeft();
}

function SpinRight(){
	currentPlayer.SpinRight();
}

function MoveForward(){
	currentPlayer.MoveForward();
}

function IsWallAhead(){
	return currentPlayer.IsWallAhead();
}

function IsPathAhead(){
	return currentPlayer.IsPathAhead();
}

function IsHoleAhead(){
	return currentPlayer.IsHoleAhead();
}

function NotFinished(){
	return currentPlayer.NotFinished();
}

function PlayOrders(orderString){
	console.log("Orders : \n" + orderString);
	currentPlayerActions = currentPlayer.PlayOrders(orderString);
	if (currentPlayerActions.HitActionCap()){
		alert("El algoritmo provoca un ciclo infinito.")
		RestartMap();
	} else {
		currentPlayerActions.Start();	
	}
}

//Testing

function CreateTestMap2(){

	var map = new MazeMap(16, 16, S);
	map.FromString("0000000000000000/0000000000000000/0000000000000000/0000000000000000/0000000000000000/0000200000000000/0000000000000000/0000300000000000/0000000000000000/0000000000000000/0000000000000000/0000000000000000/0000000000000000/0000000000000000/0000000000000000/0000000000000000");
	return map;

}



function CreateTestMap(){

	var map = new MazeMap(16, 16, S);
	map.FromString("1111111111111111/1111111111111111/1111111111111111/1113001111111111/1111101111111111/1111101111111111/1112001111111111/1111111111111111/1111111111111111/1111111111111111/1111111111111111/1111111111111111/1111111111111111/1111111111111111/1111111111111111/1111111111111111");
	return map;

}