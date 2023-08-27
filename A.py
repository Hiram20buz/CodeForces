import math  
def x(li,lf,n):
    if(n==0):
        lst.append(lf)
        return lst
    
    else:
        result=math.ceil((lf+li)//2)
        lst.append(result)
        n = n-1
        return x(result,lf,n)
  
def check_decreasing_after_subtraction(lst):
    differences = [lst[i+1] - lst[i] for i in range(len(lst)-1)]
    is_decreasing = all(diff >= 0 for diff in differences)
    if(len(set(differences)) == len(differences) and is_decreasing ):
        return True
        
    else:
        return False      
        
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
