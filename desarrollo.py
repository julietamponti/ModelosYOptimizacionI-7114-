#Voy a crear un diccionario, donde la clave es el numero de la prenda prenda y  el valor de cada una, un diccionario que contiene tiempo de lavado
# y una lista con sus incompatibilidades.
def crearDiccionario(archivo):
    dic = {}
    linea = archivo.readline()
    while linea != '':
        if linea.startswith(('e','n')):
            dato0,dato1,dato2 = tuple(linea.replace('\n','').split())            
            if dato0 == 'e':
                if dato1 not in dic.keys():
                    dic[dato1] = {'tiempo':0,'incomp':[]}                    
                dic[dato1]['incomp'].append(dato2)                    
            else:
                dic[dato1]['tiempo']= int(dato2)                    
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
    while index < len(lista) and compatible:    #la condicion de que sea compatible la prenda que se esta buscando localizar, es que sea compatible con   
                                                #todas las prendas que ya estan asignadas al lavado        
        
        if lista[index] in dic['incomp']:      
            compatible = False                  #si la prenda del lavado que esta iterando esta en la lista de incompatibles de la prenda que 
                                                #se quiere asignar, ya no son incompatibles
        
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

def main():
    archivo = open('Enunciado.txt',mode= 'r',encoding= 'utf-8')
    prendas = crearDiccionario(archivo)
    #print(prendas)
    lavados = {}
    lavados = crearLavados(lavados,prendas)
    print(lavados)

main()