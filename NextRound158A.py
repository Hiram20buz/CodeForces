x=0
l=list(map(int,input().split()))
total=list(map(int,input().split()))
for i in range(l[0]):
    if(total[i] >= total[l[1]-1] and total[i] > 0):
        x += 1
    
print(x)
