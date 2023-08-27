import math  
def x(li,lf,n):
    if(n==0):
        lst.append(lf)
        return lst
    
    else:
        result=math.ceil((lf+li)/2)
        lst.append(result)
        n = n-1
        return x(result,lf,n)
  
def check_decreasing_after_subtraction(lst):
    dif=[]
    for i in range(len(lst)-1):
        dif.append(lst[i+1]-lst[i])
    
    return all(dif[i] > dif[i+1] for i in range(len(dif)-1))

def y(x,i):
    if check_decreasing_after_subtraction(x):
        if(len(set(x)) == len(x)):
            return x
        else:
            return [-1]
    elif i<len(x)-1:
        x[i]=x[i]+1
        return y(x,i+1)
        
    elif i == len(x)-2 :
        return [-1]
        
l=int(input())
total=[]

for i in range(l):
    lst1=list(map(int,input().split()))
    n = lst1[len(lst1)-1]
    lst=[]
    lst.append(lst1[0])
    final=x(lst1[0],lst1[len(lst1)-2],n-2)
    total.append(y(final,1))
    
for sublist in total:
    print(*sublist)
