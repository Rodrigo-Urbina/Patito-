# Manejo de funciones y variables dentro de nuestro directorio de funciones y tabla de variables

import sys
import estructuras as tabla


# Tabla de ids de todas las declaraciones que hayan.
arrIDs = {}

# variables globales
is_local = false
is_global = false
is_main = false


# Función que inicializa la tabla con funciones, global, y main.
def add (id, data_type):
    temp = tabla.tabla(data_type, {})

    if len(arrIDs) >= 1 and not funct_Exist(id):
        arrIDs[id] = temp
    if not arrIDs:
        arrIDs[id] = temp

# Función que revisa que no haya dos funciones con el mismo nombre.
def funct_Exist(id):
    for keys in arrIDs:
        if id == keys:
            print("Id de funcion declarado previamente:", id)
            sys.exit()
            return True
    return False

# Función que valida si no hay una variable global con el mismo id ya definido.
def global_Var_Exist(id):
    if "global" in arrIDs.keys():
        for keys in arrIDs["global"].value:
            if id == keys:
                print("Variable global con el mismo ID:", id)
                sys.exit()
                return True
    return False

# Función que comprueba que no se puedan volver a declarar dos variables
# con el mismo ID.
def local_Var_Exist(id, id_function):
    aux = False # aux es la variable booleana que regresa el si esta o no esta ya dentro de la funcion local

    if id in arrIDs[id_funcion].value:
        aux = True
        print("ERROR: ID ya definido: ", id)
        sys.exit()
    return aux


# Funcion que transforma las variables flotantes en tipo flotante
def turn_Float(data, id, id_function):
    temp = str(type(data))

    if arrIDs[id_function].value[id].data_type == 'float' and temp == "<class 'int'>":
        temp = "<class 'float'>"
    return temp

# Función que valida que el valor ingresado y el tipo de la variable
# sean iguales.
def type_validation(data, id, id_function):
    temp = turn_Float(data, id, id_function)
    aux = None
    localFound = False
    globalFound = False

    if id in arrIDs[id_function].value:
        aux = arrIDs[id_function].value[id].data_type
        localFound = True
    if "global" in arrIDs.keys():
        if id in arrIDs["global"].value:
            aux = arrIDs["global"].value[id].data_type
            globalFound = True
    if not localFound and not globalFound:
        print('ERROR: ID no declarado:', id)
        sys.exit()

    if data == 'true' or data == 'false':
        temp = "<class 'bool'>"
    if temp == "<class 'float'>" and aux == 'float':
        return True
    if temp == "<class 'int'>" and aux == 'int':
        return True
    if temp == "<class 'str'>" and aux == 'string':
        return True
    if temp == "<class 'bool'>" and aux == 'bool':
        return True
    if temp == None:
        print(id, "No tiene valor asignado")
        sys.exit()
    else:
        print("ERROR: Dato no válido. validate", data, id, id_function)
        sys.exit()


# Función que obtiene el tipo de una variable dentro de una función.
def getType(id, id_function):
    type = arrIDs[id_function].value[id].data_type
    return type


# Función que obtiene el valor de una variable dentro de una función.
def getValue(id, id_function):
    value = arrIDs[id_function].value[id].value
    return value

# Función que retorna una lista con las variables que son parámetros
# dentro de la función.
def getidParam(id_function):
    temp = []
    for id in arrIDs[id_function].value:
        if arrIDs[id_function].value[id].param:
            temp.append(id)
    return temp

# Función que retorna el valor de una variable si esta se encuentra declara,
# en caso contrario regresa el id.
def returnValue(id, id_function):
    if id in arrIDs[id_function].value.keys():
        temp = arrIDs[id_function].value[id].value
        return temp
    else:
        return id
