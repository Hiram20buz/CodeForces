import math
n=int(input())
lst=[]
for i in range(n):
    floor = 0
    total=list(map(int,input().split()))
    sum=total[0]-2
    if(sum > 0):
        floor=floor+1
    
    lst.append(math.ceil(sum/total[1])+1)
    
for i in lst:
    print(i)
