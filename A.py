lst=[]
lst.append(100)
def x(li,lf,n):
    if(n==0):
        lst.append(lf)
        return lst
    
    else:
        result=(lf+li)//2+1
        lst.append(result)
        n = n-1
        return x(result,lf,n)
        

print(x(100,200,2))
