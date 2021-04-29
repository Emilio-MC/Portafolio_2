#Nombre: Invertir los elementos de una lista
#Entradas: Debe imgresar una lista
#Salidas: Retornara los numeros de la lista pero en forma inversa
#Restricciones: Solo puede ingresar una lista 
def invertirLista(lista):
    if lista==[]:
        print ("No ingrese una lista vacia ")
        return 0
    elif lista!= []:
        return invertirLista_aux(lista, [])
    else:
        print ("ERROR: Debe ingrear una lista")


def invertirLista_aux(lista, nuevalista):
    if lista == []:
        return nuevalista
    else:
        nuevalista=nuevalista+[lista[-1]]
        return invertirLista_aux(lista[:-1],nuevalista)
