#Nombre: Determinar cuál es el número menor y mayor de una lista
#Entradas: Debe imgresar una lista
#Salidas: Retornara los numeros mayores y menores de la lista
#Restricciones: Solo puede ingresar una lista 
def extremosLista(lista):
    if lista == []:
        print ("No puede ingresar una lista vacia")
        return print ("ERROR")
    else:
        return extremosLista_aux(numeroMayor(lista),numeroMenor(lista))
    
def extremosLista_aux(lista, nuevaLista):
    if lista == nuevaLista:
        otraLista=[lista]
        return otraLista
    else:
        masListas=[nuevaLista,lista]
        return masListas
    
def numeroMayor(lista):
    if lista==[]:
        print ("No puede ingresar una lista vacia")
        return print ("ERROR")
    else:
        return numeroMayor_aux(lista[1:], lista[0])
    
def numeroMayor_aux(lista, indice):
    if lista == []:
        return indice
    elif lista[0]>indice:
        return numeroMayor_aux(lista[1:], lista[0])
    else:
        return numeroMayor_aux(lista[1:], indice)


def numeroMenor(lista):
    if lista == []:
        print ("No puede ingresar una lista vacia")
        return print("ERROR")
    else:
        return numeroMenor_aux(lista[1:], lista[0])
    
def numeroMenor_aux(lista, resu):
    if lista==[]:
        return resu
    elif lista[0]<resu:
        return numeroMenor_aux(lista[1:], lista[0])
    else:
        return numeroMenor_aux(lista[1:], resu)


