#Practica Uno
numeros = []
longitud_lista = int(input("Cuantos datos vas a ingresar en la lista?: "))

for _ in range(longitud_lista):
    numeros.append(int(input("Introduce un numero entero: ")))

suma = sum(numeros)
print(f"\nLista: {numeros} \nLa suma total de los elementos es: {suma}")
print(len(numeros))


#Practica Dos
lista = ['a', 'A', 'marioneta', 'Marioneta', 'MARIONETA', 'z', 'Z', 'z', 'cache', 'Cache' ]
print(f"Lista Original: {lista}")

elemento = input("Introduce el elemento que deseas eliminar: ")

for _ in lista:
    if elemento.lower() in lista:
        lista.remove(elemento.lower())
    elif elemento.upper() in lista:
        lista.remove(elemento.upper())

print(f"Elemento eliminado: {lista}")

#Practica Tres
numeros = [1,2,3,4,5,67,8,9,7,6,5]
print(f"Lista numeros: {numeros}")

numeros_eliminados = []
numeros_eliminados.append(numeros.pop(0))#Eliminando el primer numero
numeros_eliminados.append(numeros.pop())#Eliminando el ultimo numero

print(f"Lista Numeros: {numeros} \n Lista numeros eliminados: {numeros_eliminados}")