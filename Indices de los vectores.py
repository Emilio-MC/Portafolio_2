#Nombre: Retornar Indices de los vectores
#Entrada: Debe de ingresar tres vectores con los numeros que quiera
#Salida: Devolver los indices de los vectores cuyo valor sean CERO o un numero NEGATIVO
#Restricciones: Solo puede ingresar una lista y deben haber numeros negativos y positivos
def obtenerIndicesListaVectores(v1,v2,v3):
    if isinstance(v1,list) and isinstance(v2,list) and isinstance(v3,list):
        if tamañoVector(v1)==tamañoVector(v2)==tamañoVector(v3):
            if validarDatosVector(v1,v2,v3):
                vector4=validarIndice(v1,0,[])
                vector5=validarIndice(v2,0,[])
                vector6=validarIndice(v3,0,[])
                vector7=[vector4]+[vector5]+[vector6]
                return vector7
            else:
                return -1
        else:
            return -1
    else:
        print ("ERROR: Debe de ingresar una lista")
            
           
def validarIndice(vector,indice,NuevaLista):
    if vector== []:
        return NuevaLista
    elif vector[0]<=0:
        return validarIndice (vector[1:],indice+1,NuevaLista+[indice])
    else:
        return validarIndice(vector[1:],indice+1,NuevaLista)

def tamañoVector(v1):
    if v1==[]:
        return 0
    else:
        return tamañoVector_aux(v1,0)

def tamañoVector_aux(vector,resultado):
    if vector==[]:
        return resultado
    else:
        return tamañoVector_aux(vector[1:],resultado+1)

def validarDatosVector(vector1,vector2,vector3):
    if vector1==[] and vector2==[] and vector3==[]:
        return print ("ERROR: No puede ingresar una lista vacia")
    else:
        if isinstance(vector1[0],int) and isinstance(vector2[0],int) and isinstance(vector3[0],int):
            return validarDatosVector(vector1[1:],vector2[1:],vector3[1:])
        else:
            return False
