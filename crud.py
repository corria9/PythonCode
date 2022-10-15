class Contacto :
    def __init__(self, pNombre, apellido, telefono, correo):
        self.nombre = pNombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}, Tel: {self.telefono}, eMail: {self.correo}"
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido  
    def setNombre(self, pNombre):
        self.nombre = pNombre      
    def setApellido(self, pApellido):
        self.apellido = pApellido
    def setTelefono(self, pTelefono):
        self.telefono = pTelefono
    def setCorreo(self, pCorreo):
        self.correo = pCorreo        

def modificar():
    informar()
    indice = int(input("Ingrese el numero de contacto que desea Modificar: "))
    nombre = input("Ingrese nuevo nombre: ")

def borrar():
    informar()
    indice = int(input("Ingrese el numero de contacto que desea borrar: "))
    print(f"Esta seguro de eliminar a {listaContactos[indice - 1].getNombre()} {listaContactos[indice - 1].getApellido()}")
    respuesta = input("S - Borrar ### N - No Borrar")
    if(respuesta == "s"):
        listaContactos.remove(listaContactos[indice - 1])

def agregar(): #funcion o metodo
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    telefono = input("Ingrese telefono: ")
    correo = input("Ingrese correo: ")
    contactoNuevo = Contacto(nombre, apellido, telefono, correo)
    listaContactos.append(contactoNuevo)
    #print(contactoNuevo)

def informar():
    print(" ")
    print("###############   Informe   ###############")
    for indice in range(0, len(listaContactos)):
        print(f"{indice + 1} - {listaContactos[indice]}")
    
    #for contacto in listaContactos:
    #    print(contacto)
    
#Inicio del Programa
listaContactos = []   
contacto1 = Contacto('Armando', 'Coria', 5539809876, 'armando.coria@gmail.com')
contacto2 = Contacto('Juan', 'Fierros', 5509897656, 'juan.fierros@gmail.com')
listaContactos.append(contacto1)
listaContactos.append(contacto2)
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
    elif(opcion == 'b'):
        borrar()  
    elif(opcion == 'm'):
        modificar()      
    else:   
        print("Opcion Incorrecta")