import random

def guessNumber(x):
    print("####################################")
    print("####### Bienvenido al Juego! #######")
    print("####################################")
    print("## Tu meta es adivinar el Numero! ##")
    print("####################################")

    randomNumber = random.randint(1, x) #Numero aleatorio entre 1 y x

    predict = 0

    while predict != randomNumber:
        predict = int(input(f"Adivina un numero entre 1 y {x}: "))

        if predict < randomNumber:
            print("Intenta otra vez. Este numero es muy pequeño.")
        elif predict > randomNumber:
            print("Intenta otra vez. Este numero es muy grande.")

    print(f"Felicitaciones!!! Adivinaste el numero {randomNumber} correctamente!!")      


guessNumber(3)      