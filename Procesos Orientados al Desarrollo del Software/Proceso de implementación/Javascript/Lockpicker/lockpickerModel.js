//MAP

var FLOOR = 0;
var WALL = 1;
var START = 2;
var EXIT = 3;
var HOLE = 4;
var SPRITE_SIZE = 32;
var PIVOT_OFFSET = (SPRITE_SIZE / 2);
var MAX_ACTION_COUNT = 500;

function IsNumeric(n) {
  return !isNaN(parseFloat(n)) && isFinite(n);
}

function IsArray(obj){
	return (obj instanceof Array);
}

var targetNumbers;
var inputNumbers;
var currentNumber;
var currentIndex;

function Lock (password) {
	if (password)
		this.SetPassword(password);
	console.log("Lock.Constructor : " + this.password);
}

Lock.prototype.SetPassword  = function (password){
	if (IsArray(password))
		this.password = password;
	else
		console.log("Lock.SetPassword(" + password + ") : " + x + " is not an array!");
}

Lock.prototype.AddPasswordNumber = function (x){
	if (IsNumeric(x))
		this.password.push(x);
	else
		console.log("Lock.AddPasswordNumber(" + x + ") : " + x + " is not a number!");
}

Lock.prototype.Check = function(password){
	if (this.password.length != password.length)
		return false;
	for (i = 0; i < this.password.length; i++){
		if (this.password[i] != password[i]){
			return false;
		}
	}
	return true;
}

Lock.prototype.PasswordSize = function(){
	return this.password.length;
}

Lock.prototype.ToString = function(){
	
	result = "";
	if (this.password.length > 0){
		result += this.password[0];
		for (i = 1; i < this.password.length; i++){
			result += "," + this.password[i];
		}
	}
	return result;
}

Lock.prototype.FromString = function (str){
	
	rows = str.split(",");
	console.log ("Lock.FromString(" + str + ")");
	this.password = [];
	for (var row = 0; row < rows.length; row++){	
		key =  parseInt(rows[row]);
		if (IsNumeric(key)){
			this.AddPasswordNumber(key);
		} else {
			console.log("Key " + key + " Is not a valid number!");
		}
	}
	
	this.valid = true;
	
}

Lock.prototype.GetDigit = function(index){
	return this.password[index];
}

Lock.prototype.Draw = function(scene){
	var sprite;
	for (var row = 0; row < this.height; row++){
		for (var col = 0; col < this.width; col++){
			//console.log("Drawing : Row,col = [" + row + "," + col + "] -> " + this.tiles[row][col]);
			sprite = scene.add.sprite((SPRITE_SIZE * row), (SPRITE_SIZE * col), this.IndexToSprite(this.tiles[row][col]));
			sprite.setOrigin(0, 0);
		}
	}
}

///LOCKPICK
var INTERACTION_COUNT_CAP = 4000;

function Lockpick(){
	this.Reset();
}

Lockpick.prototype.GetDigit = function(index){
	if (index >= this.input.length){
		return "_";
	} else {
		return this.input[index];
	}
}

Lockpick.prototype.GetCurrentValue = function(){
	return this.currentValue;
}

Lockpick.prototype.SetCurrentValue = function(x){
	this.currentValue = x;
}

Lockpick.prototype.InputCurrentValue = function(){
	this.input.push(this.currentValue);
}

Lockpick.prototype.InputSize = function(){
	return this.input.length;
}

Lockpick.prototype.TryToOpen = function(lock){
	return lock.Check(this.input);
}
	
Lock.prototype.LastInput = function(){
	if (this.input.length > 0)
		return this.input[this.input.length-1];
	else
		return 0;
}

Lock.prototype.AnteLastInput = function(){
	if (this.input.length > 1)
		return this.input[this.input.length-2];
	else
		return 0;
}
	
Lockpick.prototype.Reset = function(){
	this.currentIndex = 0;
	this.input = [];
	this.currentValue = 0;
}

Lockpick.prototype.PlayOrders = function(orderString){
	this.actions = new PlayerActions(this);
	eval(orderString);
	return this.actions;
}