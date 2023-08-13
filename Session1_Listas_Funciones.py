print("Hola Mundo!!!")

# Recomendacion es tener las colecciones del mismo tipo


# lista = [12, 56.7, "hola", False, 20+7j]

# # suma=0.0

# suma=""

# for valor in lista:

#     # suma = suma+valor

#     suma = suma+str(valor)

#     print(valor)

# print(suma)

# LISTAS son una serie de elementos ordenados por indice, mutables, permiten repetidos

# funciones builtins

# lista = [1,6,2,7,23,0]

# print(len(lista))

# print(type(lista))

# print(lista)

# lista.append(33)

# print(lista)

# lista[0]=100

# print(lista)

# lista.sort()

# print(lista)

# lista.reverse()

# print(lista)


# TUPLAS son una serie de elementos ordenados por indice, inmutables, permiten valores repetidos

# dias=('Dom','Lun','Mar','Mie','Jue','Vie','Sab')

# print(type(dias))

# print(len(dias))

# print(dias)

# print(dias.count('Lun'))

# print(dias.index('Mie'))

# # Convirtiendo la Tupla en Lista

# lista_dias=list(dias)

# print(lista_dias)

# lista_dias.pop(5)

# print(lista_dias)

# # La lista aun permanece

# print(dias)


# CONJUNTOS son una serie de elementos, no tienen orden y no permite repetidos

# enteros1 = {1,2,7,8,9,0,11,34,25}

# enteros2 = {13,23,7,83,9,0,11}

# print(type(enteros1))

# print("Enteros1:",enteros1)

# print("Enteros2:",enteros2)

# print(len(enteros1))

# print(len(enteros2))

# union = enteros1.union(enteros2)

# print("Union:",union)

# print("num:",len(union))

# resta = (enteros1-enteros2)

# print("Resta:",resta)

# print("num:",len(resta))

# interseccion = enteros1.intersection(enteros2)

# print("Interseccion:",interseccion)


# DICCIONARIOS son una serie de parejas llave(objeto), valor(objeto), ordenados

# permiten duplicados ,son mutables.


# larouse = {'cafe':'Semilla aromatica',

#            'casa':'lugar donde se habita',

#            'java':'lenguaje de programacion' }


# diccionario = {1:'Fernando',102:'Juan Jose', 19:"Maria Luisa", 200:"Veronica"}


# # Obteniendo todas las llaves

# llaves = larouse.keys()

# for llave in llaves:

#     print(llave)

# print("Llaves:",llaves)

# lista_llaves=list(llaves)

# print(lista_llaves)


# # Obteniendo todos los valores

# valores = larouse.values()

# lista_valores=list(valores)

# print(lista_valores)


# elemento = larouse.get('cafe')

# print("Elemento:",elemento)


# for llave, valor in larouse.items():

#     print(f"La llave: {llave} ,tiene el valor: {valor}")


# larouse['cafe']="bebida aromatica"

# print(larouse)


# larouse.pop('cafe')

# print(larouse)


# Otras posibilidades (tener cuidado)

# lista_compleja = [12, ["hola","mundo"], (12,13,14),{1:"a",23:'r'}]

# print(lista_compleja)

#-----FUNCIONES------

# Una funcion es un codigo reusable que puede recibir 0 o mas parametros
# y siempre regresa un valor.


regreso = print("Hola Mundo!!!")
print(type(regreso))
print(regreso)


def mi_funcion():
    print("Hola Mundo Funcional!!!")
    # return None

print("R:", mi_funcion())

def f2(a=1000, b=100):
    return a + b

print("Regreso:", f2(10, 20))
print("Regreso:", f2(200))
print("Regreso:", f2())

def f3(*valores):
    print(type(valores))
    print(valores)
    suma = 0

    for ele in valores:
        suma += ele
    return suma

f3()
f3(2, 3)
resultado = f3(1, 2, 3, 4, 5, 56, 1234, 9)
print("La suma fue:", resultado)

