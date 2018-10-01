var gameScene = new Phaser.Scene('MazeScene');

var config = {
	type: Phaser.AUTO,
	width: 512,
	height: 512,
	parent: 'phaser-div', //se define el canvas donde va a dibujar
	scene: gameScene
};

var game = new Phaser.Game(config);



gameScene.preload = function () {
	this.load.image ('Floor', 'Assets/Floor.png');
	this.load.image ('Wall', 'Assets/Wall.png');
	this.load.image ('Start', 'Assets/Start.png');
	this.load.image ('Exit', 'Assets/Exit.png')
}


function mapIndexToSprite(index){   
    switch (index){
        case PISO:
            return 'Floor';
            break;
        case PARED:
            return 'Wall';
            break;
        case INICIO:
            return 'Start';
            break;
        case SALIDA:
            return 'Exit';
            break;
    }	
}

gameScene.create = function () {    
 var mapaPrueba=new Mapa(32,32);
 mapaPrueba.LlenarGrilla(PISO);
 dibujarMapa(mapaPrueba);	
}


gameScene.update = function() {

}

function dibujarMapa(mapa){
	var sprite;
	for (var row = 0; row < mapa.ancho; row++){
		for (var col = 0; col < mapa.altura; col++){
			//console.log("Drawing : Row,col = [" + row + "," + col + "] -> " + this.tiles[row][col]);
			sprite = gameScene.add.sprite((SPRITE_SIZE *row),(SPRITE_SIZE * col), mapIndexToSprite(mapa.grilla[row][col])).setInteractive();
			
			sprite.on('pointerdown', function (pointer) {

        		this.setTint(0xff0000);

    		});

   			 sprite.on('pointerout', function (pointer) {

        		this.clearTint();

   			 });

   			 sprite.on('pointerup', function (pointer) {

      		  this.clearTint();

    		});
			sprite.setOrigin(0, 0);
		}
	}
}

