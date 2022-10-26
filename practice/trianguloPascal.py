num = int(input("Introduce el numero de filas: "))
print(num)

for i in range(num):
    print(" " * (num-i), end=" ")
    print(" ".join(map(str, str(11**i))))