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

def main():
    archivo = open('Enunciado.txt',mode= 'r',encoding= 'utf-8')
    prendas = crearDiccionario(archivo)
    print(prendas)
main()