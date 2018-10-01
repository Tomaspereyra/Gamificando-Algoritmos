//MAP

var FLOOR = 0;
var WALL = 1;
var START = 2
var EXIT = 3;
var SPRITE_SIZE = 32;
var PIVOT_OFFSET = (SPRITE_SIZE / 2);

function MazeMap (width, height, defaultOrientation) {
	this.height = height;
	this.width = width;
	this.defaultOrientation = defaultOrientation;
	console.log("Constructor : [" + width + "," + height + "]");
	this.tiles = new Array(width);
	for (var i = 0; i < width; i++) {
		this.tiles[i] = new Array(height);
	}
}
	
MazeMap.prototype.FromString = function (str){
	rows = str.split("/");
	console.log("Length : " + rows.length);
	for (var row = 0; row < this.height; row++){	
		for (var col = 0; col < this.width; col++){
			//console.log("FromString : Row,col = [" + row + "," + col + "]");
			this.tiles[row][col] = parseInt(rows[row][col]);
		}
	}
	console.log(this.tiles);
}

MazeMap.prototype.IndexToSprite = function(index){
	var result;
	if (index == FLOOR){
		result = 'Floor';
	} else if (index == WALL){
		result = 'Wall';
	} else if (index == START){
		result = 'Start';
	} else if (index == EXIT){
		result = 'Exit';
	} else {
		console.log("ERROR : IndexToSprite() : index " + index + " Is not valid!");
	}
	return result;
	
}

MazeMap.prototype.GetStart = function (){
	for (var row = 0; row < this.height; row++){
		for (var col = 0; col < this.width; col++){
			//console.log(this.tiles[row][col]);
			if (this.tiles[row][col] == START)
				return [row, col];
		}
	}
	return [0][0];
}

MazeMap.prototype.Draw = function(scene){
	var sprite;
	for (var row = 0; row < this.height; row++){
		for (var col = 0; col < this.width; col++){
			//console.log("Drawing : Row,col = [" + row + "," + col + "] -> " + this.tiles[row][col]);
			sprite = scene.add.sprite((SPRITE_SIZE * row), (SPRITE_SIZE * col), this.IndexToSprite(this.tiles[row][col]));
			sprite.setOrigin(0, 0);
		}
	}
}

///PLAYER
//Orientations
var N = 0;
var E = 1;
var S = 2;
var W = 3;
var LEFT = 0;
var RIGHT = 1;


function Player(map, gameScene){
	var startPos = map.GetStart();
	this.x = startPos[0];
	this.y = startPos[1];
	this.sprite = null;
	this.map = map;
	this.SetOrientation(map.defaultOrientation);
	this.actions = null;
	this.gameScene = gameScene;
}

Player.prototype.Place = function(x, y){
	this.x = x;
	this.y = y;
}

Player.prototype.IsAlive = function(){
	return !this.map.tiles[this.x][this.y].IsWall();
}
	
Player.prototype.GetCanvasX = function(){
	return (SPRITE_SIZE * this.x) + PIVOT_OFFSET;
}

Player.prototype.GetCanvasY = function(){
	return (SPRITE_SIZE * this.y) + PIVOT_OFFSET;
}
	
Player.prototype.Reset = function(){
	pos = this.map.GetStart();
	this.Place(pos[0], pos[1]);
	this.SetOrientation(this.map.defaultOrientation);
}

Player.prototype.SetOrientation = function(orientation){
	this.orientation = orientation;
	//this.UpdateSpriteOrientation();
}

Player.prototype.UpdateSpriteOrientation = function(){
	if (this.sprite != null)
		this.sprite.angle = this.AngleFromOrientation(this.orientation);
}	
	
Player.prototype.AngleFromOrientation = function(orientation){
	var angle = 0;
	if (orientation == N){
		angle = 180;
	} else if (orientation == S){
		angle = 0;
	} else if (orientation == E){
		angle = 270;
	} else if (orientation == W){
		angle = 90;
	} else {
		console.log("INVALID ORIENTATION " + orientation);
	}
	return angle;
}	
	
Player.prototype.Draw = function(){
	if (this.sprite == null){
		this.sprite = this.gameScene.add.sprite(this.GetCanvasX(), this.GetCanvasY(), 'Player');
	} else {
		this.sprite.x = this.GetCanvasX();
		this.sprite.y = this.GetCanvasY();
	}
	this.UpdateSpriteOrientation();
}

Player.prototype.PlayOrders = function(orderString){
	this.actions = new PlayerActions(this);
	eval(orderString);
	return this.actions;
}

Player.prototype.MoveForward = function(){
	//console.log(gameScene.game);
	
	if (this.orientation == N){
		this.y++;
	} else if (this.orientation == S){
		this.y--;
	} else if (this.orientation == E){
		this.x++;
	} else if (this.orientation == W){
		this.x--;
	}
	
	this.actions.EnqueueAction(new MoveForwardAction(this.orientation));
}

Player.prototype.SpinRight = function(){
	//console.log(gameScene.game);
	
	this.orientation++;
	
	if (this.orientation > W)
		this.orientation = N;
	
	this.actions.EnqueueAction(new SpinAction(RIGHT));
}

Player.prototype.SpinLeft = function(){
	this.orientation--;
	if (this.orientation < N)
		this.orientation = W;
	
	this.actions.EnqueueAction(new SpinAction(LEFT));
}

//PLAYER ACTIONS

function PlayerActions(player){
	this.finished = false;
	this.pendingActions = [];
	this.player = player;
}	

PlayerActions.prototype.EnqueueAction = function(action){
	action.player = this.player;
	this.pendingActions.push(action);
}

PlayerActions.prototype.GoToNextAction = function(){
	if (this.pendingActions.length == 0)
		this.currentAction = null;
	else
		this.currentAction = this.pendingActions.shift();
}

PlayerActions.prototype.Start = function(){
	this.finished = false;
	this.GoToNextAction();
}

PlayerActions.prototype.Update = function(){
	if (this.currentAction != null){
		if (this.currentAction.finished){
			this.GoToNextAction();
		} else {
			this.currentAction.Update();
		}
	} else {
		this.finished = true;
	}
}

//ACTIONS

function SpinAction(direction){
	
	if (direction == RIGHT)
		this.step = 1;
	else
		this.step = -1;
	this.speed = 2;
	this.player = null;
	this.degreesRotated = 0;
	this.finished = false;
}
	
SpinAction.prototype.Update = function(){
	var rotation = this.step * this.speed;
	this.player.sprite.angle += rotation;
	this.degreesRotated += Math.abs(rotation);
	if (this.degreesRotated >= 90)
		this.finished = true;
	
}

function MoveForwardAction (direction){
	
	
	if (direction == N){
		this.xStep = 0;
		this.yStep = -1;
	} else if (direction == S){
		this.xStep = 0;
		this.yStep = 1;
	} else if (direction == E){
		this.xStep = 1;
		this.yStep = 0;
	} else if (direction == W){
		this.xStep = -1;
		this.yStep = 0;
	}

	this.speed = 1;
	this.player = null;
	this.distanceCovered = 0;
	this.finished = false;
	
	console.log("new MoveForwardAction. Direction : " + direction);
	
}

MoveForwardAction.prototype.Update = function(){
	this.player.sprite.x += this.speed * this.xStep;
	this.player.sprite.y += this.speed * this.yStep;
	this.distanceCovered += this.speed;
	if (this.distanceCovered >= 32)
		this.finished = true;
	
}