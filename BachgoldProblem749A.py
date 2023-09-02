n=int(input())
lst=[]
def x(lst,n):
    if(n % 2 !=0):
        lst.append(3)
        
    while(sum(lst)<n):
        lst.append(2)
        if sum(lst) > n:
            lst.pop()
            break
        
x(lst,n) 
print(len(lst))
print(*lst)
