lst=[]

for i in range(int(input())):
    w = input()
    size=len(w)
    if(size > 10):
        lst.append(w[0]+str(size-2)+w[size-1])
    else:
        lst.append(w)
    
for i in lst:
    print(i)
