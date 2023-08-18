lst = [((w[0]+str(size-2)+w[size-1]) if (size := len(w := input())) > 10 else w) for i in range(int(input())) ]

for i in lst:
    print(i)
    
'''
print("in new line")
print('\n'.join(map(str, lst)))
'''
