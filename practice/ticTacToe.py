tablero = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

def mostrarTablero():
    print("")
    for fila in tablero:
        print(fila)

def juego():
    mostrarTablero()
    while True:
        posicion = input('Juega X. Elige una posicion fila,columnna de 1 a 3')
        if posicion == 'salir':
            break

juego()          