"""leer los nros de legajo de los alumnos de un curso y su nota de examen final. El fin de la carga se determina ingresando un -1 como legajo. Se debe validar que la nota ingresada este entre 1 y 10. Terminada la lectura de datos, informar:

 * Cantidad de alumnos que aprobaron con nota mayor o igual a 4
 * Cantidad de alumnnos que desaprobaron el examen nota menor a 4
 * Promedio de nota y los legajos que superan el promedio
 
 Luego se solicita mostrar un listado de legajos y calificaciones ordenando de manera ascendente segun el numero de legajo. Resolver de dos formas: utilizando dos listas paralelas y utilizando una matriz de dos filas"""

lista_notas, lista_legajos = [], []

#Programa

#ingreso de datos
legajo = int(input("Ingrese el legajo: "))
while legajo != -1:
    nota = int(input("Ingrese la nota: "))

#definir nota entre 1 y 10
    while nota < 1 or nota > 10:
        print("la nota ingresada es incorrecta, porfavor ingrese a continuacion una nota entre 1 y 10: ")
        nota = int(input())

    lista_notas.append(nota)
    lista_legajos.append(legajo)
        
    legajo = int(input("ingrese otro legajo: "))

#cant de alumnos que aprobaron con nota >= 4
total_aprobados, total_desaprobados = 0, 0
for i in range(len(lista_notas)):
    if lista_notas[i] >= 4:
        total_aprobados += 1
#cant de desaprobados
    else:
        total_desaprobados += 1

#promedio y legajos que lo superan
promedio,suma_notas = 0, 0
for i in range (len(lista_notas)):
    suma_notas += lista_notas[i]
    promedio = suma_notas/len(lista_notas)

#impresiones 
if lista_notas == [] and legajo == -1:
    print ("No se introdujo ningun legajo")
else:
    print()
    print(lista_legajos) 
    print("\n",lista_notas, sep="")
    print("\nLa cantidad de alumnos que aprobo es:", total_aprobados)
    print("La cantidad de alumnos que desaprobo es:", total_desaprobados)
    print("\nEl promedio fue de:", promedio)
    print() 

    #pos = 0
    for i in range (len(lista_notas)):
        if lista_notas[i] > promedio:
            #pos = i
            #while pos == len(lista_legajos):
            #for j in range (len(lista_legajos)):
            print("* El alumno con legajo:", lista_legajos[i], "tuvo una nota por encima del promedio")

#ordenamiento listas
for j in range(len(lista_notas)):
    for i in range(len(lista_notas)-1):
        if lista_notas[i] > lista_notas[i+1]:
            aux = lista_notas[i+1]
            lista_notas[i+1] = lista_notas[i]
            lista_notas[i] = aux

            lista_legajos[i] > lista_legajos[i+1]
            aux2 = lista_legajos[i+1]
            lista_legajos[i+1] = lista_legajos[i]
            lista_legajos[i] = aux2

print()
print(lista_legajos)
print(lista_notas)