lst=[]

for i in range(int(input())):
    w = input()
    size=len(w)
    '''
    if(size > 10):
        lst.append(w[0]+str(size-2)+w[size-1])
    else:
        lst.append(w)
    '''
    #result = (w[0]+str(size-2)+w[size-1]) if size > 10 else w
    lst.append((w[0]+str(size-2)+w[size-1]) if size > 10 else w)


    
for i in lst:
    print(i)
