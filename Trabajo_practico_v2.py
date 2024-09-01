# Función para añadir un contacto
def agregar_contacto(contactos):
    while True:
        nombre = input("Ingrese nombre de contacto. Finalice con -1: ")
        if nombre == "-1":
            break

        # Creación del diccionario para el contacto
        contacto = {"Nombre": nombre} # 'nombre del diccionario' = {'nombre de la clave' : 'valor'}


        # Establecimiento de tipos y valores a las claves del dicionario 
        tipo_contacto = input("Tipo de contacto (movil, oficina, email, fijo). Finalice con -1: ")
        if tipo_contacto != "-1":
            contacto["Tipo de Contacto"] = tipo_contacto        # --> Se le asigna al elemento 'Tipo de contacto' el metodo de registro previamente seleccionado

        telefono = input("Número de teléfono. Finalice con -1: ")
        if telefono != "-1":
            contacto["Telefono"] = telefono         # --> Se le asigna al elemento 'Telefono' un el valor numerico previamente ingresado

        email = input("Email. Finalice con -1: ")
        if email != "-1":
            contacto["Email"] = email       # --> Se le asigna al elemento 'Email' un el valor string previamente ingresado


        # Validar si el teléfono ya existe (si el teléfono fue ingresado) --> buscamos validar invocando otra funcion, dentro de esta 
        if "Telefono" in contacto:
            if validar_telefono(contactos, contacto["Telefono"]):
                contactos.append(contacto)
        else:
            contactos.append(contacto)

    return contactos


# Función de validación
def validar_telefono(contactos, telefono):
    for contacto in contactos:
        if "Telefono" in contacto and contacto["Telefono"] == telefono: # --> si el elemento de la lista 'telefono' esta en la lista (contactos) y el elemento de la lista (telefono) es igual a telefono, todo esto dentro de un 'para contactos (c/ elemento) en contactos (lista)'. Entonces el telefono existe y esta repetido. 
            print("El teléfono ya pertenece a un contacto.")
            return False
    return True


# Programa Principal
contactos = agregar_contacto([]) # Ingresa, utilizando una funcion, los elemento a la lista siendo a su ves estos elementos diccionarios que permiten registrar el nombre y valor (en este caso tipo de contacto) a imprimir 

# Impresión en pantalla
print("Contactos agregados:")
for contacto in contactos: #Para '1er contacto (nombre)' en 'lista de contactos'
    print(f"Nombre: {contacto.get('Nombre', 'N/A')}") #metodo (.get), busca el valor de la clave en el diccionario, en esta caso para imprimir. En caso de no encontrarlo devuelve N/A
    print(f"Tipo de Contacto: {contacto.get('Tipo de Contacto', 'N/A')}") #metodo anteriormente mensionado
    print(f"Telefono: {contacto.get('Telefono', 'N/A')}") #""
    print(f"Email: {contacto.get('Email', 'N/A')}") #""
    print("-" * 20)

#f: permite ingresar toda una cadena de caracteres (strings) y realizar la impresion de las variables dentro de los llaves ( '{}' ) 


"""Consulta para la clase del martes 03/09:
    * Implementacion de matrices. Donde seria mas correctamente usarlas? (por el momento, se me ocurre en cunjunto a los diccionarios)
    * Establecer ingresos de datos por fuera de la funcion: agregar_contacto()
    * Es la funcion suficientemente general? de que forma puede ser aplicada mas general?
    * Metodo distinto (sugerido) para finalizar un ingreso? 
    * Distinguir los ingresos de datos de los contactos, ej.: se quiere ingresar el numero sobre la el 'movil' comprobar que este este compuesto por: - inicio de telefono: 11  - seguido por los 8 siguientes numeros: 1234-5678. Asi con el resto de tipos de contactos
    * Verificar si el tipo de contacto esta correctamente especificado, en caso contrario solicitarlo hasta que sea correcto"""
