""" convert list to comma separated string """
items = ['foo', 'bar', 'xyz']
print(', '.join(items))

""" list of numbers to comma separated """
numbers = [2,3,5,10]
print('-'.join(map(str,numbers)))

data = [2, 'hello', 3, 3.4]
print('='.join(map(str, data)))

a='abcdefghijklmnñopqrstuvwxyz'
print(a[::-1])
for char in reversed(a):
    print(char)

b=[1,3,4,5,6,7,8,9,10]
for el in a:
    if el == 0:
        break
else:
    print('did not break out for loop')        