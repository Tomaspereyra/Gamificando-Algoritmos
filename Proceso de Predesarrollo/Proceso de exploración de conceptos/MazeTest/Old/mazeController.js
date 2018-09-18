//Event handlers
$( document ).ready(function() {
	$("#play-button" ).click(function() {
		Blockly.JavaScript.addReservedWords('code');
		var code = Blockly.JavaScript.workspaceToCode(workspace);
		PlayOrders(code);
	});   
	$("#reset-button" ).click(function() {
		RestartMap();
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
	this.load.image ('Floor', 'Assets/Floor.png');
	this.load.image ('Wall', 'Assets/Wall.png');
	this.load.image ('Start', 'Assets/Start.png');
	this.load.image ('Exit', 'Assets/Exit.png');
	this.load.image ('Player', 'Assets/Beholder.png');
	
}

gameScene.create = function () {    
	console.log("create()...");
	StartMap(CreateTestMap());
	//PlayOrders("MoveForward();SpinLeft();SpinRight();MoveForward();")
}

gameScene.update = function() {
	if (currentPlayerActions != null){
		if (!currentPlayerActions.finished){
			currentPlayerActions.Update();
			console.log("Updating Actions!");
		} else {
			console.log("Player Actions Finished Rendering!");
		}
	}
}

function RestartMap(){
	currentPlayer.Reset();
	currentPlayer.Draw();
	currentPlayerActions.finished = true;
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


function PlayOrders(orderString){
	currentPlayerActions = currentPlayer.PlayOrders(orderString);
	currentPlayerActions.Start();
}

//Testing

function CreateTestMap(){

	var map = new MazeMap(16, 16, S);
	map.FromString("1111111111111111/1111111111111111/1111111111111111/1113001111111111/1111101111111111/1111101111111111/1112001111111111/1111111111111111/1111111111111111/1111111111111111/1111111111111111/1111111111111111/1111111111111111/1111111111111111/1111111111111111/1111111111111111");
	return map;

}