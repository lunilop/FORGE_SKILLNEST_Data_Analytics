# ------------------------------------ Ejercicio 1 ---------------------------------

#  imprime todos los números enteros del 0 al 100.

print("\nEjercicio 1\n")

for i in range (101):
    print(i, end=" ")

print("\n")


# ------------------------------------ Ejercicio 2 ---------------------------------

#  imprime todos los números múltiplos de 2 entre 2 y 500

print("\nEjercicio 2\n")

for m in range (2, 501):
    if m % 2 ==0:
        print(m, end=" ")

print("\n")


# ------------------------------------ Ejercicio 3 ---------------------------------

# imprime los números enteros del 1 al 100. 
# Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”

print("\nEjercicio 3\n")

for j in range (1, 101):
    
    if j % 10 == 0:
        print("baby")
    elif j % 5 == 0:
        print("ice ice")    
    else:   
        print(j, end="  ")

print("\n")


# ------------------------------------ Ejercicio 4 ---------------------------------

#  suma los números pares del 0 al 500,000 e imprime la suma total.

print("\nEjercicio 4\n")

suma = 0
for s in range (500000):
    suma += s
    
print(suma)
print("\n")


# ------------------------------------ Ejercicio 5 ---------------------------------

#  imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.

print("\nEjercicio 5\n")

for r in range (2024,0,-3):
    print(r, end=" ")

print("\n")


# ------------------------------------ Ejercicio 6 ---------------------------------

# establece tres variables: numInicial, numFinal y multiplo. 

# Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo. 
# Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas).

print("\nEjercicio 6\n")

numInicial = 3
numFinal = 10
multiplo = 2

for v in range (numInicial, numFinal + 1):
    if v % multiplo == 0:
        print(v, end= " ")

print("\n")