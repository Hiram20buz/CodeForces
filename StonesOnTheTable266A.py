l=int(input())
lst=list(input())
def rec(l,lst):
    x=0
    lon=len(lst)
    for i in range(0,lon//2):
        if(lst[i] == lst[i+1]):
            lst.pop(i+1)
            x += 1
    
    if(len(lst) == len or x == 0):
        return lst
        
    else:
        return rec(len(lst),lst)
        
        
#print(rec(l,lst))

def rec1(l,lst):
    x=0
    lon=len(lst)
    for i in range(lon-1,lon//2,-1):
        if(lst[i] == lst[i-1]):
            lst.pop(i-1)
            x += 1
    
    if(len(lst) == len or x == 0):
        return lst
        
    else:
        return rec(len(lst),lst)
   
f=rec1(len(rec(l,lst)),rec(l,lst))

print(l-len(f))



