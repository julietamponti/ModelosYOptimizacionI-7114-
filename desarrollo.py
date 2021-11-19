#Voy a crear un diccionario, donde la clave es el numero de la prenda prenda y  el valor de cada una, un diccionario que contiene tiempo de lavado
# y una lista con sus incompatibilidades.
"""
def crearDiccionario(archivo):
    dic = {}
    linea = archivo.readline()
    while linea != '':
        if linea.startswith(('e','n')):
            dato0,dato1,dato2 = tuple(linea.replace('\n','').split())            
            if dato0 == 'e':
                if dato1 not in dic.keys():
                    dic[dato1] = {'tiempo':0,'incompatibilidades':[]}                    
                dic[dato1]['incompatibilidades'].append(dato2)    
                if dato2 not in dic.keys():
                    dic[dato2] = {'tiempo':0,'incompatibilidades':[]} 
                dic[dato2]['incompatibilidades'].append(dato1)              
            else:
                if not dato1 in dic.keys():
                    dic[dato1] = {'tiempo':0,'incompatibilidades':[]}  
                    dic[dato1]['tiempo']= int(dato2)    
                else:
                    dic[dato1]['tiempo']= int(dato2)    
                print(dato1)               
        linea = archivo.readline()
    archivo.close()
    return dic

def mayorTiempoDeLavado(dic): #devuelve el numero de prenda que mas tarda den lavarse de las que quedan sin lavar y todos sus datos
    max = 0 #ya que comparare con el y siempre sera menor a los tiempos de lavado
    kmax = ''

    for k in dic.keys():
        if dic[k]['tiempo'] > max:
            max = dic[k]['tiempo'] # toma el valor maximo de tiempo
            kmax = k              # la prenda que mas tarda en lavarse
    return (kmax,dic.pop(kmax)) # elimino la prenda, ya que ya ha sido asignada a un lavado, es decir que sera lavada


def esCompatible(lista,dic):
    compatible = True
    index = 0
    while index < len(lista) and compatible:
        if lista[index] in dic['incompatibilidades']:
            compatible = False
        else:
            index += 1
    return compatible
    

def crearLavados(lavados,prendas):  #devuelve un diccionario con todos 
    while len(prendas) > 0:
        lavado =[]
        k, prenda = mayorTiempoDeLavado(prendas)
        lavarropas = {}   
        lavado.append(k)

        for p,v in prendas.items():
            if esCompatible(lavado,v):
                lavado.append(p)
        
        for x in lavado:
            lavarropas[k] = prenda
            if x != k:
                lavarropas[x] = prendas.pop(x) #idem pop anterior, se le asigno un lavado, por lo que ya no me interesa ubicarla en otro
        
        lavados[len(lavados)+1] = lavado   

    return(lavados)

def escribirArchivo(diccionario):   #escribe el archivo en el formato que se solicita
    fichero = open ("resultado2.txt",mode='w')
    for x,y in diccionario.items():
        for j in y:
            fichero.write(str(j) + ' '+ str(x)+ '\n')   #formato solicitado
    print("Se escribio el archivo")
    fichero.close()


def main():
    archivo = open('Enunciado2.txt',mode= 'r',encoding= 'utf-8')
    prendas = crearDiccionario(archivo)
    #print(prendas)
    lavados = {}
    lavados = crearLavados(lavados,prendas)
    #print(lavados)
    escribirArchivo(lavados)
"""

def leerArc (archivo):
    linea = archivo.readline()
    prendas = []
    while linea != '':
        if linea.startswith('p'):
            p, c, n, m  = tuple(linea.replace('\n','').split())  
            prendas = mandarPrendasALavar(prendas,int(n))

        elif linea.startswith(('e','n')):
            dato0,dato1,dato2 = tuple(linea.replace('\n','').split())            
            if dato0 == 'e':
                agregarIncompatibilidad(prendas,int(dato1),int(dato2))      
            else:
                asginarTiempoLavadoPrenda(prendas,int(dato1),int(dato2))
        linea = archivo.readline()
    archivo.close()
    return prendas

def agregarIncompatibilidad(prendas,p1,p2):
     prendas[p1-1].agregarIncompatibilidad(p2)
     prendas[p2-1].agregarIncompatibilidad(p1)

def asginarTiempoLavadoPrenda(prendas,prenda,tiempo):
    prendas[prenda-1].asginarTiempoLavadoPrenda(tiempo)

def mandarPrendasALavar(prendas,cantidadDePrendas):
    for i in range (1,cantidadDePrendas+1):
        prendas.append(Prenda(i))
    return(prendas)

def ordenMayorTiempoDeLavado(prendas):
    prendas.sort(key=lambda x:x.getDuracionLavadoPrenda(),reverse=True)
    return (prendas) 


def crearLavados(list_mayor_igual_10,list_menor_10):
    lavados_1 = generarLavados(list_menor_10)
    lavados_2 = generarLavados(list_mayor_igual_10)
    lavados = []
    for i in lavados_1:
        lavados.append(i)
    for j in lavados_2:
        lavados.append(j)
    return(lavados)
    
def generarLavados(prendas):
    lavados = []
    prendas = ordenMayorTiempoDeLavado(prendas)
    lavado = Lavado(1)
    prenda = prendas[0]
    lavado.agregarPrenda(prenda)
    lavados.append(lavado)
    prenda.esLavada()
    for prenda in prendas:
        for lavado in lavados:
            if (lavado.esCompatible(prenda) and prenda.getEstado()==False):
                lavado.agregarPrenda(prenda)
                prenda.esLavada()
        if prenda.getEstado() == False:
            lavado = Lavado((len(lavados)+1))
            lavado.agregarPrenda(prenda)
            lavados.append(lavado)
            prenda.esLavada()
    return (lavados)            

def escribirArchivo(lavados):
    fichero = open('2entrega.txt','w')
    for lavado in lavados:
        for prenda in lavado.getPrendasEnLavado():
            fichero.write(str(prenda.get_nro()) + ' ' + str(lavado.getNumLavado()) +"\n")

    fichero.close()

class Prenda:
    def __init__(self,numero):
        self.nro = numero
        self.tiempoLavado = 0
        self.prendasIncomp = []
        self.lavada = False
    
    def agregarIncompatibilidad(self,prendaInc):
        self.prendasIncomp.append(prendaInc)

    def asginarTiempoLavadoPrenda(self,tiempo):
        self.tiempoLavado = tiempo
    
    def get_nro(self):
        return(self.nro)
    
    def getIncompatibilidades(self):
        return(self.prendasIncomp)

    def getDuracionLavadoPrenda(self):
        return(self.tiempoLavado)

    def getEstado(self):
        return(self.lavada)
    
    def esLavada(self):
        self.lavada = True
    
    def prendaCompatible(self,prenda):
        if prenda.get_nro() not in self.prendasIncomp:
            return True
        return False

class Lavado:
    def __init__(self,numero):
        self.nro = numero
        self.prendas = []
        #self.prendasNoAceptadas = []

    def agregarPrenda(self,prenda):
        #self.prendas.append(prenda.get_nro())
        self.prendas.append(prenda)
        #self.cancelarPrendas(prenda.getIncompatibilidades())
    
    """def cancelarPrendas(self,incompatibilidades):
        if (len(self.prendasNoAceptadas))==0:
            self.prendasNoAceptadas == incompatibilidades
        else:
            for i in incompatibilidades:
                if not i  in prendasNoAceptadas:
                    self.prendasNoAceptadas.append(i)
    """
    def cantPrendas(self):
        return (len(self.prendas))
    
    def esCompatible(self,prendaAAgregar):
        for prenda in self.prendas:
            #return (prenda.prendaCompatible(prendaAAgregar))
            if prendaAAgregar.get_nro() in prenda.getIncompatibilidades():
                return False
        return True
                #a = a-1
                #print('a:',a)
    def getPrendasEnLavado(self):
        return(self.prendas)
    
    def getNumLavado(self):
        return(self.nro)

def main():
    archivo = open('Enunciado2.txt',mode= 'r',encoding= 'utf-8')
    #archivo = open('probando.txt',mode= 'r',encoding= 'utf-8')
    listaPrendas = leerArc(archivo)
    list_menor_10 = []
    list_mayor_igual_10 = [] 
    for prenda in listaPrendas:
        if prenda.getDuracionLavadoPrenda()>= 10:
            list_mayor_igual_10.append(prenda)
        else:
            list_menor_10.append(prenda)

    lavados = crearLavados(list_mayor_igual_10,list_menor_10)
    #suma = 0 
    for lavado in lavados:
        print('lavado: ',lavado.getNumLavado())
        print ('prendas en lav: ')
        for prenda in lavado.getPrendasEnLavado():
            print('num:',prenda.get_nro(),'tiempo: ', prenda.getDuracionLavadoPrenda())
        #suma = suma + len(lavado.getPrendasEnLavado())

    #print('suma: ',suma)
    
    
    escribirArchivo(lavados)
main()
