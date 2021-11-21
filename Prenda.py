class Prenda:
    def __init__(self,numero):
        self.nro = numero
        self.tiempoLavado = 0
        self.prendasIncompatibles = []
        self.lavada = False
        self.lavadosVecinos = []
    
    def agregarIncompatibilidad(self,prendaInc):
        self.prendasIncompatibles.append(prendaInc)

    def asginarTiempoLavadoPrenda(self,tiempo):
        self.tiempoLavado = tiempo
    
    def get_nro(self):
        return(self.nro)
    
    def getIncompatibilidades(self):
        return(self.prendasIncompatibles)

    def getCantidadIncompatibilidades(self):
        return(len(self.prendasIncompatibles))
    
    def getDuracionLavadoPrenda(self):
        return(self.tiempoLavado)

    def getEstado(self):
        return(self.lavada)
    
    def esLavada(self):
        self.lavada = True
    
    def prendaCompatible(self,prenda):
        if prenda.get_nro() not in self.prendasIncompatibles:
            return True
        return False
        
    def agregarLavadoVecino(self,lavado):
        self.lavadosVecinos.append(lavado)

    def lavadoVecinoAsociado(self,numLavado):
        for lav in self.lavadosVecinos:
            if lav.getNumLavado() == numLavado:
                return False
        return True
            
    def getGrado(self):
        return(len(self.lavadosVecinos))