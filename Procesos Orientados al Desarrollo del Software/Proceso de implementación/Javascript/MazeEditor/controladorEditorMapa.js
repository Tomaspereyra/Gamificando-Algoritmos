
var gameScene = new Phaser.Scene('MazeScene');

var config = {
	type: Phaser.AUTO,
	width: 575,
	height: 575,
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
 var mapaPrueba=new Mapa(16,16);
 mapaPrueba.LlenarGrilla(PISO);
 dibujarTodo(mapaPrueba);	
}


gameScene.update = function() {

}

var pincel=PISO;
function dibujarMapa(mapa){
	var sprite;
	for (var row = 0; row < mapa.ancho; row++){
		for (var col = 0; col < mapa.altura; col++){
			//console.log("Drawing : Row,col = [" + row + "," + col + "] -> " + this.tiles[row][col]);
			sprite = gameScene.add.sprite((SPRITE_SIZE *(row+1)),(SPRITE_SIZE * col), mapIndexToSprite(mapa.grilla[row][col])).setInteractive();
			sprite.row = row
			sprite.col = col


			sprite.on('pointerdown', function (pointer) {//cuando tengo click
				x = pointer.x;
        		y = pointer.y;
        		row=Math.floor((x/SPRITE_SIZE));  
        		col=Math.floor((y/SPRITE_SIZE));
        		console.log("X=",row ,"Y=",col);

                if(pincel==PARED){
                    mapa.CambiarAPared(row,col);
                    this.setTexture('Wall');
                }
                
                if(pincel==PISO){
                    mapa.CambiarAPiso(row,col);
                    this.setTexture('Floor');
                }
                
                if(pincel==INICIO){
                    mapa.EstablecerInicio(row,col);
                    this.setTexture('Start');
                }

                if(pincel==SALIDA){
                    mapa.EstablecerSalida(row,col);
                    this.setTexture('Exit');
                }

        		this.setTint(0xff0000);//lo pinto de rojo

    		});


   			 sprite.on('pointerup', function (pointer) {//cuando levanta el click del mouse lo vuelve a pintar gris

      		  this.clearTint();//limpia el tint rojo a original

    		});
			sprite.setOrigin(0,0);
		}
	}
}

function paletaMapa(){
			
		for (var col = 0; col < 4; col++){
			sprite = gameScene.add.sprite((SPRITE_SIZE *0),(SPRITE_SIZE * col), mapIndexToSprite(col)).setInteractive();
			sprite.setOrigin(0,0);
            sprite.col = col


          
            sprite.on('pointerdown', function (pointer) {//cuando tengo click
                if (sprite.col=0) {
                    pincel=PISO;
                }
                 if (sprite.col=1) {
                    pincel=PARED;
                }
                 if (sprite.col=2) {
                    pincel=INICIO;
                }
                 if (sprite.col=3) {
                    pincel=SALIDA;
                }

                this.setTint(0xff0000);//lo pinto de rojo

            });
            
            sprite.on('pointerup', function (pointer) {//cuando levanta el click del mouse lo vuelve a pintar gris

              this.clearTint();//limpia el tint rojo a original

            });   

        }
		
	
	//return this.AsignarTileSeleccionado(tileSeleccionado);

}

function dibujarTodo(mapa){
	dibujarMapa(mapa);
	paletaMapa();

}