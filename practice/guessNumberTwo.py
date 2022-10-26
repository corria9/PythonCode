import random


def adivina_el_numero_computadora(x):

    print("#########################################")
    print("########## Bienvenido al Juego! #########")
    print("#########################################")
    print(f"## Selecciona un numero entre 1 y {x} ##")
    print("#########################################")

    limite_inferior = 1
    limite_superior = x

    respuesta = " "

    while respuesta != "c":
        #Generar prediccion
        if limite_inferior != limite_superior: #[1, 10]
            prediccion = random.randint(limite_inferior, limite_inferior)
        else: 
            prediccion = limite_inferior    

        #Obtener respuesta del usuario
        respuesta = input(f"Mi prediccion es {prediccion}. Si es muy alta, ingresa (A). SI es muy baja, ingresa (B). SI es correcta, ingresa (C) ").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1    
        elif respuesta == "b":
            limite_inferior = prediccion + 1

    print(f"Siiii! La computadora adivino tu numero correctamente: {prediccion}")    


adivina_el_numero_computadora(3)            