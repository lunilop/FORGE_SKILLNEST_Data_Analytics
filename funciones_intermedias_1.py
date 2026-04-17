# ------------------------------------ Ejercicio 1 ---------------------------------

# Actualizar valores en diccionarios y listas

print("\nEjercicio 1\n")

matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
matriz[1][0] = 6

# Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
cantantes[0]["nombre"] = "Enrique Martin Morales"

# En ciudades, cambia “Cancún” por “Monterrey”
ciudades["México"][2] = "Monterrey"

# En las coordenadas, cambia el valor de “latitud” por 9.9355431
coordenadas[0]["latitud"] = 9.9355431

print(matriz)
print(cantantes)
print(ciudades["México"])
print(coordenadas)


# ------------------------------------ Ejercicio 2 ---------------------------------

# Iterar a través de una lista de diccionarios

# Crea la función iterarDiccionario(lista) que reciba una lista de diccionarios y 
# recorra cada diccionario de la lista e imprima cada llave y el valor correspondiente. 

print("\nEjercicio 2\n")

cantantes2 = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

def iterarDiccionario(listaDic):
    for diccionario in listaDic:
        linea = []
        for llave, valor in diccionario.items():
            linea.append(f"{llave} - {valor}")
        print(", ".join(linea))
    
iterarDiccionario(cantantes2)


# ------------------------------------ Ejercicio 3 ---------------------------------

# Obtener valores de una lista de diccionarios

# Crea la función iterarDiccionario2(llave, lista), que reciba una cadena con el nombre de una llave y una lista de diccionarios. 
# La función debe imprimir el valor almacenado para esa clave de cada diccionario que se encuentra en la lista. 

print("\nEjercicio 3\n")

def iterarDiccionario2(llave, lista):
    for d in lista:
        if llave in d:
            print(d[llave])

# Pruebas
print("--- Nombres ---")
iterarDiccionario2("nombre", cantantes)
print("--- Paises ---")
iterarDiccionario2("pais", cantantes)


# ------------------------------------ Ejercicio 4 ---------------------------------

# Iterar a través de un diccionario con valores de lista

# Crea una función imprimirInformacion(diccionario), que reciba un diccionario en donde los valores son listas. 
# La función debe imprimir el nombre de cada clave junto con el tamaño de su lista y seguido de esto los valores de la lista para esa clave.

print("\nEjercicio 4\n")

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirInformacion(diccionario):
    for llave, lista_valor in diccionario.items():
        print(f"{len(lista_valor)} {llave.upper()}")

        for v in lista_valor:
            print(v)
        print("") 

imprimirInformacion(costa_rica)