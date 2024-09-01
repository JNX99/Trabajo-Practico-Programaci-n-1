def busqueda_secuencial(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

# Ejemplo de uso
mi_lista = [4, 2, 7, 1, 9, 5]
elemento_buscado = 7
resultado = busqueda_secuencial(mi_lista, elemento_buscado)
if resultado != -1:
    print(f"El elemento {elemento_buscado} se encuentra en la posición {resultado}.")
else:
    print(f"El elemento {elemento_buscado} no se encuentra en la lista.")