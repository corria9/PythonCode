words = input("Enter some text: ")

print(f"You entered: {words}")
words = words.split(' ')

for i in words:
    if len(i) >= 3:
        i = i + "%sfu" %(i[0])
        i = i[1:]
        print(i)
    else:
        pass
        