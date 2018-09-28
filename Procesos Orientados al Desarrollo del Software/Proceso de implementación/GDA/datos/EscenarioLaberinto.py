from datos.Escenario import Escenario


class EscenarioLaberinto(Escenario):

    def __init__(self, bloquesPermitidos, cantBloquesMax, hint, posibleSolucion, descripcion, mapa):
        Escenario.__init__(self, bloquesPermitidos, cantBloquesMax, hint, posibleSolucion, descripcion)
        self.mapa = mapa

    def setMapa(self, mapa):
        self.mapa = mapa

    def getMapa(self):
        return self.mapa

    def __str__(self):
        return str("ID:"+str(self.getIdEscenario())+" Bloques Permitidos:"+str(self.getBloquesPerimitidos())
                   +" Bloques max:"+str(self.getCantBloquesMax())+" Hint:"+self.getHint()+" Posible solucion: "
                   +self.getPosiblesSolucion() + " Descripcion:"+self.getDescripcion()+" Mapa:" + self.getMapa())
