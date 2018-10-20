var PISO = 0;
var PARED = 1;
var INICIO = 2;
var SALIDA = 3;
var SPRITE_SIZE = 32;
var PIVOT_OFFSET = (SPRITE_SIZE / 2);


function Mapa (ancho, altura) {
	this.ancho = ancho;
    this.altura = altura;
    this.grilla = new Array(ancho);
	this.tileSeleccionado=PISO;
	for (var i = 0; i < ancho; i++) {
		this.grilla[i] = new Array(altura);
	}

}

Mapa.prototype.LlenarGrilla= function(TIPO_TIlE){
	for(var fila=0; fila<this.ancho; fila++){
		for(var columna=0; columna<this.altura;columna++){
			this.grilla[fila][columna]=TIPO_TIlE;
		}
	}
}

Mapa.prototype.CambiarAPared=function(x,y){
		this.grilla[x][y]=PARED
}

Mapa.prototype.CambiarAPiso=function(x,y){
		this.grilla[x][y]=PISO
}

Mapa.prototype.EstablecerInicio=function(x,y){
		this.grilla[x][y]=INICIO
}

Mapa.prototype.EstablecerSalida=function(x,y){
		this.grilla[x][y]=SALIDA
}

Mapa.prototype.asignarTile=function(x,y,tipoTile){
	this.grilla[x][y]=tipoTile;
}

Mapa.prototype.IndexToChar = function(index){
    switch (index){
        case PISO:
            return ' ';
            break;
        case PARED:
            return '#';
            break;
        case INICIO:
            return 'S';
            break;
        case SALIDA:
            return 'E';
            break;
    }
}

Mapa.prototype.ToPrettyString = function(){
    var str = "";
    for(var fila=0; fila<this.ancho; fila++){
		for(var columna=0; columna<this.altura;columna++){
			str += this.IndexToChar(this.grilla[fila][columna]);
            //str += this.grilla[fila][columna];
		}
        str += "\n";
	}
    return str;
}

Mapa.prototype.ToString = function(){
    var str = "";
    for(var fila=0; fila<this.ancho; fila++){
        for(var columna=0; columna<this.altura;columna++){
            str += this.grilla[fila][columna];
            //str += this.grilla[fila][columna];
        }
        str += "/";
    }
    return str;
}

Mapa.prototype.Validar=function(){ //si es valido devuelve true sino falso
    var contadorInicio=0;
    var contadorSalida=0;

    for(var fila=0; fila<this.ancho; fila++){
        for(var columna=0; columna<this.altura;columna++){
             if(this.grilla[fila][columna]==INICIO){
                contadorInicio=contadorInicio+1;
             }

            if(this.grilla[fila][columna]==SALIDA){
                contadorSalida=contadorSalida+1;
            }
            
        }
    }

    return (contadorInicio==1 && contadorSalida==1);
}