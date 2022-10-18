numeroUsuario = int(input("De que numero quieres la tabla?"))

if numeroUsuario < 1:
    numeroUsuario = 1

print(f"#### Tabla de multiplicar del numero {numeroUsuario}####")    

for numeroTabla in range(1,11):
    print(f"{numeroUsuario} X {numeroTabla} = {numeroUsuario * numeroTabla}")
else:
    print("Tabla Finalizada.")
