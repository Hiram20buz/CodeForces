l=list(map(int,input().split()))
for i in range(l[1]):
    if(l[0]%10 == 0):
        l[0]=l[0]//10
    else:
        l[0]=l[0]-1
    
print(l[0])
