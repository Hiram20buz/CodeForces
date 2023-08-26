def x(li,lf,n):
    if(n==0):
        lst.append(lf)
        return lst
    
    else:
        result=(lf+li)//2+1
        lst.append(result)
        n = n-1
        return x(result,lf,n)
        
        
l=int(input())
total=[]

for i in range(l):
    lst1=list(map(int,input().split()))
    n = lst1[len(lst1)-1]
    lst=[]
    lst.append(lst1[0])
    final=x(lst1[0],lst1[len(lst1)-2],n-2)
    if(len(set(final)) == len(final)):
        total.append(final)
    else:
        total.append([-1])
    
for sublist in total:
    print(*sublist)
