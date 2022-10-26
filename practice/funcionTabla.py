def tabla(numero):
    print(f"Tabla de multiplicar del numero: {numero}")

    for contador in range(11):
        operacion = numero * contador
        print(f"{numero} X {contador} = {operacion}")

    print("\n")

tabla(2) 
tabla(10)        