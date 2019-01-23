//MAP

var FLOOR = 0;
var WALL = 1;
var START = 2;
var EXIT = 3;
var HOLE = 4;
var SPRITE_SIZE = 32;
var PIVOT_OFFSET = (SPRITE_SIZE / 2);
var MAX_ACTION_COUNT = 500;

function MazeMap (width, height, defaultOrientation) {
	this.height = height;
	this.width = width;
	this.defaultOrientation = defaultOrientation;
	console.log("Constructor : [" + width + "," + height + "]");
	this.tiles = new Array(width);
	this.valid = false;
	for (var i = 0; i < width; i++) {
		this.tiles[i] = new Array(height);
	}
}

MazeMap.prototype.GetTile = function (x, y){
	
	if ((x < 0 || x >= this.width || y < 0 || y >= this.height) ||  this.tiles[x][y] == null)
		return WALL;
	else
		return this.tiles[x][y];
}

MazeMap.prototype.FromString = function (str){
	
	if (this.ValidMapString(str)){
		rows = str.split("/");
		var newHeight = rows.length;
		var newWidth = rows[0].length;
		console.log ("New Size : [" + newWidth + "," + newHeight + "]");
		//console.log("Length : " + rows.length);
		for (var row = 0; row < this.height; row++){	
			for (var col = 0; col < this.width; col++){
				//console.log("FromString : Row,col = [" + row + "," + col + "]");
				this.tiles[row][col] = parseInt(rows[row][col]);
			}
		}
		this.width = newWidth;
		this.height = newHeight;
		this.valid = true;
		console.log(this.tiles);
	} else {
		this.valid = false;
	}
	
}

MazeMap.prototype.ValidMapString = function(str){
	if (str == null || str.length == 0 || str == "")
		return false;
	rows = str.split("/");
	if (rows.length == 0)
		return false;
	var rowLength = rows[0].length;
	for (var row = 0; row < this.height; row++){	
		for (var col = 0; col < this.width; col++){
			if (rows[row].length != rowLength) //Irregular
				return false;
			//console.log("FromString : Row,col = [" + row + "," + col + "]");
			var parsedTile = parseInt(rows[row][col]);
			if (isNaN(parsedTile))
				return false;
			if (parsedTile < FLOOR || parsedTile > HOLE)
				return false;
		}
	}
	return true;
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
var INTERACTION_COUNT_CAP = 4000;

function Player(map, gameScene){
	var startPos = map.GetStart();
	this.map = map;
	this.Place(startPos[0], startPos[1]);
	this.SetOrientation(map.defaultOrientation);
	this.sprite = null;
	this.actions = null;
	this.gameScene = gameScene;
	this.interactionCount = 0;
}

Player.prototype.Place = function(x, y){
	this.x = x;
	this.y = y;
}

Player.prototype.IsOnExit = function(){
	return (this.map.tiles[this.x][this.y] == EXIT);
}

Player.prototype.IsAlive = function(){
	return (this.map.tiles[this.x][this.y] != WALL);
}

Player.prototype.IsDead = function(){
	return !this.IsAlive();
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
	this.interactionCount = 0;
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
	
Player.prototype.TakeSpriteOutOfScene = function(){
	
	//Lo sacamos de escena
	this.sprite.x = -500;
	this.sprite.y = -500;

}
	
Player.prototype.Draw = function(){
	if (this.sprite == null){
		this.sprite = this.gameScene.add.sprite(this.GetCanvasX(), this.GetCanvasY(), 'Player');
		this.sprite.anims.load('explosion');
	} else {
		this.sprite.x = this.GetCanvasX();
		this.sprite.y = this.GetCanvasY();
		this.sprite.anims.stop();
		this.sprite.setTexture("Player");
	}
	
	this.UpdateSpriteOrientation();
}

Player.prototype.PlayOrders = function(orderString){
	this.actions = new PlayerActions(this);
	eval(orderString);
	return this.actions;
}

Player.prototype.TileAhead = function(){
	var tile = null;
	if (this.orientation == N){
		tile = this.map.GetTile(this.x, this.y - 1);
	} else if (this.orientation == S){
		tile = this.map.GetTile(this.x, this.y + 1);
	} else if (this.orientation == E){
		tile = this.map.GetTile(this.x + 1, this.y);
	} else if (this.orientation == W){
		tile = this.map.GetTile(this.x - 1, this.y);
	}
	return tile;
}

Player.prototype.IsWallAhead = function(){
	return this.TileAhead() == WALL;
}

Player.prototype.IsPathAhead = function(){
	var tileAhead = this.TileAhead();
	return (tileAhead == FLOOR || tileAhead == START || tileAhead == EXIT);
}

Player.prototype.IsHoleAhead = function(){
	return this.TileAhead() == HOLE;
}

Player.prototype.Finished = function(){
	return (this.IsDead() || this.IsOnExit() || this.actions.HitActionCap() || this.interactionCount++ >= INTERACTION_COUNT_CAP);
}

Player.prototype.NotFinished = function(){
	return !this.Finished();
}

Player.prototype.MoveForward = function(){
	if (this.NotFinished()){
		if (this.orientation == N){
			this.y--;
		} else if (this.orientation == S){
			this.y++;
		} else if (this.orientation == E){
			this.x++;
		} else if (this.orientation == W){
			this.x--;
		}
		
		if (this.IsAlive())
			this.actions.EnqueueAction(new MoveForwardAction(this.orientation));
		else
			this.actions.EnqueueAction(new MoveForwardAndDieAction(this.orientation));
	}
}

Player.prototype.SpinRight = function(){
	if (this.NotFinished()){
		this.orientation++;
		
		if (this.orientation > W)
			this.orientation = N;
		
		this.actions.EnqueueAction(new SpinAction(RIGHT));
	}
}

Player.prototype.SpinLeft = function(){
	if (this.NotFinished()){
		this.orientation--;
		if (this.orientation < N)
			this.orientation = W;
		
		this.actions.EnqueueAction(new SpinAction(LEFT));
	}
}

//PLAYER ACTIONS
function PlayerActions(player){
	this.finished = false;
	this.pendingActions = [];
	this.player = player;
}	

PlayerActions.prototype.HitActionCap = function(){
	return (this.ActionCount() >= MAX_ACTION_COUNT);
}

PlayerActions.prototype.ActionCount = function(){
	return this.pendingActions.length;
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
	console.log("new SpinAction. Direction : " + direction);
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
	if (this.distanceCovered >= SPRITE_SIZE)
		this.finished = true;
	
}

function MoveForwardAndDieAction (direction){
	
	
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
	this.animating = false;
	console.log("new MoveForwardAndDieAction. Direction : " + direction);
	
}

MoveForwardAndDieAction.prototype.Update = function(){
	this.distanceCovered += this.speed;
	if (this.distanceCovered < (SPRITE_SIZE / 2)){
		this.player.sprite.x += this.speed * this.xStep;
		this.player.sprite.y += this.speed * this.yStep;
		
	} else {	
		if (!this.animating){
			this.animating = true;
			this.player.sprite.anims.play('explosion');
		} else {
			this.distanceCovered += this.speed;
			if (this.distanceCovered >= 150 + ((SPRITE_SIZE / 2))){
				console.log("FInished!");
				this.player.sprite.anims.pause();
				this.finished = true;
				this.player.TakeSpriteOutOfScene();
			}
		}
		
	}
}