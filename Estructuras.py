#Estructuras
#- - - - - - - - - -

#Busqueda binaria

#Requisitos, lista ordenada de manera ascendente

nro = x     #Variable que se va modificando

a=[1,2,4,5,7,8,9]

min, max, pos = 0, len(a)-1, -1

while  min <= max and pos == -1:  
    medio = (min+max)//2    
    if nro == a[medio]:
        pos = medio         
    elif nro > a[medio]:
        min = medio + 1
    else:
        max = medio - 1

if pos != -1:
    print("EL valor no esta en la posicion", pos)
else:
    print("EL valor no esta en la lista")

#- - - - - - - - - -
#Busqueda secuencial --> Aplicada a una funcion

def busquedaSecuencial(lista, nro):             #Realizo la busqueda en la lista, usando el valor asignado que se dara
    for i in range(0, len(lista)):
        if nro == lista[i]:
            return 1
    return 0

#- - - - - - - - - -
#Valor repetido 

def repetido(a):
    band, i = 1, 0
    
    while band == 1 and i < len(lista):
        if a == lista[i]:
            band = 0
        i = i + 1
    return band

#- - - - - - - - - -

#Ordenamiento: Burbujeo
a=[25,3,35,7,4,1]

print(a)
for j in range(len(a)):
    for i in range(len(a)-1):   
        if a[i] > a[i+1]:      
            aux = a[i+1]
            a[i+1] = a[i]
            a[i] = aux
print(a)

#- - - - - - - - - -

#Ordemiento: Secuencial
print(a)        
for i in range(len(a)-1):   
    for j in range(i + 1, len(a)):   
            if a[i] > a[j]:      
                aux = a[j]
                a[j] = a[i]
                a[i] = aux
                band = 1
print(a)

#- - - - - - - - - -

#Ordenamiento: Insercion 

a=[5,9,3,1,2,8,4,7,6]

print(a)
# recoremos todos los elementos
for i in range(1, len(a)):
    # si el valor es inferior al anterior
    if a[i] < a[i-1]:
        #recorremos todos los elementos desde donde se encuentra el valor hasta el inicio de la lista
        for j in range(i,0,-1):
            # si el valor actual es inferior al anterior, lo movemos 
            if a[j]<a[j-1]:
                #reemplazamos el valor 
                a[j], a[j-1] = a[j-1], a[j]

                # se muestra la lista como va quedando
                print(a)

#- - - - - - - - - - -
# Pasar un numero a elementos de una lista

# Variables
lista = []

# Programa
nro = int(input("Ingrese el número a convertir a la lista: "))

while nro > 0:
    lista.append(nro%10)
    nro = nro // 10

print(lista)

#- - - - - - - - - - -
# eliminar elementos de una lista

# Lista de ejemplo
lista = [1, 2, 3, 4, 5]

# Función para verificar si un número cumple la condición requerida
def cumple_condicion(x):
    return x % 2 == 0

# Índice para recorrer la lista
i = 0

# Crear una nueva lista y agregar elementos que cumplan la condición
nueva_lista = []
while i < len(lista):
    if cumple_condicion(lista[i]):
        nueva_lista.append(lista[i])
    i += 1

# Asignar la nueva lista a la variable original
lista = nueva_lista

# Imprimir la lista modificada
print(lista)