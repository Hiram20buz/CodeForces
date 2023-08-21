my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 100, 'k': 110, 'l': 120, 'm': 130, 'n': 140, 'o': 150, 'p': 160, 'q': 170, 'r': 180, 's': 190, 't': 200, 'u': 210, 'v': 220, 'w': 230, 'x': 240, 'y': 250, 'z': 260}
    
print(my_dict)
a = list('315045130113011000111')

i = 0
while i < len(a):
    if a[i] == '1':
        print(''.join(a[i:i+3]))
    i += 1
    
for j in range(len(a)):
    if a[j] == '1':
        print(''.join(a[j:j+3]))

#if a[i] == '1' and a[i+2] == '0' :
