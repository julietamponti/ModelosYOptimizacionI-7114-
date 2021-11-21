class Lavado:
    def __init__(self,numero):
        self.nro = numero
        self.prendas = []

    def agregarPrenda(self,prenda):
        #self.prendas.append(prenda.get_nro())
        self.prendas.append(prenda)
        #self.cancelarPrendas(prenda.getIncompatibilidades())
    
    def cantPrendas(self):
        return (len(self.prendas))
    
    def esCompatible(self,prendaAAgregar):
        for prenda in self.prendas:
            if prendaAAgregar in prenda.getIncompatibilidades():
                return False
        return True

    def prendaEnLavado(self,prenda):
        for p in self.prendas:
            if p == prenda:
                return True
        return False

    def getPrendasEnLavado(self):
        return(self.prendas)
    
    def getNumLavado(self):
        return(self.nro)

    def get_duracion(self):
        max = 0
        for prenda in self.prendas:
            if prenda.getDuracionLavadoPrenda()>max:
                max = prenda.getDuracionLavadoPrenda()
        return(max)