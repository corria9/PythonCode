from statistics import correlation


class Contacto :
    def __init__(self, pNombre, apellido, telefono, correo):
        self.nombre = pNombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}, Tel: {self.telefono}, eMail: {self.correo}"

def agregar(): #funcion o metodo
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    telefono = input("Ingrese telefono: ")
    correo = input("Ingrese correo: ")
    contactoNuevo = Contacto(nombre, apellido, telefono, correo)
    listaContactos.append(contactoNuevo)
    print(contactoNuevo)

def informar():
    print(" ")
    print("###############   Informe   ###############")
    for indice in range(0, len(listaContactos)):
        print(f"{indice + 1} - {listaContactos[indice]}")
    
    #for contacto in listaContactos:
    #    print(contacto)

#Inicio del Programa
listaContactos = []   
opcion = ' '
  
while(opcion != 'x'):
    print("###############   Agenda   ###############")
    print("####      A - Agregar Contactos       ####")
    print("####      M - Modificar Contactos     ####")
    print("####      I - Informe de Contactos    ####")
    print("####      B - Borrar Contactos        ####")
    print("####      X - Salir                   ####")
    print("##########################################")   
    opcion = input ("Ingrese la opcion deseada: ")
    
    if(opcion == 'x'):
        print("Saliendo....")
    elif(opcion == 'a'):    
        agregar()
    elif(opcion == 'i'):    
        informar()
    else:   
        print("Opcion Incorrecta")