from Prenda import Prenda
from Lavado import Lavado

# ---------------------------------------------------
#                  INTENTO GRAFO TP2                 #
# ---------------------------------------------------

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

    prendas[p1-1].agregarIncompatibilidad(prendas[p2-1])
    prendas[p2-1].agregarIncompatibilidad(prendas[p1-1])
    

def asginarTiempoLavadoPrenda(prendas,prenda,tiempo):
    prendas[prenda-1].asginarTiempoLavadoPrenda(tiempo)

def mandarPrendasALavar(prendas,cantidadDePrendas):
    for i in range (1,cantidadDePrendas+1):
        prendas.append(Prenda(i))
    return(prendas)

# Ordeno por cantidad de incompatibilidades en un primer momento, suponiendo que a mayor 
# cantidad de incomaptibilidades resulta mas dificil ubicar esta prendas en lavados (colorearlas)
# y me da un resultado mas optimo
def ordenCantidadIncompatibilidades(prendas):
    prendas.sort(key=lambda x:x.getCantidadIncompatibilidades(),reverse=True)
    return (prendas) 


# def ordenMayorTiempoDeLavado(prendas):
#     prendas.sort(key=lambda x:x.getDuracionLavadoPrenda(),reverse=True)
#     return (prendas) 

def actualizarGradoPrendas(prendas,lavados):
    for prenda in prendas:
        for prendaInc in prenda.getIncompatibilidades():
            for lavado in lavados:
                if (prenda.lavadoVecinoAsociado(lavado.getNumLavado()) and lavado.prendaEnLavado(prendaInc)):
                    prenda.agregarLavadoVecino(lavado)
    return(prendas)
        
def buscarPrendaConMayorGrado(prendas,lavados):
    prendasAct = actualizarGradoPrendas(prendas, lavados)
    prendasAct.sort(key=lambda x:x.getGrado(),reverse=True)
    return(prendasAct[0])

def crearLavados(prendas):
    lavados = []
    prendasLavadas = []
    lavado = Lavado(1)
    prenda = prendas[0]
    lavado.agregarPrenda(prenda)
    lavados.append(lavado)
    prenda.esLavada()
    prendas.pop(0)
    while(len(prendas)>0):
        print('lenPrendas: ',len(prendas))
        prendaAAsignar = buscarPrendaConMayorGrado(prendas, lavados)
        for lavado in lavados:
            if (lavado.esCompatible(prendaAAsignar) and prendaAAsignar.getEstado()==False):
                #print('if 1')
                lavado.agregarPrenda(prendaAAsignar)
                prendaAAsignar.esLavada()
        if prendaAAsignar.getEstado() == False:
            #print('if 2')
            lavado = Lavado((len(lavados)+1))
            lavado.agregarPrenda(prendaAAsignar)
            lavados.append(lavado)
            prendaAAsignar.esLavada()
        prendas.remove(prendaAAsignar)
        print('lenPrendas desp del for: ',len(prendas))
    return (lavados)            

def escribirArchivo(lavados):
    fichero = open('resultadoTP2-UltimaVersion.txt','w')
    for lavado in lavados:
        for prenda in lavado.getPrendasEnLavado():
            fichero.write(str(prenda.get_nro()) + ' ' + str(lavado.getNumLavado()) +"\n")

    fichero.close()

def main():
    archivo = open('Enunciado2.txt',mode= 'r',encoding= 'utf-8')
    #archivo = open('Enunciado.txt',mode= 'r',encoding= 'utf-8')
    listaPrendas = leerArc(archivo)
    lista_orden_incomp = ordenCantidadIncompatibilidades(listaPrendas)
    lavados = crearLavados(lista_orden_incomp)
    
    totalTiempLav = 0
    for lavado in lavados:
        
        print('lavado: ',lavado.getNumLavado())
        print ('prendas en lav: ')
        for prenda in lavado.getPrendasEnLavado():
            #print('num:',prenda.get_nro(),'tiempo: ', prenda.getDuracionLavadoPrenda())
            print(prenda.get_nro())
        
        totalTiempLav += lavado.get_duracion()
        #suma = suma + len(lavado.getPrendasEnLavado())
    
    #print('suma: ',suma)
    
    print('\n')
    print('------------------------------------------------------')
    print('duracion total de lavados: ',totalTiempLav)
    print('------------------------------------------------------')   
    
    escribirArchivo(lavados)
    
    print(listaPrendas)
main()
