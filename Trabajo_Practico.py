#Aplicacion de gestion de contactos
"""Implementar una aplicación de gestión de contactos utilizando
diccionarios para almacenar datos, listas para manejar contactos,
matrices para organizar datos en vistas, manejo de excepciones
para validación, recursividad para búsquedas, y Git para control
de versiones. Incluir lectura y escritura de archivos."""


# Función para añadir un contacto
def agregar_contacto(liContactos,liTelefonos):
    
    Nombre=input("Ingrese nombre de contacto. Finalice con -1: ")
    Telefono=0
    while Nombre!="-1":

        Telefono=int(input("Telefono: " ))
        #validar sin duplicado
        i=validar_telefono(liTelefonos,Telefono)
        if i==1:
            liContactos.append(Nombre)
            
                       
        Nombre=input("Ingrese nombre de contacto. Finalice con -1: " )


# Función de validación
def validar_telefono(LiTelefonos,telefono):
    j=-1
    
    # Verificar si el teléfono ya está en la lista
    if telefono not in LiTelefonos:
        LiTelefonos.append(telefono)
        j=1
    else:
        print("El teléfono ya pertenece a un contacto.")
        
    return j

"""
Puntos a corregir / añadir:
    * Agregar diccionrio de variables para un mejor entendimiento de desarrollo en trabajo de equipo
    * Tomar el número de telefono como cadena de caracteres? 
    * Validar el tipo de contacto que se ingresa. A que tipo de orden pertenece (personal, oficina, correo electronico, telefono fijo)
    * Utilizacion de una matriz para su mejor manejo y gestion
    * Utilizacion de diccionario, para encapsular contacto y medios de contacto
    * Funcion agregar_contacto() hacer general el parametro de ingreso para su posible reutilizacion
    * El bucle de carga de contacto no finaliza al ingresar -1 (tomarlo como string? int?)
    
    """


#Programa Principal
        
LiContactos = []
LiTelefonos=[]        
        
agregar_contacto(LiContactos,LiTelefonos)

print (LiContactos)
print (LiTelefonos)