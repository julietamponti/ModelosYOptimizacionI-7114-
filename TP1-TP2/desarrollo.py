from Prenda import Prenda
from Lavado import Lavado

# ---------------------------------------------------
#                  MEJOR MODELO TP2                 #
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

def crearLavados(prendas):
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
    fichero = open('resultadoTP2.txt','w')
    for lavado in lavados:
        for prenda in lavado.getPrendasEnLavado():
            fichero.write(str(prenda.get_nro()) + ' ' + str(lavado.getNumLavado()) +"\n")

    fichero.close()

def main():
    archivo = open('Enunciado2.txt',mode= 'r',encoding= 'utf-8')
    #archivo = open('Enunciado.txt',mode= 'r',encoding= 'utf-8')
    listaPrendas = leerArc(archivo)
    lavados = crearLavados(listaPrendas)
    
    totalTiempLav = 0
    for lavado in lavados:
        
        print('lavado: ',lavado.getNumLavado())
        print ('prendas en lav: ')
        for prenda in lavado.getPrendasEnLavado():
            print('num:',prenda.get_nro(),'tiempo: ', prenda.getDuracionLavadoPrenda())
            #print(prenda.get_nro())
        
        totalTiempLav += lavado.get_duracion()
        #suma = suma + len(lavado.getPrendasEnLavado())
    
    #print('suma: ',suma)
    
    print('\n')
    print('------------------------------------------------------')
    print('duracion total de lavados: ',totalTiempLav)
    print('------------------------------------------------------')   
    
    escribirArchivo(lavados)

main()

