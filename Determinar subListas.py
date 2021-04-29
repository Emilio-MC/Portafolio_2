#Nombre: Determinar subListas
#Entrada: Debe ingresar una lista 
#Salida: Devolver la cantidad de sublistas que contiene la lista
#Restricciones: Solo puede ingresar una lista
def nivelesLista(lista):
    if isinstance(lista,list):
        return nivelesLista_aux(lista,[])
    else:
        print("ERROR: Debe de ingresar una lista")

def nivelesLista_aux(lista,lista2):
    if lista==[]:
        return lista2
    elif isinstance(lista[0],list):
       D=dividir(lista[0],1)
       return nivelesLista_aux(lista[1:],lista2+[D])
    else:
        return nivelesLista_aux(lista[1:],lista2+[0])

def dividir(lista,lista2):
    if lista==[]:
        return lista2
    else:
        if isinstance(lista[0],list):
            return dividir(lista[0],lista2+1)
        else:
            return 1
